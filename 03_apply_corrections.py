"""
03_apply_corrections.py
=======================

Applies the declared corrections and writes the corrected dataset.

    Press Run. No arguments.

THE SOURCE WORKBOOK IS NOT TOUCHED. It is a received deliverable under
`documentation/`. The corrected dataset is written to `data/`, where it is
plainly a product of this project and not something that can be mistaken for
what was handed over.

Every correction is declared in `src/corrections.py` with the evidence that
establishes it. This stage applies them, counts what each one changed, and
re-runs the audit against the result so that the effect is measured rather
than asserted.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.bootstrap import ensure_venv

ensure_venv()

import pandas as pd                                        # noqa: E402

from src.corrections import apply, declared                # noqa: E402
from src.params_schema import ParameterError, current      # noqa: E402
from src.source import audit, load                         # noqa: E402

CORRECTED_FILE = '03_corrected_composition.csv'
LOG_FILE = '03_corrections_log.csv'


def main() -> int:
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1

    frame = load(params, 'zenodo')
    before = audit(frame, params)

    print('Declared corrections:\n')
    for _, row in declared().iterrows():
        mark = 'APPLIED    ' if row.applied else 'NOT APPLIED'
        print(f'  [{mark}] {row.id}')
        print(f'      defect:   {row.defect}')
        print(f'      action:   {row.action}')
    print()

    corrected, log = apply(frame, params)

    print('What each one changed:')
    for _, row in log.iterrows():
        print(f'  {row.id:<34} {row.rows_changed:>3} rows   {row.what}')

    empty = log[(log.rows_changed == 0) & (log.id != 'C3-eesm-rotor-winding-mass')]
    if not empty.empty:
        print('\n⚠️  A correction matched nothing. It was written against a '
              'workbook that has\n    since changed:')
        for _, row in empty.iterrows():
            print(f'      {row.id}')

    after = audit(corrected, params)
    print(f'\nAudit before: {len(before)} findings '
          f'({int((before.severity == "blocking").sum())} blocking)')
    print(f'Audit after:  {len(after)} findings '
          f'({int((after.severity == "blocking").sum())} blocking)')

    gone = set(before.check) - set(after.check)
    left = sorted(set(after[after.severity == 'blocking'].check))
    if gone:
        print(f'  resolved: {", ".join(sorted(gone))}')
    if left:
        print(f'  blocking remaining: {", ".join(left)}')

    os.makedirs(params.output.data_dir, exist_ok=True)
    path = os.path.join(params.output.data_dir, CORRECTED_FILE)
    corrected.to_csv(path, index=False)
    log_path = os.path.join(params.output.data_dir, LOG_FILE)
    log.to_csv(log_path, index=False)
    print(f'\n{path}: written ({len(corrected)} rows, '
          f'{int((corrected.corrected != "").sum())} carrying a correction)')
    print(f'{log_path}: written')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
