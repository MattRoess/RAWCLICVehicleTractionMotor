"""
src/bootstrap.py
================

**Copyright notice:** Copyright © 2026 Empa, Matthias Roesslein

Run under this project's own interpreter, whatever was used to start the file.

WHY THIS EXISTS. The stages are started by pressing Run in Positron, and
Positron runs whichever interpreter its session happens to hold -- often a
pyenv or system Python with no pandas in it. The failure that produces is
`ModuleNotFoundError`, which reads like a missing package and is really a
missing interpreter, and the person then installs pandas into the wrong
environment and gets the same error again.

So each stage calls `ensure_venv()` before importing anything third-party, and
re-executes itself under `./.venv/bin/python` if that is not already what is
running.

⚠️ AND A RE-EXEC DOES NOT RELOAD `src/`. Positron keeps one long-lived session:
after editing a module under `src/`, the old module object is still in
`sys.modules` and the next Run uses yesterday's code. Restart the session after
editing `src/`. This bootstrap cannot fix that -- it fixes which interpreter,
not which session.
"""
from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENV_PYTHON = os.path.join(ROOT, '.venv', 'bin', 'python')


def ensure_venv() -> None:
    """
    Run under this project's interpreter, from this project's directory.

    ⚠️ IT ALSO CHANGES THE WORKING DIRECTORY, and that is not tidiness. Every
    path in `params_schema.py` is written from the project root --
    `data/raw/...`, `documentation/...` -- so a stage started from anywhere
    else fails on four settings at once with "which is not a file", which
    reads like the files are missing when they are simply being looked for in
    the wrong place. Positron and a terminal in another folder both do this.

    Anchored on this file's own location, so it is right however the stage was
    started.
    """
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    if os.path.abspath(os.getcwd()) != ROOT:
        os.chdir(ROOT)

    if os.path.abspath(sys.executable) == os.path.abspath(VENV_PYTHON):
        return
    if not os.path.isfile(VENV_PYTHON):
        # No project environment to switch to. Say so rather than failing later
        # on an import, which would name the package and not the cause.
        print(f'WARNING: {VENV_PYTHON} does not exist, so this is running under\n'
              f'         {sys.executable}\n'
              f'         Create it with:  python -m venv .venv && '
              f'./.venv/bin/pip install -r requirements.txt', file=sys.stderr)
        return
    os.execv(VENV_PYTHON, [VENV_PYTHON, os.path.abspath(sys.argv[0])])
