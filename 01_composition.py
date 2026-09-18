"""
01_composition.py
=================

**THE ONE STAGE.** Reads the sources, checks them, corrects what is
established, and writes the traction-motor composition dataset.

    Press Run. No arguments -- every setting is in `src/params_schema.py`.

    read -> audit -> verify the stator reading -> correct -> audit again
                  -> write the dataset

WHAT IT WRITES, into `output.data_dir`:

    TractionMotor_composition.xlsx   the dataset, in the RAWCLIC house schema,
                                     with this project's own quality columns
    TractionMotor_composition.csv    the same, for anything that reads text
    composition_audit.csv            every finding, before and after
    composition_corrections.csv      what each correction changed

ONE STAGE AND NOT FOUR. Auditing, verifying and correcting are one argument,
not three tasks: the correction exists because the audit found something, and
the audit afterwards is how we know the correction worked. Run separately they
could disagree about which version of the data they were looking at.

⚠️ WHAT THIS DATASET IS. The **current** composition -- the fleet as the
sources describe it, corrected. It is NOT a trajectory. Of the years
`run.years` asks for, one is measured; everything else is a modelling decision
that §4 of METHODOLOGY.md builds and this stage does not.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.bootstrap import ensure_venv

ensure_venv()

import pandas as pd                                        # noqa: E402

from src.composition import (CITATION, apply_corrections,   # noqa: E402
                             audit, components, declared,
                             figure_critical, figure_factors,
                             figure_motor_mass, load, trajectory)
from src.params_schema import ParameterError, current       # noqa: E402

STEM = 'TractionMotor_composition'


def _rule(title: str) -> None:
    print(f'\n{title}\n{"-" * len(title)}')


def _severities(findings: pd.DataFrame) -> str:
    counts = findings.severity.value_counts()
    return '  '.join(f'{name} {int(counts.get(name, 0))}'
                     for name in ('blocking', 'gap', 'note'))


def verify_stator(frame, bench, params) -> str:
    """
    Which reading of a component mass the evidence supports.

    ⚠️ WEIGHS EVIDENCE, DOES NOT PROVE. Drexler's min and max are the extremes
    of a 46-machine sample, not physical limits. What carries the conclusion is
    the margin between the two readings, not that anything lies outside.
    """
    data = params.data
    lamination = bench[bench.part == 'statorSheetLaminationStack'].iloc[0]
    low, high = float(lamination['min']), float(lamination['max'])
    key = ['componentKeyLevel1', 'productKeyLevel3']

    stator = frame[(frame.parameterCode == data.component_of_product) &
                   (frame.componentKeyLevel2 == 'stator')].set_index(key)['meanValue']
    winding = frame[(frame.parameterCode == data.material_of_component) &
                    (frame.componentKeyLevel2 == 'stator') &
                    (frame.componentKeyLevel3 == 'windings')].set_index(key)['meanValue']
    table = pd.DataFrame({'stator': stator, 'winding': winding}).dropna()

    print(f'  benchmark: stator lamination, n={int(lamination.n)}, '
          f'{low}-{high} kg, mean {lamination["mean"]} kg ({lamination["where"]})')
    outside = {}
    for reading, values in (('a', table.stator - table.winding),
                            ('b', table.stator)):
        outside[reading] = int(((values > high) | (values < low)).sum())
        print(f'  reading ({reading}): implied lamination '
              f'{values.min():6.2f} - {values.max():6.2f} kg   '
              f'outside the sample: {outside[reading]} of {len(values)}')
    best = min(outside, key=outside.get)
    print(f'  -> ({best}) is much better supported '
          f'({outside["b"] if best == "a" else outside["a"]} against '
          f'{outside[best]} outside)')
    return best


def main() -> int:
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1

    _rule('Sources')
    frame = load(params, 'zenodo')
    bench = components()
    print(f'  zenodo       {len(frame)} rows')
    print(f'  drexler2025  {len(bench)} component statistics')
    print(f'               {CITATION}')

    _rule('Audit of the source')
    before = audit(frame, params)
    print(f'  {len(before)} findings   {_severities(before)}')
    for check, group in before.groupby('check', sort=False):
        print(f'    [{group.severity.iloc[0]:8}] {check:<28} {len(group):>3} rows')

    _rule('Which reading of a component mass')
    verify_stator(frame, bench, params)

    _rule('Corrections')
    for _, row in declared().iterrows():
        print(f'  [{"applied" if row.applied else "declared":>8}] {row.id}')
    corrected, log = apply_corrections(frame, params)
    print()
    for _, row in log.iterrows():
        print(f'  {row.id:<34} {row.rows_changed:>3} rows   {row.what}')

    empty = log[log.rows_changed == 0]
    if not empty.empty:
        print('\n  ⚠️  matched nothing -- written against a workbook that has '
              'since changed:')
        for _, row in empty.iterrows():
            print(f'       {row.id}')

    _rule('Audit of the result')
    after = audit(corrected, params)
    print(f'  {len(after)} findings   {_severities(after)}')
    resolved = sorted(set(before.check) - set(after.check))
    if resolved:
        print(f'  resolved:  {", ".join(resolved)}')
    blocking = sorted(set(after[after.severity == 'blocking'].check))
    print(f'  blocking:  {", ".join(blocking) if blocking else "none"}')

    marked = corrected[corrected.get('reliability', '') == 'unreliable'] \
        if 'reliability' in corrected.columns else corrected.iloc[0:0]
    if not marked.empty:
        print(f'\n  kept as published and marked unreliable: {len(marked)} rows')
        for flag, rows in marked.groupby('flag'):
            values = rows.meanValue.dropna()
            print(f'    {flag}: {len(rows)} rows'
                  + (f', {values.min():.2f}-{values.max():.2f} kg' if len(values) else ''))

    _rule('Trajectory to 2070')
    series = trajectory(corrected, params)
    years = sorted(set(series.productionYear))
    basis = series.groupby('yearBasis')['productionYear'].nunique()
    print(f'  {len(series)} rows   {len(years)} years '
          f'{min(years)}-{max(years)}   '
          f'{len(params.scenario.conductor_diameter)} voltage classes')
    for name in ('measured', 'projected', 'backcast'):
        if name in basis:
            print(f'    {name:<10} {int(basis[name])} years')

    print('\n  material efficiency, mass as a share of '
          f'{params.scenario.base_year}:')
    from src.composition import factor as _factor
    classes = list(params.scenario.floor)
    print('      year  ' + ' '.join(f'{k:>11}' for k in classes))
    for year in years:
        if year < params.scenario.base_year:
            continue
        print(f'      {year}  '
              + ' '.join(f'{_factor(year, k, params):>11.3f}' for k in classes))

    print(f'\n  voltage, copper mass relative to '
          f'{params.scenario.base_voltage} V:')
    for volts, diameter in params.scenario.conductor_diameter.items():
        print(f'      {volts:>5} V   diameter {diameter:.3f}  ->  '
              f'cross-section and mass {diameter ** 2:.1%}')

    _rule('Written')
    os.makedirs(params.output.data_dir, exist_ok=True)
    os.makedirs(params.output.figures_dir, exist_ok=True)
    out = os.path.join(params.output.data_dir, STEM)

    # The CURRENT composition, in all three voltage classes. The corrected
    # frame itself has no voltage dimension -- the source describes the 400 V
    # fleet -- so the current dataset is the trajectory at the base year,
    # which is where the variants are built.
    current_year = series[series.productionYear == params.scenario.base_year]

    corrected.to_csv(f'{out}.csv', index=False)
    current_year.to_csv(f'{out}_current.csv', index=False)
    series.to_csv(f'{out}_trajectory.csv', index=False)
    with pd.ExcelWriter(f'{out}.xlsx', engine='openpyxl') as writer:
        current_year.to_excel(writer, sheet_name='composition_current',
                              index=False)
        for volts in params.scenario.conductor_diameter:
            block = current_year[current_year.voltageClass == volts]
            block.to_excel(writer, sheet_name=f'current_{volts}V', index=False)
        after.to_excel(writer, sheet_name='findings', index=False)
        log.to_excel(writer, sheet_name='corrections', index=False)
        declared().to_excel(writer, sheet_name='corrections_declared', index=False)
        bench.to_excel(writer, sheet_name='benchmark_drexler2025', index=False)
    audit_path = os.path.join(params.output.data_dir, 'composition_audit.csv')
    pd.concat([before.assign(stage='before'),
               after.assign(stage='after')]).to_csv(audit_path, index=False)

    figures = params.output.figures_dir
    made = [
        figure_factors(params, os.path.join(figures, '01_material_efficiency.png')),
        figure_motor_mass(series, params,
                          os.path.join(figures, '02_motor_mass.png')),
        figure_critical(series, params,
                        os.path.join(figures, '03_critical_materials.png')),
    ]

    print(f'  {out}.xlsx              {len(current_year)} rows, '
          f'{5 + len(params.scenario.conductor_diameter)} sheets')
    print(f'  {out}_current.csv       {len(current_year)} rows, '
          f'{len(params.scenario.conductor_diameter)} voltage classes')
    print(f'  {out}_trajectory.csv    {len(series)} rows')
    print(f'  {audit_path}')
    for path in made:
        print(f'  {path}')

    measured = [y for y in years if params.data.year_is_measured(y)]
    print(f'\n  ⚠️  {len(measured)} of {len(years)} years is measured '
          f'({", ".join(map(str, measured)) or "none"}).\n'
          f'      Everything else is scenario.floor and '
          f'scenario.initial_rate, not data.')
    return 0


def _years(spec: str):
    from src.params_schema import years_wanted
    return years_wanted(spec)


if __name__ == '__main__':
    raise SystemExit(main())
