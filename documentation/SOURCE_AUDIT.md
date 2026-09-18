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

### ✅ RESOLVED 2026-09-18 — reading (a), by `02_verify_stator.py`

Settled against **Drexler et al. (2025)**, which is not a second opinion but
the same data before it was fitted: every consolidated mass is a regression
through Drexler's benchmark points. Its stator lamination stacks are measured
on **46 machines, 7.20–35.52 kg, mean 16.62 kg** (Fig. 11c).

| reading | implied lamination | outside the measured range |
|---|---|---|
| **(a)** `c-p` is the stator | 10.75–39.54 kg, mean 25.11 | **1 of 24** |
| (b) `c-p` is the lamination | 13.97–52.72 kg, mean 33.31 | **10 of 24** |

Reading (b) would have the regression producing ten values its own source
never contained, up to 52.72 kg against a measured maximum of 35.52 kg.

> **The `c-p` row is the stator.** The lamination cell was filled with the
> stator total, and the true lamination is `stator − windings`.
> **Total motor mass is unaffected; the material split is wrong.**

**The remaining offset is sampling, not a second defect.** Consolidated
segment averages run heavier than Drexler's motor averages — **1.51×** for the
stator lamination and **1.50×** for the rotor lamination. Two independent
components giving the same ratio is what a sampling difference looks like:
segments including large vans, against 48 individual motors including small
ones. A further defect would not land on both at the same factor.

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

**The audit never corrects.** `src/source.py` reports. Corrections are declared
in `src/corrections.py`, each with the evidence that establishes it, and applied
by `03_apply_corrections.py`.

**The source workbook is never edited.** It is a received deliverable under
`documentation/`. The corrected dataset is written to `data/`, where it is
plainly a product of this project and cannot be mistaken for what was handed
over.

---

## Corrections applied 2026-09-18

| | correction | rows | evidence |
|---|---|---|---|
| **C1** | lamination := `stator − windings`, **per draw** | 24 | `02_verify_stator.py` vs Drexler Fig. 11c |
| **C2** | EESM rotor winding: rare earth → **copper** | 11 | Drexler: "sliding brushes and **copper sleeves**", 9 EESM rotors |
| **C3** | EESM rotor winding **mass** | 0 | **NOT APPLIED — flagged** |
| **C4** | `c-p` rows added for housing, gearBox, coolingSystem; housing material → aluminium | 78 | Consolidated description §3; Drexler §5.1.1 "cast aluminium" |
| **C5** | induction rotor cage: copper → **aluminium** | 4 | Drexler: "**all eight** motors examined were made of aluminum", avg 2.26 kg |

**Result: 53 findings → 18. Blocking: 38 → 0.**

Verified rather than asserted — after correction, **72 of 72** components have
materials summing to the component mass with a maximum deviation of `0`, and
rare earth appears only under `permanentMagnets`.

### C1's uncertainty is drawn, not shifted

The first version of C1 moved `p025`/`p975` by the same amount as the mean.
**That is interval arithmetic in disguise** — it keeps the stator's own width
for a quantity that is a *difference of two uncertain masses*. Corrected to
Monte Carlo: the difference is taken per draw and the percentiles are of the
result, 200,000 draws, `src/draws.py`.

The two masses are **correlated** — both are regressions on the same vehicle's
torque, so a motor larger than the fit expects is larger in both, and the
errors largely cancel. `monte_carlo.within_motor_correlation` carries that
assumption. **It is not measured**; the dataset gives no covariance.

It matters, and here is by how much (PM, segment C):

| ρ | p025 | p975 | width |
|---|---|---|---|
| 0.00 | 23.3733 | 24.4104 | 1.0371 |
| 0.50 | 23.4769 | 24.3070 | 0.8301 |
| **0.90** | **23.5843** | **24.1990** | **0.6147** |
| 1.00 | 23.6174 | 24.1658 | 0.5484 |
| *(old shift)* | *23.4216* | *24.3737* | *0.9520* |

**The shifted interval was 1.55× too wide.** Between ρ=0 and ρ=1 the width
varies by a factor of 1.9, so the assumption is worth arguing with — and it is
one line in `src/params_schema.py`.

### C3 is deliberately not applied

Drexler measures total rotor copper at **3.68 kg** (max 4.45, min 2.86, Fig.
30b). The consolidated rows carry **7.53–10.88 kg** — two to three times the
measured maximum — and the value is pinned at exactly `10.880000` across 8 of
11 segments, which is a filled-down cell.

So the mass is almost certainly wrong as well. It is **still not corrected**,
because replacing a segment-resolved series with one benchmark average is a
modelling decision rather than a correction, and the **1.5× segment-to-motor
offset** established in `02_verify_stator.py` means the two are not directly
comparable. `applied=False` is a real state in `src/corrections.py`: reported,
carried in the output, changing nothing until somebody decides.

**⚠️ This is the one open item. It needs a decision.**

### What C5 also revealed

The audit found `conductiveBars` as a *blank*. Drexler shows it is also the
*wrong material*: the induction machine's short-circuit cage is aluminium, not
copper, in all eight machines examined. A gap and a defect in the same rows —
which is why the correction layer and the benchmark had to meet.

### Still open after correction

- **Rotor `c-p` is blank in all 26 rows.** Derivable by summing its materials,
  but that is a decision, not a correction — the workbook declines to state it.
- **Cooling mass is blank in all 26 rows** and is not derivable from anything
  in the registry. §4.3 makes cooling architecture a scenario driver.
- **No element layer**, and one vintage.

---

## Decisions log

| date | decision |
|---|---|
| 2026-09-18 | The audit runs first and is kept as code, so a re-issued workbook is tested against the same list rather than against memory |
| 2026-09-18 | The audit reports and never corrects; corrections are decisions, recorded here |
| 2026-09-18 | C1, C2, C4, C5 applied — 38 blocking findings to 0, verified by 72/72 components summing exactly |
| 2026-09-18 | **All derived uncertainty comes from draws**, never from shifting or adding intervals — `src/draws.py`, 200,000 draws |
| 2026-09-18 | Within-motor correlation assumed **0.9** and NOT measured; width varies 1.9× between ρ=0 and ρ=1 |
| 2026-09-18 | Drexler is data, not ground truth — its min/max are sample extremes of 46 machines, used as a range check and never as a limit |
| 2026-09-18 | The source workbook is never edited; corrections are declared in code and written to `data/` |
| 2026-09-18 | **C3 (EESM rotor winding mass) NOT applied and OPEN** — measured 3.68 kg against 7.53–10.88 kg stated, but substituting a benchmark average is a modelling decision |
| 2026-09-18 | Blocking 1 **RESOLVED** against Drexler 2025: the `c-p` row is the stator; the lamination cell holds the stator total. Motor mass unaffected, material split wrong |
| 2026-09-18 | The 1.5x offset between segment averages and motor averages is sampling, not a defect — the same ratio appears on stator and rotor independently |
