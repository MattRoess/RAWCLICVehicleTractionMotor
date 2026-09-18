"""
00_parameters.py
================

Regenerates `params.xlsx` and `documentation/PARAMETER_REFERENCE.md` from the
values in `src/params_schema.py`, and says what they are.

    ./.venv/bin/python 00_parameters.py

**To change a parameter, edit `src/params_schema.py`**, then press Run here to
refresh the register. The spreadsheet and the Markdown reference are OUTPUTS:
editing either of them changes nothing, because nothing reads them.

NO ARGUMENTS, AND NOT BY OVERSIGHT. This project is run by pressing Run on the
numbered stages; a switch that only exists on a command line is a switch the
person running this never sees.

This file is intentionally thin. Every parameter, its value and its
documentation live in `src/params_schema.py`; the writing lives in
`src/params_io.py`.
"""

from __future__ import annotations

import os
import sys

# Run under the project interpreter whatever was typed, and put the repo
# root on the path. Must come before any third-party import.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.params_io import PARAMS_FILE, reference, save
from src.params_schema import ParameterError, current, flatten, source_status

REFERENCE_FILE = os.path.join('documentation', 'PARAMETER_REFERENCE.md')


def main() -> int:
    """Validate the settings, print them and the sources, write the register."""
    try:
        params = current()
    except ParameterError as error:
        print(error, file=sys.stderr)
        return 1

    rows = flatten(params)

    print('src/params_schema.py is valid. Values in force:')
    for _, _, key, value in rows:
        print(f'  {key:<28} {value}')

    # The single thing most worth knowing before expecting a composition out of
    # this project: whether the workbooks it reads are actually there.
    print(f'\nSources\n  {source_status(params)}\n')

    save(params, PARAMS_FILE)
    print(f'{PARAMS_FILE}: regenerated ({len(rows)} parameters)')

    os.makedirs(os.path.dirname(REFERENCE_FILE), exist_ok=True)
    with open(REFERENCE_FILE, 'w') as handle:
        handle.write(reference(params))
    print(f'{REFERENCE_FILE}: regenerated')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
