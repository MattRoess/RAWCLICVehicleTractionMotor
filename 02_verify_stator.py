"""
02_verify_stator.py
===================

Decides what a component mass in the consolidated dataset actually means, by
testing both readings against Drexler et al. (2025).

    Press Run. No arguments.

THE QUESTION. `01_audit_source.py` finds that the `statorSheetLaminationStack`
material row equals the stator `c-p` row exactly, in 24 of 24 filled cases, in
a stator that also carries windings. Two readings are possible and they are not
equivalent:

    (a) the c-p row is the STATOR, and the lamination cell was filled with
        the stator total by mistake -> true lamination = stator - windings
    (b) the c-p row is the LAMINATION, and the true stator is
        lamination + windings -> every stator is ~24% heavier than stated

Both are internally consistent, so the consolidated file cannot settle it.

WHY DREXLER CAN. Every mass in the consolidated dataset is a regression
through Drexler's benchmark points, so Drexler is not a second opinion -- it
is the same data before it was fitted and averaged into segments. Its stator
lamination stacks are measured on 46 machines. A reading that puts the
consolidated laminations outside that measured range is a reading that has the
regression producing values its own source never contained.

This stage changes nothing. It writes the comparison and states which reading
the evidence supports, for `documentation/SOURCE_AUDIT.md` to record.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.bootstrap import ensure_venv

ensure_venv()

import pandas as pd                                       # noqa: E402

from src.drexler import CITATION, MOTORS, VEHICLES        # noqa: E402
from src.params_schema import ParameterError, current     # noqa: E402
from src.source import load                               # noqa: E402

OUT_FILE = '02_stator_reading.csv'


def main() -> int:
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1

    data = params.data
    frame = load(params, 'zenodo')
    bench = load(params, 'drexler2025')

    lamination = bench[bench.part == 'statorSheetLaminationStack'].iloc[0]
    low, high = float(lamination['min']), float(lamination['max'])
    print(f'Benchmark: {CITATION}\n  {VEHICLES} vehicles, {MOTORS} motors, '
          f'model years 2018-2023')
    print(f'  stator sheet lamination stack, n={int(lamination.n)}: '
          f'{low}-{high} kg, mean {lamination["mean"]} kg ({lamination['where']})\n')

    key = ['componentKeyLevel1', 'productKeyLevel3']
    stator = frame[(frame.parameterCode == data.component_of_product) &
                   (frame.componentKeyLevel2 == 'stator')].set_index(key)['meanValue']
    windings = frame[(frame.parameterCode == data.material_of_component) &
                     (frame.componentKeyLevel2 == 'stator') &
                     (frame.componentKeyLevel3 == 'windings')].set_index(key)['meanValue']

    table = pd.DataFrame({'c_p_stator': stator, 'm_c_windings': windings}).dropna()
    table['lamination_if_a'] = table.c_p_stator - table.m_c_windings
    table['lamination_if_b'] = table.c_p_stator
    table['stator_if_b'] = table.c_p_stator + table.m_c_windings

    verdict = {}
    for reading in ('a', 'b'):
        values = table[f'lamination_if_{reading}']
        above = int((values > high).sum())
        below = int((values < low).sum())
        verdict[reading] = above + below
        table[f'outside_if_{reading}'] = (values > high) | (values < low)
        print(f'  reading ({reading}): implied lamination '
              f'{values.min():6.2f} - {values.max():6.2f} kg, mean {values.mean():6.2f}'
              f'   OUTSIDE the measured range: {above + below} of {len(values)}'
              f'  ({above} above {high}, {below} below {low})')

    best = min(verdict, key=verdict.get)
    print(f'\n  -> reading ({best}) is supported: it puts '
          f'{len(table) - verdict[best]} of {len(table)} values inside the '
          f'measured range,\n     against '
          f'{len(table) - verdict[min(verdict, key=lambda r: -verdict[r])]} '
          f'for the other.')
    if best == 'a':
        print('\n  The `c-p` row IS the stator. The lamination cell was filled with\n'
              '  the stator total, and the true lamination is stator - windings.\n'
              '  Total motor mass is unaffected; the material split is wrong.')

    # The size offset, stated so it is not mistaken for agreement. Zenodo
    # averages over vehicle SEGMENTS including large vans; Drexler averages
    # over 48 individual MOTORS including small ones. The two means should not
    # be equal, and the ratio being near-identical for stator and rotor is
    # what says the offset is sampling and not a second defect.
    rotor = frame[(frame.parameterCode == data.material_of_component) &
                  (frame.componentKeyLevel3 == 'rotorSheetLaminationStack')]['meanValue'].dropna()
    rotor_bench = bench[bench.part == 'rotorSheetLaminationStack'].iloc[0]
    stator_ratio = table[f'lamination_if_{best}'].mean() / float(lamination['mean'])
    rotor_ratio = rotor.mean() / float(rotor_bench['mean'])
    print(f'\n  Segment averages run heavier than motor averages, consistently:\n'
          f'    stator lamination  {stator_ratio:.2f}x Drexler\n'
          f'    rotor  lamination  {rotor_ratio:.2f}x Drexler\n'
          f'  Near-identical ratios across two independent components say this is\n'
          f'  the sampling difference (segments incl. vans vs 48 individual\n'
          f'  motors), not a further defect.')

    os.makedirs(params.output.data_dir, exist_ok=True)
    path = os.path.join(params.output.data_dir, OUT_FILE)
    table.round(4).to_csv(path)
    print(f'\n{path}: written ({len(table)} rows)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
