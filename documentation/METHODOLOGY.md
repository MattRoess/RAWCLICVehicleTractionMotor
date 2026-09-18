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
> **It is kept as a verification source** -- see §2.1. Nothing from it enters
> the dataset; it is used to check values established elsewhere.

Its **method** is still the right idea — scale a bill of material by torque
rather than quote one reference motor — and §2.2 below shows that the
current benchmark doing exactly that is already upstream of tier 1.

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
benchmark and GREET are **verification sources, not data sources**:

> **No number from any of the three enters the dataset. Not a mass, not a
> material split, not an element fraction. They are used to check values that
> were established from admissible sources, and for nothing else.**

This is stricter than composition-only, and deliberately so. A source that is
too old to supply a mass is also too old to be quietly holding up an `e-m` row
that nobody has checked against a primary source. The dataset has to stand on
its own sources; these three tell us whether it stands.

### What a verification source is for

1. An `m-c` or `e-m` value is established from an **admissible** source --
   supplier datasheet, standard, current open literature, or derivation with a
   stated method.
2. It is **then** compared against Chalmers, Munro 2020 or GREET.
3. Agreement is recorded as a check passed. Disagreement is recorded as a
   **flag**, and the flag is resolved against the admissible sources -- never
   by moving the value towards the old one.

The comparison has to be written down somewhere, or the check is not
reproducible and is therefore not a check. It belongs in **documentation, not
in the workbook** -- a verification table citing source, year and the two
values. Nothing in `data/` ever carries one of these numbers.

### Where the composition actually comes from, then

This costs nothing, because the primary sources are better anyway and are
already in hand:

| layer | admissible source |
|---|---|
| electrical steel `e-m` | **JFE and Nippon Steel** technical reports -- 3.0-4.5 wt% Si, 0.15-2.5 wt% Al |
| NdFeB `e-m` | magnet grade datasheets and the Nd2Fe14B stoichiometry; Dy/Tb by grade per §4.2 |
| copper, aluminium, insulation `e-m` | standards and supplier specification |
| rare earth per motor | **JRC** -- 1-3 kg NdPr, up to 200 g Dy |
| `c-p` masses | derived per §2.2, from current ratings and current architecture |

A mass or a composition that no admissible source supports stays missing and
gets derived with a stated method. A derived value is admissible; a borrowed
one is not, because a 2018 number silently fixes a 2018 design into a 2030 or
2060 row, and the whole time dimension of this model is the claim that the
design does not stay fixed.

### 2.2 The recent benchmark exists, and it is upstream of tier 1

**Corrected 2026-09-18.** This section previously recorded that no recent
public motor bill of material exists. That is wrong, and the answer was inside
the dataset the project already had.

The consolidated dataset's own description names its source:

> **Drexler, D., Kampker, A., Born, H., et al.** *Advances in electric motors:
> a review and benchmarking of product design and manufacturing technologies.*
> Elektrotech. Inftech. **142**, 312-345 (2025).
> doi:10.1007/s00502-025-01331-3

**Every mass in the consolidated dataset is a regression through Drexler's
benchmark points.** Not a second opinion on tier 1 -- the first one, at full
resolution. The description states the method plainly: component
weight-torque relationships fitted by linear regression, uncertainty taken
from the regression confidence interval, torques per car model from the EV
Database, Monte Carlo propagation, averaged per segment.

Two consequences:

1. **Tier 1 is current, not old.** The deliverable is dated **29.05.2026** and
   was reviewed by Valeo. The `-2020` in `productionYear` is the vintage the
   data *describes*, not the age of the source.
2. **Drexler at full resolution answers what the segment averages cannot** --
   per machine rather than per segment, and it is the only thing that can
   settle the blocking finding in `SOURCE_AUDIT.md`, which is unresolvable
   from inside the consolidated file because both readings are internally
   consistent.

**Still to obtain.** Springer requires authentication and MDPI returned 403 on
the automated fetch. Declared in the registry with a blank file, which is the
honest state: known, not yet in hand.

### 2.2.1 Adding a source is a declaration, not a code change

`data.sources` in `src/params_schema.py` is the whole interface. One entry per
source:

| field | |
|---|---|
| `file` | path, **blank = declared but not yet in hand** |
| `role` | `data` may supply values; `verification` may only be compared against |
| `tier` | `tier1` measured and in the house schema, `tier2` everything else |
| `vintage` / `published` | what the data describes, and when it was issued |
| `reads` | which reader understands the file |
| `citation` | what a figure caption must be able to say |

No stage names a file. Every stage asks the registry for the sources it is
entitled to, so a new bill of material reaches the whole project by being
declared.

**`role` is a gate in code, not a label.** `src/source.py:load()` raises
`PermissionError` on a verification source, and `load_verification()` refuses a
data source. §2.1 is enforced rather than remembered, because a rule that lives
only in prose is a rule that gets broken by whoever is in a hurry.

Every row a reader returns is stamped with `sourceName` and `sourceTier`, so a
frame that has travelled two function calls can still say where it came from.

**Adding Drexler when the file arrives:** set its `file`, write a `bom` reader
against the actual document. Nothing else changes.

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

These carry numbers and cost nothing. The status column says which are
**admissible** -- may supply dataset values -- and which are **verification
only** per §2.1.

| source | what it gives | status |
|---|---|---|
| **R&D GREET**, Argonne | vehicle material composition by component, traction motor included, free, updated annually | **verification only, §2.1.** Still worth pulling — it is the broadest free cross-check that exists — but no GREET number enters the dataset |
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

### 4.0 Two years are measured. Eleven are constructed.

**Decided 2026-09-18: the Zenodo dataset is a historic anchor, not a basis for
the forward look.**

It is a good dataset and it is current as a publication -- but it describes the
**2020** fleet: 400 V, round-wire stators, magnets sized before heavy-rare-earth
reduction became a design driver. Read forward it would assert that none of
that changes, which is precisely the thing this project exists to deny. It
anchors history and supplies no year after 2020.

Every source carries a `covers` window in the registry, and it is the years the
source's numbers legitimately describe -- not when it was written. Zenodo has
**one vintage**, so its window is one year. So does Drexler 2025, until the
file is in hand and shows otherwise.

At `run.years = '2010-2070, 5'` that gives:

| | |
|---|---|
| **measured** | **2020** (Zenodo), **2025** (Drexler) |
| **constructed** | 2010, 2015, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070 |

**Two of thirteen.** Printed on every run of `00_parameters.py`, because it is
the most consequential fact about this project and the easiest one to forget
once the figures look convincing.

Note that **2010 and 2015 are constructed too.** They are a backcast, not a
reading: no source here describes the 2010 fleet. "Historic" does not mean
"measured", and the registry refuses to pretend otherwise.

**`horizon` is `historic` for every source, and only `historic` is accepted.**
No source describes the future. Every year past 2025 is built by §4.1-§4.4 on
stated mechanisms -- efficiency improvement, magnet chemistry, cooling
architecture, voltage class -- and each one has to be defensible on its
mechanism rather than on a measurement it does not have.

`data.measured_until` and `data.year_is_measured(year)` exist so a stage asks
instead of assuming, and so that moving the boundary is a registry edit rather
than a number buried in code.

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
| 2026-09-18 | Chalmers, Munro 2020 and GREET are **verification sources, not data sources** — no number from any of them enters the dataset, at any layer |
| 2026-09-18 | Verification comparisons are written in documentation, never in `data/`; a disagreement is resolved against the admissible sources, never towards the old one |
| 2026-09-18 | Composition comes from supplier datasheets and standards; a value no admissible source supports is derived with a stated method, not borrowed |
| 2026-09-18 | ~~No recent public motor-only BOM exists~~ **CORRECTED**: Drexler et al. 2025 is the recent benchmark, and it is the upstream of the tier-1 dataset |
| 2026-09-18 | Tier 1 is CURRENT — deliverable dated 29.05.2026, reviewed by Valeo; `-2020` is the vintage described, not the age |
| 2026-09-18 | Sources live in one registry, `data.sources`; adding a source is a declaration, and `role` is enforced in code |
| 2026-09-18 | Munro REJECTED — the videos do not weigh parts, the written benchmark is 2020 and paid |
| 2026-09-18 | Free and current sources only: GREET first, then JRC, IEA, steel-supplier datasheets and OEM statements |
| 2026-09-18 | Five motors: three from the dataset, axial flux and dual-rotor radial added as tier 2 |
| 2026-09-18 | DeepDrive is dual-rotor **radial** flux, checked against the company's own description |
| 2026-09-18 | Gearbox is inside the boundary; power electronics is not |
| 2026-09-18 | 400 V, 800 V and 1000 V described separately, because voltage decides copper |
| 2026-09-18 | Years 2010–2070 built from a steady, modest material-efficiency improvement |
| 2026-09-18 | **Zenodo is a historic anchor, not the forward basis** — it describes the 2020 fleet, and read forward it would deny the change this project models |
| 2026-09-18 | Each source carries a `covers` window; one vintage means one year. 2 of 13 modelled years are measured, and 2010/2015 are a backcast, not a reading |
| 2026-09-18 | Magnet Dy/Tb content follows permissible magnet temperature, which follows cooling architecture, which follows heavy-REE access — Europe oil-cooled, China housing-water-cooled |
