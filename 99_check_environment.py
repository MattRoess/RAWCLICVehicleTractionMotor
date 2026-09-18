"""
00_check_environment.py
=======================

Smoke test for a fresh checkout: proves the interpreter and the packages are
where the rest of this project will expect them, and profiles whatever
composition workbook is present.

Run it first, before writing or running anything else:

    ./.venv/bin/python 00_check_environment.py

There is deliberately NO hardcoded expected schema here. The traction-motor
composition workbook is not in this folder yet, and inventing the columns it
"should" have would mean checking the file against a guess. Instead this reports
what is actually in whatever .xlsx it finds -- sheets, shape, columns, and the
distinct values of every low-cardinality text column. Tighten it into a real
schema check once the workbook has arrived and been looked at.

For reference, `RAWCLICStockAndFlow/code/04_03_tractionmotors.py` reads the
workbook expecting `materialKeyLevel3`, `materialKeyLevel4`, `parameterCode` and
`value`, filtered to `params.materials.composition_parameter_code`. That is what
the consumer wants, not a verified description of the file.

It writes nothing.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

# A text column with at most this many distinct values is treated as a key
# column worth listing in full; anything wider is just summarised.
MAX_DISTINCT_TO_LIST = 30


def check_packages() -> None:
    print(f"Interpreter : {sys.executable}")
    print(f"Python      : {sys.version.split()[0]}")
    for name in ("pandas", "numpy", "scipy", "openpyxl", "matplotlib", "ipykernel"):
        try:
            module = __import__(name)
        except ImportError as exc:  # noqa: PERF203 -- one message per package is the point
            raise SystemExit(
                f"MISSING PACKAGE: {name} ({exc}). Install the pinned set with:\n"
                f"    ./.venv/bin/pip install -r requirements.txt"
            ) from exc
        print(f"  {name:<11} {getattr(module, '__version__', 'unknown')}")


def find_workbooks() -> list[Path]:
    return sorted(p for p in PROJECT_ROOT.glob("*.xlsx") if not p.name.startswith("~$"))


def describe_workbook(path: Path) -> None:
    import pandas as pd

    print(f"\nWorkbook    : {path.name}")
    # keep_default_na=False: these consolidated workbooks write a literal 'n/a'
    # where a level of detail does not apply. Left to pandas' defaults that
    # becomes NaN and the levels stop being distinguishable from each other.
    workbook = pd.ExcelFile(path)
    print(f"Sheets      : {len(workbook.sheet_names)} -- {workbook.sheet_names}")

    for sheet_name in workbook.sheet_names:
        frame = workbook.parse(sheet_name, keep_default_na=False, na_values=[""])
        print(f"\n  [{sheet_name}] {len(frame):,} rows x {len(frame.columns)} columns")
        print(f"  columns: {list(frame.columns)}")
        for column in frame.columns:
            values = {str(v) for v in frame[column]}
            if len(values) <= MAX_DISTINCT_TO_LIST:
                print(f"    {column} ({len(values)} distinct): {sorted(values)}")
            else:
                print(f"    {column}: {len(values):,} distinct values -- not listed")


def main() -> None:
    check_packages()

    workbooks = find_workbooks()
    if not workbooks:
        print(
            "\nNo .xlsx workbook in the project root yet -- expected, until the "
            "traction-motor composition file arrives. The environment itself is "
            "fine; there is simply nothing to read."
        )
    else:
        for path in workbooks:
            describe_workbook(path)

    print("\nEnvironment OK.")


if __name__ == "__main__":
    main()
