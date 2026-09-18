"""
01_audit_source.py
==================

Checks the Zenodo consolidated dataset and writes what is wrong with it.

    Press Run. No arguments -- every setting is in `src/params_schema.py`.

WHY THIS RUNS FIRST. The consolidated workbook is the only measured source
this project has, so every mass it ever reports rests on it. This stage reads
it, applies the checks in `src/source.py`, prints a summary and writes the full
finding list to `data/01_source_audit.csv`.

IT CHANGES NOTHING. Not the workbook, not the values. A blocking finding is a
decision to be taken with a source behind it, recorded in
`documentation/SOURCE_AUDIT.md` -- not a correction to be applied quietly by
the stage that happens to notice it.

A NON-ZERO EXIT MEANS BLOCKING FINDINGS REMAIN. That is the normal state
today, and the point: the next stage cannot be trusted until they are settled.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.bootstrap import ensure_venv

ensure_venv()

from src.params_schema import ParameterError, current      # noqa: E402
from src.source import audit, load                         # noqa: E402

AUDIT_FILE = '01_source_audit.csv'


def main() -> int:
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1

    frame = load(params)
    print(f'{params.data.consolidated_file}\n  {len(frame)} rows, '
          f'{len(frame.columns)} columns\n')

    findings = audit(frame, params)

    counts = findings.severity.value_counts()
    for severity in ('blocking', 'gap', 'note'):
        print(f'  {severity:9s} {int(counts.get(severity, 0)):3d}')

    print('\nFindings, one line per check:')
    for check, group in findings.groupby('check', sort=False):
        severity = group.severity.iloc[0]
        print(f'\n  [{severity}] {check}  ({len(group)} rows)')
        # The first row carries the explanation; the rest differ only in which
        # motor and segment, and printing all of them buries the point.
        print(f'      {group.detail.iloc[0]}')
        motors = sorted(set(group.motor) - {'(all)', '(various)'})
        if motors:
            print(f'      affects: {", ".join(motors)}')

    os.makedirs(params.output.data_dir, exist_ok=True)
    path = os.path.join(params.output.data_dir, AUDIT_FILE)
    findings.to_csv(path, index=False)
    print(f'\n{path}: written ({len(findings)} findings)')

    blocking = int(counts.get('blocking', 0))
    if blocking:
        print(f'\n{blocking} BLOCKING findings. These are numbers that would be '
              f'wrong in the\nstock-and-flow model, not merely missing. See '
              f'documentation/SOURCE_AUDIT.md.')
    return 1 if blocking else 0


if __name__ == '__main__':
    raise SystemExit(main())
