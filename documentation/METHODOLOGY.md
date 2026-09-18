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
> **Its masses are not used. Nine years old.** They predate 800 V in volume,
> hairpin winding at scale, heavy-rare-earth reduction as a design driver, and
> both new architectures here. Recorded so that they are not proposed again.
>
> **Its material compositions are admissible** -- see §2.1. Composition-only,
> at matched architecture.

Its **method** is still the right idea — scale a bill of material by torque
rather than quote one reference motor — and §2.2 below takes that idea without
taking its numbers.

### 2.1 Age applies to the weights, not to the composition

**A source's age has to be judged per layer, because the three layers of the
schema age at completely different rates.**

| layer | what it says | does it age |
|---|---|---|
| `c-p` component of product | how many kg of stator, rotor, housing, gearbox in a motor | **yes, fast.** This is the whole point of 2010-2070: same torque, less material. A 2018 mass is a 2018 design |
| `m-c` material of component | how the stator splits into electrical steel, copper, insulation, potting | **slowly.** It moves when the architecture moves -- hairpin winding, oil cooling, a magnet-free rotor -- and those are architecture changes the scenarios already carry explicitly |
| `e-m` element of material | what NdFeB, electrical steel or winding copper IS, element by element | **essentially not at all.** Chemistry is chemistry. Nd2Fe14B has the stoichiometry it has. Non-oriented electrical steel is 3.0-4.5 wt% Si because of core loss physics, not because of the model year |

So the rule is:

> **Recency is required for `c-p`. Older sources remain admissible for `m-c`
> and `e-m`, provided the architecture they describe is the architecture being
> described.**

That last clause is the guard. A 2018 round-wire stator is a valid source for
what copper and lamination steel are, and **not** a valid source for the
material split of a 2030 hairpin stator, because the winding technology
changed underneath it.

**Settled 2026-09-18.** The 2017/2018 Chalmers inventory, the 2020 Munro
benchmark and GREET are **composition-only sources**:

> **Use them for `m-c` and `e-m`. Never for `c-p`.**

Not a preference to weigh against other considerations -- a hard gate. No mass,
no kg, no "motor weighs", no component total may be taken from any of the
three, in any scenario, at any year, however convenient the gap it would fill.
What may be taken is what a material is made of, cited by source and year.

If a mass is missing and one of these three is the only place it appears, that
mass stays missing and gets **derived** per §2.2 instead. A derived mass with a
stated method is admissible; a borrowed 2018 mass is not, because it silently
fixes a 2018 design into a 2030 or 2060 row and the whole time dimension of
this model is the claim that the design does not stay fixed.

### 2.2 Recent bills of material do not exist in public, and that is the finding

Searched 2026-09-18. **No recent, complete, motor-only bill of material at a
matched rating is published for any of the five motors.** This is the same gap
the critical review identified, and nothing since has closed it.

Where the current numbers actually are:

| | holds it | usable |
|---|---|---|
| **Munro Live** (YouTube) | **current teardowns, free** — see 2.3 | **yes**, and it is the best recent source found |
| **A2MAC1**; Munro's written reports | current teardowns, component by component | commercial. Munro's 10-motor comparison is **2020** and paid — **composition only**, never masses, §2.1 |
| **IDTechEx** | architecture shares and trends | commercial; already cited by the review |
| **ORNL / DOE VTO** | public teardowns, real weighed parts | the motor teardowns are older; recent work is inverters and drive units |
| **OEM technical papers** | one machine each, well documented | scattered, and rarely a full BOM |
| **Steel and magnet suppliers** | what the material IS | **public and current** — JFE and Nippon Steel give non-oriented electrical steel as 3.0–4.5 wt% Si, 0.15–2.5 wt% Al |

### 2.3 Munro Live: rejected 2026-09-18

Munro & Associates publish current teardowns on YouTube -- YASA YM360 axial
flux in May 2026, BYD iDM-210 in March 2026, the magnet-free Nissan Ariya in
August 2025. Current, free, and covering machines nothing else covers.

**They do not weigh the parts.** The videos are engineering commentary on
design, cooling and material choice, not a bill of material, and no component
masses can be taken from them. Their written 10-motor benchmark does carry
weights, and it is **2020 and paid** -- old by the same test that rejected
Chalmers.

Recorded so that neither is proposed again. What the videos are still good for
is qualitative: which machine is oil-cooled, which uses hairpin winding, which
has no magnets.

### 2.4 What is freely available and current

These carry numbers, cost nothing, and are current enough to use. In the order
worth pulling:

| source | what it gives | status |
|---|---|---|
| **R&D GREET**, Argonne | **vehicle material composition by component**, traction motor included, free download, updated annually | **pull first.** The vehicle-material-composition module is the closest thing to a free BOM that exists |
| **JRC**, *The role of rare earth elements in wind energy and electric mobility* and the 2024-25 CRM reports | rare earth per motor; already cited by the critical review, so already vetted | free PDFs |
| **IEA**, critical minerals and rare earth reports | demand and intensity, already vetted by the review | free |
| **JFE Steel**, **Nippon Steel** technical reports | what non-oriented electrical steel IS: **3.0-4.5 wt% Si, 0.15-2.5 wt% Al** | free PDFs, current |
| **OEM and supplier statements** | rating, mass, voltage class, cooling, per machine. **Valeo sells a high-voltage rare-earth-magnet-free motor**; Renault-Valeo E7A; BMW Gen5/Gen6 | free, and the only current per-machine data |
| **MDPI Machines 2025**, *Electric Vehicle Motors Free of Rare-Earth Elements* | the architecture landscape without NdFeB | open access |

### 2.5 Figures already in hand from those sources

| | |
|---|---|
| NdPr alloy per EV traction motor | **1-3 kg** |
| dysprosium per EV traction motor | **up to 200 g** |
| share of EVs using NdFeB permanent-magnet motors | **over 90%** |
| rare earth demand tied to EV motors | **37 kt in 2024, 43 kt expected 2025** |
| non-oriented electrical steel | **3.0-4.5 wt% Si, 0.15-2.5 wt% Al** |
| hairpin winding, slot copper density | **46% -> 60%** against round wire |

Those are element-level numbers for the magnet and the steel -- the layer the
consolidated dataset does not have -- and they are current. They are not yet a
bill of material, because none of them says how much lamination stack or how
much copper a given machine carries.

**Beyond these, derive rather than find.**### What tier 2 is not allowed to be

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
| 2026-09-18 | **Age is judged per layer**: `c-p` masses must be recent, `m-c` and `e-m` compositions do not expire |
| 2026-09-18 | Chalmers, Munro 2020 and GREET are **composition-only sources** — `m-c` and `e-m` yes, `c-p` never. A missing mass is derived, not borrowed |
| 2026-09-18 | No recent public motor-only BOM exists in writing; bills of material are DERIVED from current ratings and current material shares |
| 2026-09-18 | Munro REJECTED — the videos do not weigh parts, the written benchmark is 2020 and paid |
| 2026-09-18 | Free and current sources only: GREET first, then JRC, IEA, steel-supplier datasheets and OEM statements |
| 2026-09-18 | Five motors: three from the dataset, axial flux and dual-rotor radial added as tier 2 |
| 2026-09-18 | DeepDrive is dual-rotor **radial** flux, checked against the company's own description |
| 2026-09-18 | Gearbox is inside the boundary; power electronics is not |
| 2026-09-18 | 400 V, 800 V and 1000 V described separately, because voltage decides copper |
| 2026-09-18 | Years 2010–2070 built from a steady, modest material-efficiency improvement |
| 2026-09-18 | Magnet Dy/Tb content follows permissible magnet temperature, which follows cooling architecture, which follows heavy-REE access — Europe oil-cooled, China housing-water-cooled |
