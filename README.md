# RAWCLICVehicleTractionMotor

What electric traction motors are made of, consolidated from the underlying
sources: give it a motor type, a torque, a voltage class and a year, get
kilograms per vehicle by material.

It is the traction-motor counterpart to `RAWCLICVehicleBattery` (batteries),
`RAWCLICVehicleComposition` (whole car) and `RAWCLICVehicleElectronics` (BEV
electronics), and it feeds
`RAWCLICStockAndFlow/code/04_03_tractionmotors.py`.

**Start with `documentation/HANDOVER.md`** -- what this stands on, what was
corrected and why, and what is still open. `documentation/METHODOLOGY.md` is
the long form.

---

## Running it

Two stages, in order. No arguments, and not by oversight: **every setting is in
`src/params_schema.py`**, so a switch that only exists on a command line is a
switch the person running this never sees.

```bash
./.venv/bin/python 00_parameters.py
./.venv/bin/python 01_composition.py
```

`00_parameters.py` validates the settings and regenerates `params.xlsx` and
`documentation/PARAMETER_REFERENCE.md` from them. Both are OUTPUTS -- editing
either changes nothing, because nothing reads them.

`01_composition.py` is the one stage: read the sources, audit them, verify the
stator reading, correct what is established, audit again, write the dataset and
the figures. Auditing and correcting are one argument, not two tasks.

### What it writes, into `data/`

`data/` has three folders and each says what is in it: **`raw/`** what this code
opens, **`composition/`** what it produces for its own use, **`consolidated/`**
the two files another repository reads. Nothing else lives under `data/` -- if a
file there is written by no stage in this repository, that is a bug, not an
archive.

Into `data/consolidated/`, which is the whole interface to the stock-and-flow
model and holds nothing else:

| file | |
|---|---|
| `TractionMotor_for_stockandflow.xlsx` | what `04_03_tractionmotors.py` reads, 13 299 rows, house schema |
| `TractionMotor_for_stockandflow.csv` | the same, for anything reading text |
| `draws/` | the 200 000 simulations: 31 `float32` `(200000, 12)` arrays, the torque grid, the year/voltage scale table and a manifest. A `.csv` of three percentiles is not a distribution -- see `HANDOVER.md`. |

Into `data/composition/`, for this project's own use:

| file | |
|---|---|
| `TractionMotor_composition_by_torque.csv` | **the deliverable.** 14 508 rows, no segment dimension |
| `TractionMotor_composition_trajectory.csv` | by segment, 13 338 rows |
| `TractionMotor_composition.xlsx` | current composition, 8 sheets, house schema |
| `composition_audit.csv` | every finding, before and after correction |

Plus seven figures in `figures/`.

`RAWCLICStockAndFlow` is pointed at `data/consolidated/` through
`params.materials.traction_composition_dir` and reads the workbook where it
lies, exactly as it reads `RAWCLICVehicleBattery/data/consolidated`. **It keeps
no copy** -- traction motor information lives in this project and nowhere else.

### Where a source lives, and why there are two places

**A file this code opens is in `data/raw/`.** Today that is the Zenodo
consolidated workbook and the EV Database fleet snapshot, and nothing else.
`documentation/` holds what is read by a person and transcribed -- the Drexler
paper, the practical and comprehensive reports, the critical review. The
Drexler PDF is declared in the registry and never opened, which is the whole
distinction: its numbers reached the code through a person.

Sources are declared in `data.sources` in `src/params_schema.py` -- **adding a
source is a declaration, not a code change**. `role` is a gate enforced in
code: `load()` refuses a verification source. The base is the Zenodo
consolidated dataset; what each source may do, and which two of them are not
independent, is `HANDOVER.md` §2.

### The smoke test

```bash
./.venv/bin/python 99_check_environment.py
```

It checks the interpreter and the pinned packages, and profiles any `.xlsx` it
finds in the project root -- sheets, shape, columns and the distinct values of
every low-cardinality column. It writes nothing. Today the only workbook in the
root is `params.xlsx`, so that is what it profiles.

### In Positron

Open this folder as the workspace. `.vscode/settings.json` already points the
interpreter at `.venv`, activates it in every terminal, and runs scripts from
the project root, so relative paths to the sources resolve the same way whether
the code runs from the console, a script or a notebook cell.

---

## The environment

Python 3.14.4, matching `RAWCLICStockAndFlow` and `RAWCLICVehicleBattery`.
Versions are pinned in `requirements.txt`; `ipykernel` is there because Positron
needs it to start a Python console.

```bash
~/.pyenv/versions/3.14.4/bin/python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

⚠️ **The project lives in iCloud Drive and `.venv` does not survive it.**
Working across two Macs left 222 empty directories under `site-packages` on
2026-09-21 -- `numpy/_utils/` among them, which fails as
`cannot import name 'set_module' from 'numpy._utils' (unknown location)` rather
than as a missing package. It is not repairable in place: delete `.venv` and run
the two lines above. Rebuilding takes about a minute, and no data or code is in
there.

## Data is not in the repository

Same rule as the sibling projects: `.gitignore` excludes every `.xlsx`, `.csv`,
`.pkl`, `.npy` and `.png`. A fresh clone gets the CODE ONLY and cannot run
until the source documents are supplied separately -- iCloud, shared drive,
however they are distributed -- and the deliverable is handed to the
stock-and-flow model directly, not through GitHub.
