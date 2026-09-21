"""
01_composition.py
=================

**THE ONE STAGE.** Reads the sources, checks them, corrects what is
established, and writes the traction-motor composition dataset.

    Press Run. No arguments -- every setting is in `src/params_schema.py`.

    read -> audit -> verify the stator reading -> correct -> audit again
                  -> write the dataset

WHAT IT WRITES. Into `output.consolidated_dir`, which is the entire interface
to the stock-and-flow model and holds nothing else:

    TractionMotor_for_stockandflow.xlsx   what 04_03_tractionmotors.py reads
    TractionMotor_for_stockandflow.csv    the same, for anything reading text

and into `output.data_dir`, for this project's own use:

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
                             composition_by_torque, export_stock_and_flow,
                             element_layer, figure_distributions,
                             figure_grade_scenarios,
                             heavy_rare_earth_scenarios,
                             magnet_element_check,
                             write_draws, write_element_draws,
                             figure_all_types,
                             figure_by_torque,
                             verify_by_torque,
                             audit, components, declared,
                             figure_critical, figure_factors,
                             figure_fleet, figure_motor_mass,
                             figure_topologies,
                             load, trajectory)
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
          f'{len(params.scenario.copper_mass)} voltage classes')
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
    for volts, ratio in params.scenario.copper_mass.items():
        print(f'      {volts:>5} V   copper mass {ratio:.1%} of '
              f'{params.scenario.base_voltage} V')

    _rule('Composition as a function of torque')
    # The dict comes back holding the per-draw arrays -- see write_draws.
    draws_out: dict = {}
    grid = composition_by_torque(corrected, params, draws_out=draws_out)
    print(f'  {len(grid)} rows   '
          f'{grid.torque_nm.nunique()} torque points '
          f'{grid.torque_nm.min():.0f}-{grid.torque_nm.max():.0f} Nm   '
          f'{grid.productionYear.nunique()} years   no segment')
    print(f'  {int(grid.extrapolated.sum())} rows beyond the fitted torque '
          f'range, flagged')

    check = verify_by_torque(grid, corrected, params)
    print(f'\n  does a torque give back what the segments say?')
    print(f'    {"motor":<24}{"material":<12}{"n":>3}{"Ø kg":>8}'
          f'{"Ø Fehler":>10}{"max":>8}{"R2":>7}')
    for _, row in check.iterrows():
        print(f'    {row.motor:<24}{row.material:<12}{int(row.n):>3}'
              f'{row.mean_kg:>8.2f}{row.mean_abs_error_pct:>9.1%}'
              f'{row.max_abs_error_kg:>8.2f}{row.r2:>7.3f}')

    _rule('Stock-and-flow export')
    export = export_stock_and_flow(grid, corrected, params)
    print(f'  {len(export)} rows   '
          f'{export.productKeyLevel3.nunique()} segments x '
          f'{export.componentKeyLevel1.nunique()} motor types x '
          f'{export.voltageClass.nunique()} voltages x '
          f'{export.productionYear.nunique()} years')
    print(f'  joins on productKeyLevel2 + productionYear, carries torque_nm, '
          f'p025/p975 and STD')
    borrowed = int(export.slopeBorrowed.sum())
    if borrowed:
        print(f'  {borrowed} rows have a borrowed slope, flagged')

    _rule('Written')
    os.makedirs(params.output.data_dir, exist_ok=True)
    os.makedirs(params.output.consolidated_dir, exist_ok=True)
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
    grid.to_csv(f'{out}_by_torque.csv', index=False)

    # THE FILE THE STOCK-AND-FLOW MODEL READS, and the only thing in
    # `consolidated_dir` -- that folder is the whole interface to the other
    # repository, which reads it where it lies rather than keeping a copy.
    # Sheet name follows the house convention that 04_03 has used so far, so a
    # rewritten consumer can keep it or not without this project having to
    # guess.
    export_path = os.path.join(params.output.consolidated_dir,
                               'TractionMotor_for_stockandflow.xlsx')
    with pd.ExcelWriter(export_path, engine='openpyxl') as writer:
        export.to_excel(writer, sheet_name='Consolidated data', index=False)
        declared().to_excel(writer, sheet_name='corrections', index=False)
        after.to_excel(writer, sheet_name='findings', index=False)
    export.to_csv(os.path.join(params.output.consolidated_dir,
                               'TractionMotor_for_stockandflow.csv'), index=False)
    with pd.ExcelWriter(f'{out}.xlsx', engine='openpyxl') as writer:
        current_year.to_excel(writer, sheet_name='composition_current',
                              index=False)
        for volts in params.scenario.copper_mass:
            block = current_year[current_year.voltageClass == volts]
            block.to_excel(writer, sheet_name=f'current_{volts}V', index=False)
        after.to_excel(writer, sheet_name='findings', index=False)
        log.to_excel(writer, sheet_name='corrections', index=False)
        declared().to_excel(writer, sheet_name='corrections_declared', index=False)
        bench.to_excel(writer, sheet_name='benchmark_drexler2025', index=False)
    # THE ELEMENT LAYER. HANDOVER §7.2: no e-m rows anywhere, so Nd, Pr, Dy
    # and Tb could not be reported. They can now, for the magnet.
    _rule('Elements of the magnet')
    em_rows, element_mass, fractions = element_layer(grid, draws_out, params)
    if not em_rows.empty:
        base = list(params.run.magnet_grade_scenarios)[0]
        for klass in params.run.magnet_grade_scenarios:
            names, drawn = fractions[('PMElectricMotors', klass)]
            shares = {name: drawn[:, position].mean()
                      for position, name in enumerate(names)}
            print(f'  {klass:2} grade, '
                  f'{params.data.magnet_grade_temperature[klass]:3} C'
                  f'{"  <- base" if klass == base else "        "}   '
                  f'Nd {shares["Nd"]:.3f}  Pr {shares["Pr"]:.4f}  '
                  f'Dy {shares["Dy"]:.4f}  Tb {shares["Tb"]:.4f}  '
                  f'Co {shares["Co"]:.4f}')
        checks = pd.DataFrame([
            magnet_element_check(params, motor, names, drawn, grade_class=klass)
            for (motor, klass), (names, drawn) in sorted(fractions.items())])
        # Per scenario, not averaged: the stated iron band is the same
        # 0.60-0.65 for SH, UH and EH while dysprosium and cobalt climb through
        # them, so the closure gets worse with the class -- which is itself the
        # evidence that the band is a nominal balance nobody recomputed.
        print('  iron is the balance; the stated band is 0.60-0.65 for all '
              'three classes:')
        for klass, block in checks.groupby('TempClass', sort=False):
            print(f'    {klass:2}  drawn {block.drawn_median.mean():.3f}   '
                  f'inside stated {100 * block.inside_stated.mean():5.1f}%   '
                  f'inside stated less cobalt '
                  f'{100 * block.inside_stated_less_cobalt.mean():5.1f}%')

        heavy = heavy_rare_earth_scenarios(element_mass, params)
        if not heavy.empty:
            mid = heavy[(heavy.componentKeyLevel1 == 'PMElectricMotors') &
                        (heavy.torque_nm == 400)]
            print(f'\n  What the grade costs, PMSM at 400 Nm, '
                  f'{params.scenario.base_year}:')
            for _, row in mid.iterrows():
                print(f'    {row.element:2} {row.grade_class:2} '
                      f'({row.TmaxOperating_C:3} C)  {row.kg_per_vehicle:.4f} kg'
                      f'   x{row.times_base:.2f} of {row.base_class}')
            heavy.to_csv(os.path.join(params.output.data_dir,
                                      'TractionMotor_heavy_rare_earth_scenarios.csv'),
                         index=False)

        em_rows.to_csv(os.path.join(params.output.data_dir,
                                    'TractionMotor_magnet_elements.csv'),
                       index=False)
        element_mass.to_csv(os.path.join(params.output.data_dir,
                                         'TractionMotor_element_mass_by_torque.csv'),
                            index=False)
        checks.to_csv(os.path.join(params.output.data_dir,
                                   'TractionMotor_element_checks.csv'), index=False)
        written = write_element_draws(fractions, params.output.draws_dir)
        print(f'\n  {len(em_rows)} e-m rows, {len(element_mass):,} element-mass '
              f'rows, {len(written)} chemistry draw arrays, '
              f'{len(params.run.magnet_grade_scenarios)} grade scenarios')

    # THE DISTRIBUTION ITSELF, not a summary of it.
    manifest = write_draws(draws_out, params, params.output.draws_dir)
    if not manifest.empty:
        print(f'  {params.output.draws_dir}: {len(manifest)} arrays, '
              f'{manifest.draws.iloc[0]:,} draws x '
              f'{manifest.torque_points.iloc[0]} torques, '
              f'{manifest.mbytes.sum():.0f} MB')

    audit_path = os.path.join(params.output.data_dir, 'composition_audit.csv')
    pd.concat([before.assign(stage='before'),
               after.assign(stage='after')]).to_csv(audit_path, index=False)

    figures = params.output.figures_dir
    # THE DRAWS AS DISTRIBUTIONS. Every other figure here is a line and a band;
    # these two plot the arrays themselves, including across all 13 years.
    distribution_figures = [
        figure_distributions(draws_out, params,
                             os.path.join(figures, '08_distributions.png')),
    ]
    if not em_rows.empty:
        distribution_figures.append(figure_grade_scenarios(
            element_mass, fractions, draws_out, params,
            os.path.join(figures, '09_magnet_grade_scenarios.png')))
    made = [
        figure_factors(params, os.path.join(figures, '01_material_efficiency.png'),
                       current=current_year),
        figure_motor_mass(series, params,
                          os.path.join(figures, '02_motor_mass.png')),
        figure_critical(series, params,
                        os.path.join(figures, '03_critical_materials.png')),
        figure_topologies(current_year, params,
                          os.path.join(figures, '04_topologies.png')),
        figure_fleet(params, os.path.join(figures, '05_fleet_demand.png')),
        figure_all_types(grid, params,
                         os.path.join(figures, '07_all_motor_types.png')),
        figure_by_torque(grid, params,
                         os.path.join(figures, '06_composition_by_torque.png'),
                         corrected=corrected),
    ] + distribution_figures

    print(f'  {out}.xlsx              {len(current_year)} rows, '
          f'{5 + len(params.scenario.copper_mass)} sheets')
    print(f'  {out}_current.csv       {len(current_year)} rows, '
          f'{len(params.scenario.copper_mass)} voltage classes')
    print(f'  {out}_trajectory.csv    {len(series)} rows')
    print(f'  {out}_by_torque.csv     {len(grid)} rows, no segment')
    print(f'  {export_path}   {len(export)} rows  <- stock-and-flow')
    print(f'  {audit_path}')
    for path in made:
        print(f'  {path}')

    # ⚠️ COMPOSITION VINTAGES, NOT COVERED YEARS. This line used to count every
    # year any data source was entitled to supply, which included the EV
    # Database's 2011-2026 -- and that source gives torque, never what a motor
    # is made of. It announced sixteen measured years where there is one
    # composition vintage.
    described = [y for y in years if params.data.year_has_composition(y)]
    primary = params.data.sources[params.data.primary]
    base = [y for y in years
            if primary['covers'][0] <= y <= primary['covers'][1]]
    print(f'\n  ⚠️  {len(base)} of {len(years)} years has a MEASURED '
          f'COMPOSITION ({", ".join(map(str, base)) or "none"}), from '
          f'{params.data.primary}.')
    if len(described) > len(base):
        others = [y for y in described if y not in base]
        print(f'      {len(described)} are covered by any composition source '
              f'({others[0]}-{others[-1]} adds {", ".join(sorted(set(
                  name for y in others
                  for name, e in params.data.covering(y, "data").items()
                  if e.get("reads") in params.data.composition_readers
                  and name != params.data.primary)))}).')
    print(f'      Every other year is scenario.floor and '
          f'scenario.initial_rate -- constructed, not data.')
    return 0


def _years(spec: str):
    from src.params_schema import years_wanted
    return years_wanted(spec)


if __name__ == '__main__':
    raise SystemExit(main())
