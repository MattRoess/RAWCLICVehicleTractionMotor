# Handover — RAWCLIC traction motor composition

**2026-09-18.** What this project is, what it stands on, what was corrected,
and what is still open.

---

## 1. What it does

Produces the **material composition of BEV traction motors** for the
stock-and-flow model: give it a **motor type, a torque, a voltage class and a
year**, get kilograms per vehicle by material.

```bash
./.venv/bin/python 01_composition.py
```

**One stage, one module.** `01_composition.py` reads, audits, verifies,
corrects and writes in one run. `src/composition.py` holds the benchmark, the
audit, the corrections, the draws and the figures. **Every setting is in
`src/params_schema.py`** — nothing takes a command-line argument.

### Where the files are, since 2026-09-21

`data/` has exactly three folders, the same three the battery project has, and
each says what is in it: **`raw/`** what this code opens, **`composition/`** what
it produces for itself, **`consolidated/`** the two files another repository
reads.

**And no orphans.** Four files from the vanished three-stage design
(`01_source_audit`, `02_stator_reading`, `03_corrected_composition`,
`03_corrections_log`, written by scripts deleted in `5663f95`) were removed on
2026-09-21. Data no stage writes any more does not get an archive folder.

**A file this code opens lives in `data/raw/`** — the Zenodo consolidated
workbook and the EV Database snapshot, and nothing else. `documentation/` holds
what a person reads and transcribes: the Drexler paper, the reports, the
critical review. Matthias's rule, and the reason the Drexler PDF stays a
document while the Zenodo workbook did not.

### What it writes, into `data/consolidated/`

The whole interface to the stock-and-flow model, and it holds nothing else.
`RAWCLICStockAndFlow` reads it **where it lies**, through
`params.materials.traction_composition_dir`, the same arrangement it already
had with `RAWCLICVehicleBattery/data/consolidated`. No copy is kept there:
traction motor information is in this project and nowhere else.

| file | |
|---|---|
| `TractionMotor_for_stockandflow.xlsx` | what `04_03_tractionmotors.py` reads, 13 299 rows |
| `TractionMotor_for_stockandflow.csv` | the same, for anything reading text |
| `draws/` | **the 200 000 simulations themselves**, 31 arrays, 298 MB |

### The draws, because a .csv is not a distribution

Matthias 2026-09-21. Every number reported here is a percentile of an array of
200 000 fitted values, and until now those arrays were built inside
`composition_by_torque` and thrown away. They are written now, as
`RAWCLICVehicleBattery` writes its own: `float32`, shape `(200 000, 12)`, one
per motor type, component and material.

| in `data/consolidated/draws/` | |
|---|---|
| `<motor>__<component>__<sub>__<material>__draws.npy` | the mass of every draw at every grid torque, **at base year and base voltage** |
| `torque_grid.txt` | the 12 columns of every array |
| `draw_scales.csv` | `scale` per motor, component, material, year and voltage class |
| `draws_manifest.csv` | what each array is, its shape, the seed and the draw count |

**Base year times a scale, not 39 copies.** The year factor is a closed-form
curve and the voltage factor is three constants, so any year and any voltage
class is `array * scale` — verified to 5.6 × 10⁻⁸ against 3 596 reported
percentiles, which is `float32` rounding. Writing all 13 × 3 combinations would
have been twelve gigabytes of the same numbers.

**And the two spec machines now draw.** Their interval was
`mean × (1 ± width)`, `width` the quadrature sum of the borrowed shape's
relative width and `spec_share_uncertainty` — the percentile arithmetic §5 says
never to do. Each draw now borrows that draw's own radial total, scaled through
the anchor by that draw's own value there, and multiplies by a drawn share
renormalised so the parts still sum to the machine the data sheet states. The
three radial types are unchanged to the last bit; the spec means move under
1 %, and the relative 95 % width goes from 0.548 to 0.503.

### And into `data/composition/`, for this project's own use

| file | |
|---|---|
| `TractionMotor_composition_by_torque.csv` | **the deliverable.** 14 508 rows, no segment dimension |
| `TractionMotor_composition_trajectory.csv` | same by segment, 13 338 rows |
| `TractionMotor_composition.xlsx` | current composition, 8 sheets, house schema |
| `composition_audit.csv` | every finding, before and after correction |

Plus seven figures in `figures/`.

### The deliverable's dimensions

| | |
|---|---|
| motor types | **5** — PMSM, EESM, IM+PM, axial flux, dual-rotor radial |
| voltage | 400 / 800 / 1000 V |
| torque | 100–1200 Nm, every 100 |
| years | 2010–2070, every 5 |
| materials | lamination, copper, magnet, steel, aluminium |

Every row carries `meanValue`, `p025`, `p975`, `yearBasis`, `n_segments`,
`extrapolated` and `slope_borrowed`.

---

## 2. The sources, and what each may do

`data.sources` in `params_schema.py` is the whole interface. **Adding a source
is a declaration, not a code change.** `role` is a gate enforced in code:
`load()` refuses a verification source.

| source | role | covers | what it gives |
|---|---|---|---|
| **Zenodo consolidated** | data, tier 1 | 2020 | 264 rows, house schema, the base |
| **Drexler et al. 2025** | data, tier 2 | 2018–2023 | 46 machines, component statistics |
| **EV Database** | data, tier 2 | 2011–2026 | 1438 models: power, torque, segment, drive |
| **YASA, Equipmake, DeepDrive, Donut Lab** | data, tier 2 | 2019–2025 | whole-machine mass and torque |
| Chalmers 2018, Munro 2020, GREET | **verification** | — | comparison only, never into the dataset |

### ⚠️ Two of them are not independent

**Zenodo is a torque regression through Drexler's points.** Its own description
says so. Agreement between them is arithmetic, not corroboration. And Zenodo's
torques come from the EV Database, so that is not an independent check of the
masses either — only of the ranges, being a later snapshot.

**Effectively this rests on 46 machines of model years 2018–2023.**

---

## 3. What was corrected, and why

Declared in `src/composition.py`, each with its evidence. **The source workbook
is never edited.**

| | correction | rows | evidence |
|---|---|---|---|
| **C1** | lamination := `stator − windings`, per draw | 24 | Drexler Fig. 11c: reading (b) puts 10 of 24 above the measured maximum |
| **C2** | EESM rotor winding: rare earth → **copper** | 11 | Drexler: "sliding brushes and **copper sleeves**" |
| **C3** | that winding's **mass**: kept, marked unreliable | 11 | measured 3.68 kg against 7.53–10.88 stated |
| **C4** | `c-p` rows for housing, gearBox, coolingSystem | 78 | consolidated description §3; Drexler §5.1.1 |
| **C5** | induction rotor cage: copper → **aluminium** | 4 | Drexler: **all eight** machines examined were aluminium |
| **C6** | torque ranges := fleet **p05–p95** | 342 | EV Database, 1438 models |

**39 blocking findings → 1.** Verified: 72 of 72 components sum exactly, and
rare earth appears only under `permanentMagnets`.

### The one blocking finding left

`zero-interval` — the 10 EESM rotor winding rows are the **only** 10 of 192
filled rows whose `p025` equals `p975`. Every other value is a regression with
a confidence interval; these were entered, not fitted. **Marking a defect is
not fixing it**, so the finding stays.

---

## 4. Findings that changed how the data is read

**The masses are per VEHICLE, not per motor.** Zenodo's stator lamination
equals Drexler's per-machine mean × the average motor count in that segment,
median ratio 1.08 over ten segments. What was first called a "1.5× sampling
difference", then "torque", is the motor count.

**The categories are drive configurations.** In a two-motor car one machine is
permanent-magnet and the second is induction, added for power and torque. The
magnets prove it: a two-motor car carries **less** magnet than the single-motor
category, almost exactly one rotor's worth (1.07, 0.86, 0.89 of a machine).
**A shift to all-wheel drive does not multiply magnet demand.**

**Torque was in the workbook from the start** — `torque_min`/`torque_max`,
columns 42 and 43, unused until late. Mass is a regression *on* torque, so
every figure plotting mass against the year showed segment size and hid the
model.

**The fleet's torque per motor is flat**, 3–6 % between 2020 and 2026 within a
segment. The assumption "same torque, less material" holds. A fleet-wide
median would have said the opposite — that is model mix.

**Above 1200 Nm the per-motor arithmetic breaks.** Median power per assumed
motor runs 150–242 kW below 1200 Nm and 348–460 kW above. Nobody builds a
430 kW traction machine: the Lucid Air Sapphire is three motors, the
Lightyear 0 is four in-wheel motors reporting wheel torque.

---

## 5. The assumptions, and where they live

**None of these is measured.** All are in `params_schema.py`, one line each.

| setting | value | what it assumes |
|---|---|---|
| `scenario.initial_rate` | 1 %/yr | ordinary refinement — **not** Drexler's −7.6 %/yr, which was a one-off hairpin transition |
| `scenario.floor` | 0.50–0.75 | how far each material can fall before physics stops it |
| `scenario.backcast_rate` | 0.4–1.5 %/yr | before 2020; the forward curve reversed explodes |
| `scenario.copper_mass` | 800 V = **2/3** | set by Matthias; 1000 V derived by power law |
| `monte_carlo.within_motor_correlation` | 0.9 | components of one motor share a torque shock |
| `run.spec_share_uncertainty` | 0.25 | on the derived splits of the two spec machines |
| `run.min_segments_for_slope` | 5 | below this, borrow the slope |

**All uncertainty comes from draws** — `monte_carlo.draws = 200 000`. Never
from adding or shifting intervals. The regression is refitted on every draw,
with the segments bootstrapped, so the band is the **fit's** uncertainty and
widens where fewer points hold the line.

| type | basis | uncertainty |
|---|---|---|
| PMSM | 11 segments | ±12 % |
| EESM | 10 segments | ±18 % |
| IM+PM | 3 segments, **slope borrowed** | ±12 % |
| axial flux | 1 data sheet | ±28 % |
| dual-rotor radial | 1 data sheet | ±28 % |

---

## 6. The two newer machines

They have **no published composition** — their makers give a whole-machine mass
and nothing about what is inside. The split is derived from the makers' own
published factors, in `run.spec_composition`, and **overwrite it if you have
better numbers**.

**Axial flux** (YASA): lamination × 0.20 (no stator yoke, YASA states up to
80 % less stator iron and gives 30 kg → 5 kg as its example), copper × 0.60,
magnet × 0.80. The housing is **measured**: P400 C 28.2 kg minus P400 R
24.0 kg = 4.2 kg, the same machine with and without. Adds to 28.2 kg exactly.

**Dual rotor** (DeepDrive): 80 % less iron, 50 % less magnet — but **no
baseline is named**, and there is no second variant to measure a housing
against. Weaker, and marked as such.

⚠️ **The dual rotor is anchored at 1500 Nm and the grid starts at 100**, so
almost its whole range is extrapolation below the one machine that exists.

---

## 7. Open

1. **`zero-interval` is still blocking** — C3's mass is marked, not fixed.
2. ~~**No element layer.**~~ **CLOSED FOR THE MAGNET, 2026-09-21.** Matthias's
   `10_MaterialElementDefinitions.xlsx` supplies 28 sintered NdFeB grades as
   min/max per element, and the magnet now carries `e-m` rows for Nd, Fe, B, Dy,
   Tb, Pr, Co, Al, Cu, Nb and Ga, drawn per draw and multiplied into the magnet
   mass draws. The grade class comes from `run.magnet_grade` — SH radial, H
   axial flux, on the oil-cooling argument of §4.3.

   **Still open for the other four materials.** The same workbook has
   `ElectricalSteel`, `Copper`, `CastAl` and `CastFeSteel`, so lamination,
   copper, aluminium and steel can have an element layer the same way. Only the
   magnet was asked for.

   **Praseodymium: settled 2026-09-21.** Matthias: Nd and Pr are didymium, and
   the workbook's 0.29–0.32 is the two together. So that column is drawn once as
   didymium and split, Pr taking 0.107–0.214 of it from the received reports' own
   element table, and the workbook's separate `Pr` column — an impurity limit of
   0–0.01 — is **not** added on top. Nd 0.256, Pr 0.0490 of magnet mass, against
   0.305 and 0.0050 before: praseodymium was understated tenfold while an
   impurity limit was being read as a constituent. Iron's reconciliation improved
   with it, 98.3 % → 99.5 % inside the cobalt-adjusted band.
3. **Rotor `c-p` blank in all 26 rows**; derivable by summing, but that is a
   decision. **Cooling mass blank in all 26** and not derivable from anything.
4. **Topology differences may be understated.** At 500 Nm the data puts the IM
   rotor 8 % above PMSM where Drexler measures 36 %. If real differences are
   flattened, a scenario moving away from magnets shows too little change.
5. **§4.2 and §4.3 are mechanisms without numbers** — magnet chemistry by
   operating temperature, cooling by heavy-REE access, Europe oil-cooled
   against China housing-water-cooled. Documented, not quantified.
6. **2 of 13 years are measured.** Everything else is `scenario.floor` and
   `scenario.initial_rate`.
7. **800 V carries only the saving.** Insulation, potting and insulated
   bearings grow with voltage and are not modelled, so 800 V looks better than
   it is by an unquantified amount.

---

## 8. If you change one thing

Test **`scenario.floor`** first. It is the single biggest lever on every 2070
number, it is not measured, and it is five lines.
