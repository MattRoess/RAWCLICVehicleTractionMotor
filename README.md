# RAWCLICVehicleTractionMotor

What electric traction motors are made of, consolidated from the underlying
sources.

It is the traction-motor counterpart to `RAWCLICVehicleBattery` (batteries),
`RAWCLICVehicleComposition` (whole car) and `RAWCLICVehicleElectronics` (BEV
electronics), and it feeds
`RAWCLICStockAndFlow/code/04_03_tractionmotors.py`.

**The composition workbook is not here yet.** The environment is ready and the
smoke test runs; there is simply nothing to read until the file arrives.
`RAWCLICStockAndFlow` expects it as
`20260309-Traction_motors_consolidated.xlsx`
(`params.materials.traction_composition_file_name`).

---

## Running it

```bash
./.venv/bin/python 00_check_environment.py
```

That is the smoke test: it checks the interpreter and the pinned packages, and
profiles any `.xlsx` it finds in the project root -- sheets, shape, columns and
the distinct values of every low-cardinality column. It writes nothing.

It deliberately has **no hardcoded expected schema**. Nobody here has seen the
traction workbook, so checking it against an invented list of columns would only
be checking it against a guess. It reports what is actually in the file instead.
Tighten it into a real schema check once the workbook has arrived and been
looked at.

For reference, `04_03_tractionmotors.py` reads the workbook expecting
`materialKeyLevel3`, `materialKeyLevel4`, `parameterCode` and `value`, filtered
to `params.materials.composition_parameter_code`. That is what the consumer
wants, not a verified description of the file.

### In Positron

Open this folder as the workspace. `.vscode/settings.json` already points the
interpreter at `.venv`, activates it in every terminal, and runs scripts from
the project root, so relative paths to the workbook resolve the same way whether
the code runs from the console, a script or a notebook cell.

### Rebuilding the environment from scratch

```bash
~/.pyenv/versions/3.14.4/bin/python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

Python 3.14.4, matching `RAWCLICStockAndFlow` and `RAWCLICVehicleBattery`.
Versions are pinned in `requirements.txt`; `ipykernel` is there because Positron
needs it to start a Python console.
