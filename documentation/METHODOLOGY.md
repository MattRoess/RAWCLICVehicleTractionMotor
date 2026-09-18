# Methodology

What this project describes, where each number is allowed to come from, and
which choices are modelling decisions rather than readings of data.

Written 2026-09-18. `HANDOVER.md` says what state the work is in; this says why
it is built the way it is. Settings live in `src/params_schema.py` and are
documented in place.

---

## 1. What is described, and the boundary

A BEV traction motor, as **components → materials → elements of materials**,
for the years the stock-and-flow model needs, so that a fleet can be multiplied
by a composition.

### What is inside the boundary

| | in | why |
|---|---|---|
| stator, rotor, housing, cooling system | ✅ | the motor |
| **gear box** | ✅ | **decided 2026-09-18.** It is in `componentKeyLevel2` of the consolidated dataset, and a traction motor is bought, fitted and scrapped as a drive unit |
| **power electronics / inverter** | ❌ | **decided 2026-09-18.** It belongs to `RAWCLICVehicleElectronics`. Counting it here would double-count it against that project |

⚠️ **THE GEARBOX DECISION IS NOT FREE.** The critical review names e-axle
boundaries as a principal reason published motor masses disagree by tens of
kilograms — some figures are motor-only, some are motor plus inverter plus
gearbox. Every mass this project reports must therefore say that the gearbox is
in and the inverter is out, or it cannot be compared with anything published.

### The voltage dimension

**400 V, 800 V and 1000 V are described separately.** Decided 2026-09-18.

Raising the DC-link voltage lowers the current for the same power, and the
conductor cross-section follows the current. **A higher-voltage machine needs
less copper for the same torque**, which is a material effect and therefore
this project's business, not the inverter's. 800 V is in production; 1000 V is
the direction of travel.

This is a dimension of the composition, not a separate motor: the same
architecture at two voltages is two compositions.

## 2. Sources, and the tier each one buys

### Tier 1 — the consolidated dataset

`documentation/TractionMotor/Zenodo/RAWCLIC_BEV_motor_consolidated_data_V1.xlsx`,
264 rows in the RAWCLIC 43-column house schema, with `dataProcessor`, `DOI` and
the four DQ columns.

It is the only **measured** source, and it has two limits that shape everything:

* **No elements.** `materialKeyLevel3` and `materialKeyLevel4` are empty; there
  is no `e-m` row. Materials stop at `alloySteel` and `highCuAlloys2`.
* **One vintage.** `productionYear` holds the single value `-2020`. It is a
  photograph of the fleet as it was, not a trajectory.

⚠️ **AND IT IS ONE RELATIVELY OLD PUBLICATION.** It does not reflect current
trends — 800 V, heavy-rare-earth reduction, dual-rotor machines and axial flux
all postdate it. Treating it as the whole truth would freeze the model at 2020.
That is why tier 2 exists.

### Tier 2 — everything else, and it must be named

Any other bill of material: literature, LCI studies, teardowns, OEM statements.
**A tier-2 number is usable and must be labelled.** `run.motors` records the
tier per motor precisely so that no figure can draw a tier-1 and a tier-2
number in the same colour without saying so.

The best tier-2 source found so far, and the one that answers the review's
central complaint:

> **REJECTED 2026-09-18.** *Nordelöf et al., A scalable life cycle inventory
> of an electrical automotive traction machine*, Int J LCA, Part I **2017**,
> Part II **2018**. 20 materials per motor, computed rather than tabulated,
> scaling over 20–200 kW and 48–477 Nm, validated to within 21%.
>
> **Not used. Nine years old.** It predates 800 V in volume, hairpin winding at
> scale, heavy-rare-earth reduction as a design driver, and both new
> architectures here. Recorded so that it is not proposed again.

Its **method** is still the right idea — scale a bill of material by torque
rather than quote one reference motor — and §2.1 below takes that idea without
taking its numbers.

### 2.1 Recent bills of material do not exist in public, and that is the finding

Searched 2026-09-18. **No recent, complete, motor-only bill of material at a
matched rating is published for any of the five motors.** This is the same gap
the critical review identified, and nothing since has closed it.

Where the current numbers actually are:

| | holds it | usable |
|---|---|---|
| **Munro Live** (YouTube) | **current teardowns, free** — see 2.2 | **yes**, and it is the best recent source found |
| **A2MAC1**; Munro's written reports | current teardowns, component by component | commercial. Munro's 10-motor comparison is **2020** and paid — old by the same test that rejected Chalmers |
| **IDTechEx** | architecture shares and trends | commercial; already cited by the review |
| **ORNL / DOE VTO** | public teardowns, real weighed parts | the motor teardowns are older; recent work is inverters and drive units |
| **OEM technical papers** | one machine each, well documented | scattered, and rarely a full BOM |
| **Steel and magnet suppliers** | what the material IS | **public and current** — JFE and Nippon Steel give non-oriented electrical steel as 3.0–4.5 wt% Si, 0.15–2.5 wt% Al |

### 2.2 Munro Live is the recent source, and it is on video

Munro & Associates publish teardowns on YouTube as they do them. They are
current, free, and they cover the machines this project needs — including two
of the five motors:

| teardown | when | why it matters here |
|---|---|---|
| **YASA YM360 axial flux** | May 2026 | architecture, rotor and stator design, **cooling strategy**, material selection, against radial flux |
| **BYD iDM-210 drive unit** | March 2026 | a Chinese drive unit — the other side of the §4.3 geography |
| **Nissan Ariya magnet-free motor** | August 2025 | a production machine with no magnets at all |
| VW ID.4 | | hairpin winding raises slot copper density **46% → 60%** |
| Tesla Model S Plaid | | carbon-wrapped rotor, isolated pole cap |

⚠️ **THE NUMBERS ARE SPOKEN AND ON SCREEN, NOT IN A TABLE.** A teardown video
states a weight as it is weighed. Getting those into this project is manual
watching and note-taking; it cannot be fetched. Each figure taken from a video
must be recorded with the video, the date and the timestamp, or it is an
unsourced number with a story attached.

**Beyond the videos, derive rather than find.** Two things ARE public and
current, and together they give a bill of material without any old inventory:

1. **Motor ratings and masses**, per machine, from OEM and supplier statements
   — BMW Gen5/Gen6, Renault–Valeo E7A, YASA P400, DeepDrive, Nissan's
   magnet-free machine. Power, torque, mass, voltage class, cooling.
2. **Material shares within a component**, from suppliers and the consolidated
   dataset — what a lamination stack, a winding or a magnet is made of.

A mass from (1) split by shares from (2) is a current bill of material whose
every part is traceable and dated. That is the method the rejected paper
demonstrated; only its numbers were stale.

⚠️ **AND IT NEEDS A BUDGET DECISION.** If this project can buy an A2MAC1 or
Munro subscription, the derivation becomes a cross-check instead of the primary
route. That is a question about money, not about method, and it is open.

### What tier 2 is not allowed to be

The report workbook of 2026-09-18 states component masses at **60% source
reliability**, and the critical review of the same day marks as unconfirmed the
motor mass, the stator and rotor laminations, the stator copper, the shaft, the
housing, the bearings, the cooling hardware, the sensors, and **every**
architecture share for 2030, 2035, 2040 and 2050.

What the review does confirm is qualitative and is safe to build on:

* NdFeB carries **Nd and Pr**, with **Dy or Tb** where coercivity is needed
* Nd is about **29–32% of magnet mass**
* magnet mass falls in a broad **0.5–3.0 kg** traction range
* YASA P400 is **160 kW at 24–28.2 kg**
* the EU strategic-material recycling benchmark is **25% by 2030**

## 3. The five motors, and one correction

| motor | tier | note |
|---|---|---|
| `PMElectricMotors` | zenodo | 110 rows |
| `EESMElectricMotors` | zenodo | 110 rows |
| `IMandPMElectricMotors` | zenodo | 44 rows |
| `axialFluxPMElectricMotors` | report | not in the dataset; not yet in the fleet |
| `dualRotorRadialPMElectricMotors` | report | DeepDrive |

SynRM, PMa-SynRM and in-wheel are absent: demonstrators in both sources, with
no bill of material in either.

### DeepDrive is radial, not axial — checked at the source

The report workbook's `Axial Flux` sheet calls it *"Double-rotor axial flux"*.
**DeepDrive's own technology page calls it a "Dual Rotor, radial flux
machine"**, with the stator between an inner and an outer rotor. The critical
review reached the same conclusion independently. The name here follows the
source.

**This is not a labelling quibble.** An axial-flux stator core is soft magnetic
composite or amorphous iron, because the flux path is three-dimensional; a
radial one is silicon-steel lamination stack. The topology decides the
material, so a wrong name puts the wrong material in the bill.

DeepDrive's own claims, to be carried as claims: **50% less magnet material,
80% less iron, and heavy-rare-earth-free magnets.**

## 4. The time dimension, 2010–2070

**Nothing in either source gives a trajectory.** The dataset has one vintage and
every architecture share in the reports is unconfirmed. So the span is built
from stated rules, and each rule is a decision with a name.

### 4.1 Steady efficiency improvement

**Decided 2026-09-18.** The same power and the same torque are delivered with
**less material**, improving **steadily and modestly** over time — not a step
change, not a plateau.

This is the mechanism behind every year that is not 2020. It says a 2050 motor
of a given rating is lighter in its active materials than a 2020 one of the
same rating, and it must be a single stated rate rather than a different
assumption per material.

⚠️ Not yet quantified. The rate is the first number this project has to choose
and defend.

### 4.2 Magnet chemistry follows the operating temperature

**Decided 2026-09-18, and it is the distinctive claim in this project.**

The heavy rare earths — **dysprosium and terbium** — buy coercivity, and
coercivity is what lets a magnet run hot without losing its magnetisation
irreversibly. **How hot the magnet is allowed to get therefore decides how much
Dy and Tb the magnet contains.** The magnet's composition is not a free
parameter; it is set by the thermal design.

### 4.3 Cooling architecture follows heavy-rare-earth access — and that is geographic

And the thermal design is set by what the manufacturer can buy:

| | heavy REE | magnet | cooling | material consequence |
|---|---|---|---|---|
| **Europe** | constrained | little or no Dy/Tb, so lower permissible magnet temperature | **the whole machine in oil** — direct rotor and winding contact | more cooling hardware, oil, seals and pumping |
| **China** | available | Dy/Tb present, so a higher permissible magnet temperature | **water on the outside of the housing only** | far less cooling hardware |

So the same nominal motor carries a **different bill of material depending on
where it was built**, and the difference runs in two directions at once: Europe
spends cooling hardware to save heavy rare earth, China spends heavy rare earth
to save cooling hardware.

**This has to be reflected in the composition**, not mentioned in a note. A
model that applies one magnet chemistry and one cooling mass to all motors
describes neither fleet.

> Supporting, from DeepDrive's own page: **heavy-rare-earth-free magnets** are
> being marketed as a design feature. That is the European constraint turned
> into a product claim, and it is evidence the axis is real.

### 4.4 What the literature already gives for §4.2

Enough to anchor the magnet end of the mechanism, not yet the cooling end:

| | |
|---|---|
| Nd(Dy)FeB composition | **22–32% Nd, up to 10% Dy, 67–70% Fe, ~1% B** |
| a ~4% Dy grade | rated to operate at **140 °C** |
| Nd **and** Dy additions | enable **150 °C continuous** operation |
| the review, independently | Nd is **29–32%** of magnet mass; Dy and Tb are "grade- and process-dependent" |

So the direction and the rough magnitude of **Dy against permissible
temperature** are documented: single-digit percent of Dy buys roughly
140–150 °C continuous. And the reason to avoid it is documented too — Dy is the
most expensive and rarest constituent, and demand for it is the most exposed of
any magnet element absent recycling.

⚠️ **THE COOLING END IS STILL UNSOURCED.** What is not in hand is the second
half: how many kilograms of oil, channel, seal and pump a fully oil-cooled
machine carries against a housing-water-cooled one of the same rating. Without
that, §4.3 has a mechanism and no masses, and it stays a described mechanism
rather than a modelled one.

⚠️ **AND ONE TERM NEEDS CONFIRMING.** "Inversion temperature" was the phrase
used when this was decided. Written here as the temperature above which the
magnet loses magnetisation irreversibly — the working-point limit that Dy and
Tb raise. If a different quantity was meant, this section changes.

## 5. What is still needed

1. **The element workbook.** Nothing here can produce an element layer until it
   exists. `data.composition_file` is blank and stages must refuse rather than
   invent one.
2. **More bills of material**, to escape a single 2020 publication. The Chalmers
   LCI is the first; EESM, axial flux and the dual-rotor machine each need one.
3. **The efficiency rate**, §4.1 — one number, defended.
4. **The cooling-hardware masses**, §4.3 — the magnet end of the mechanism is
   anchored, §4.4; the oil-versus-water-jacket mass difference is not.
5. **Recent bills of material from outside the journals**, §2 — supplier
   statements, teardowns and standards, because published inventories are
   structurally several years late.
6. **Voltage-class copper factors**, §1 — how much copper 800 V and 1000 V save
   against 400 V for the same torque.

## Decisions log

| date | decision |
|---|---|
| 2026-09-18 | Zenodo is tier 1 and the only measured source; everything else is tier 2 and labelled |
| 2026-09-18 | The 2017/2018 Chalmers inventory is REJECTED as too old — its method is kept, its numbers are not |
| 2026-09-18 | No recent public motor-only BOM exists in writing; bills of material are DERIVED from current ratings and current material shares |
| 2026-09-18 | Munro Live's video teardowns are the recent source — free and current, extracted by hand, each figure cited to video, date and timestamp |
| 2026-09-18 | Five motors: three from the dataset, axial flux and dual-rotor radial added as tier 2 |
| 2026-09-18 | DeepDrive is dual-rotor **radial** flux, checked against the company's own description |
| 2026-09-18 | Gearbox is inside the boundary; power electronics is not |
| 2026-09-18 | 400 V, 800 V and 1000 V described separately, because voltage decides copper |
| 2026-09-18 | Years 2010–2070 built from a steady, modest material-efficiency improvement |
| 2026-09-18 | Magnet Dy/Tb content follows permissible magnet temperature, which follows cooling architecture, which follows heavy-REE access — Europe oil-cooled, China housing-water-cooled |
