# Source audit — the Zenodo consolidated dataset

`RAWCLIC_BEV_motor_consolidated_data_V1.xlsx`, 264 rows, 43 columns.
Produced by `01_audit_source.py`; the full finding list is
`data/01_source_audit.csv`.

**Run first, before anything consumes this workbook.** It is the only measured
source the project has (`METHODOLOGY.md` §2, tier 1), so every mass this
project reports rests on it. A defect here does not announce itself
downstream — it arrives as a plausible number in a figure.

**53 findings: 38 blocking, 13 gaps, 2 notes.** Blocking means a number that
would be *wrong* in the stock-and-flow model, not merely missing.

---

## What the workbook actually contains

| | |
|---|---|
| rows | 264 — **52 `c-p`, 212 `m-c`, 0 `e-m`** |
| motors | `PMElectricMotors` 110, `EESMElectricMotors` 110, `IMandPMElectricMotors` 44 |
| segments | 11 — A–F and JB–JF |
| vintage | **one**, `-2020` |
| components | `stator`, `rotor`, `housing`, `coolingSystem`, `gearBox` |
| materials | stop at `materialKeyLevel2` — `alloySteel`, `highCuAlloys2` |
| blank cells | **72 of 264 rows carry no `meanValue`** |
| values | absolute kg, not shares (`mass of component (kg) in product`) |

---

## Blocking 1 — the stator is counted twice, or the stator mass is not the stator

**24 of 24 filled cases. Exact to the last digit.**

The `statorSheetLaminationStack` material row holds precisely the value of the
stator `c-p` row — difference `0.0`, in every motor and every segment. The
stator *also* carries a `windings` row. So the stator's materials sum to
**1.2305×–1.2500×** the mass the same workbook gives for the stator.

An exact tie to fifteen digits is not a coincidence of measurement. One cell
was copied from the other.

Example, `PMElectricMotors`, segment C:

| row | kg |
|---|---|
| `c-p` stator | 31.669292 |
| `m-c` statorSheetLaminationStack | **31.669292** |
| `m-c` windings | 7.777347 |
| materials sum | 39.446640 → **1.246× the stator** |

**Two readings, and they are not equivalent:**

- **(a) The lamination cell was filled with the stator total.** The real
  lamination mass is `stator − windings`, and the motor is as heavy as stated.
  The material split is wrong; the mass is right.
- **(b) The `c-p` stator cell holds the lamination mass.** The real stator is
  `lamination + windings` and **every stator in the dataset is ~24% too
  light**. The split is right; the mass is wrong.

Under (a) nothing changes in total motor mass. Under (b) the stator — the
heaviest component in the machine — is understated across the entire fleet,
and with it every copper and electrical-steel total the model will produce.

**⚠️ NOT DECIDED. This is the one question that has to be answered before any
stage consumes the workbook,** because it cannot be resolved from inside the
data: both readings are internally consistent. It needs the Zenodo description
PDF, or a mass check against an admissible source per §2.1 — a stator of
31.7 kg versus 39.4 kg at 225–1100 Nm is a difference a cross-check can see.

## Blocking 2 — rare earth in the motor built to avoid it

**11 rows, all `EESMElectricMotors`, 7.53–10.88 kg each.**

The EESM rotor `windings` rows are labelled `rareEarthMetalsAndAlloys` under
`non-ferrousMetals`.

An externally excited synchronous machine excites its rotor with a **wound
field precisely so that it needs no magnet**. The winding is copper. Taken as
written, every EESM in the fleet carries ~10.9 kg of rare earth — which would
be the largest rare-earth term in the entire model, and is the exact opposite
of what the machine exists for.

The value is also **pinned at exactly 10.880000 across 8 of 11 segments**
(finding `repeated-across-segments`), which segments differing in size by more
than a factor of two should not be. A filled-down cell, not a measurement.

**Correction is unambiguous** — the material is copper — but the *mass* is not,
because the fill-down means 8 of the 11 numbers are one number.

## Blocking 3 — three components exist only as material rows

| component | rows | |
|---|---|---|
| `housing` | 26 | all `m-c`, **and all 26 name no material at all** |
| `gearBox` | 26 | all `m-c`, material `steelAndSteelAlloys` |
| `coolingSystem` | 26 | all `m-c`, material `AlAndAlAlloys`, **all blank** |

All three are components of the product recorded with `parameterCode` `m-c` —
a *material of a component*. None has a `c-p` row anywhere in the workbook.

A stage that walks the schema as written finds no component mass for any of
them and drops all three. Housing is worse than mislabelled: it is a mass
(~20.3 kg in PM/C) belonging to nothing.

The gearbox is **inside this project's boundary** (`METHODOLOGY.md` §1), so
this is not a cosmetic issue.

---

## Gaps — present, and empty

**72 blank `meanValue` cells.** A blank row is not an absent row: the workbook
asserts the component is there and declines to say how much.

| | rows | |
|---|---|---|
| `rotor` `c-p` | **26** | **every rotor mass in the workbook is blank**, in all three motors and all segments |
| `coolingSystem` / `coolingChannels` | **26** | every cooling mass blank — and §4.3 makes cooling architecture a scenario driver |
| `rotor` / `conductiveBars` | 4 | the induction motor's rotor cage, blank |
| remainder | 16 | scattered single segments, mostly `JE`/`JF` |

Rotor mass is **derivable** — its materials (lamination, shaft, magnets) are
populated — so this gap is closable by summing, *once blocking 1 establishes
whether a component `c-p` row in this workbook means the component or one of
its materials*.

Cooling is **not** derivable. Nothing in the workbook carries it.

**No element layer.** 0 `e-m` rows; materials stop at `alloySteel` and
`highCuAlloys2`. No element mass can be reported from this source at all —
which is why `data.composition_file` is blank and why §2.1 routes the element
layer to supplier datasheets and standards instead.

**One vintage,** `-2020`. Every year of a 2010–2070 trajectory is a modelling
decision and none of it is measured.

---

## What this means for the project

The workbook gives, reliably: **stator masses for 11 segments × 3 motors**, a
**material split per component**, and **magnet, shaft and lamination masses for
the rotor**. That is a real and useful tier-1 base.

It does **not** give: any rotor total, any cooling mass, any housing or gearbox
component mass, any element, or any year other than 2020 — and it contains one
systematic defect (blocking 1) that changes stator mass by 24% depending on
which way it is read.

**Nothing is corrected in code.** `src/source.py` reports; it does not patch.
Each correction is a decision with a source behind it and belongs here, applied
by the stage that builds the composition — not hidden in a loader.

---

## Decisions log

| date | decision |
|---|---|
| 2026-09-18 | The audit runs first and is kept as code, so a re-issued workbook is tested against the same list rather than against memory |
| 2026-09-18 | The audit reports and never corrects; corrections are decisions, recorded here |
| 2026-09-18 | Blocking 1 (stator counted twice) is **OPEN** — it cannot be resolved from inside the data and blocks every consuming stage |
