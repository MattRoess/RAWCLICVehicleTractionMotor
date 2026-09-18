# Handover

Current as of **2026-09-18**, the day the project got its parameters. Newest
entries go at the foot.

**Read `src/params_schema.py` first.** Every setting is there, it explains each
one in place, and no stage takes a command-line argument.

---

## What this project is

What BEV traction motors are made of -- components, the materials those
components are made of, and the elements in those materials -- for the years
`RAWCLICStockAndFlow/code/04_03_tractionmotors.py` needs, so a fleet can be
multiplied by a composition.

It is the traction-motor counterpart to `RAWCLICVehicleBattery`,
`RAWCLICVehicleComposition` and `RAWCLICVehicleElectronics`.

⚠️ **Motors already reach the recovery model by another route.** The electronics
case carries `Motors` as a copper stream through `element_draws`. Whether this
project replaces that or sits beside it is not decided.

## The sources, and they are not equal

**`documents/TractionMotor/Zenodo/RAWCLIC_BEV_motor_consolidated_data_V1.xlsx`
is the only measured source.** 264 rows in the RAWCLIC 43-column house schema,
with `dataProcessor`, `DOI`, the four DQ columns and mean/median/mode/STD/
p025/p975.

    componentKeyLevel1   PMElectricMotors 110, EESMElectricMotors 110,
                         IMandPMElectricMotors 44
    componentKeyLevel2   stator, rotor, housing, coolingSystem, gearBox
    componentKeyLevel3   windings, statorSheetLaminationStack,
                         rotorSheetLaminationStack, rotorShaft,
                         permanentMagnets, conductiveBars, coolingChannels
    materialKeyLevel0-2  ferrous / non-ferrous -> AlAndAlAlloys, CuAndCuAlloys,
                         rareEarthMetalsAndAlloys, steelAndSteelAlloys ->
                         alloySteel, highCuAlloys2
    productKeyLevel3     A B C D E F, JB JC JD JE JF
    parameterCode        c-p (52 rows), m-c (212 rows)

**TWO THINGS IT DOES NOT CARRY, and they shape the whole project.**

**No elements.** `materialKeyLevel3` and `materialKeyLevel4` are empty and
there is no `e-m` row. The element layer arrives as a separate workbook,
derived from this same source -- `data.composition_file`, blank until it
exists. `04_03_tractionmotors.py` handles the empty levels: it takes the
highest filled material level and filters on `m-c`, which the file has.

**No years.** `productionYear` holds one value, `-2020`. ONE VINTAGE. The
2010-2070 span in `run.years` is a modelling decision, not a reading of the
data, and nothing in this repository yet says what changes between those years
or on whose authority.

**The reports beside it are a second tier, not a second source.** The critical
review of 2026-09-18 marks as unconfirmed the motor mass, the stator and rotor
laminations, the stator copper, the shaft, the housing, the bearings, the
cooling hardware, the sensors, and every architecture share for 2030, 2035,
2040 and 2050. What it confirms is qualitative: NdFeB carries Nd and Pr with
optional Dy or Tb; Nd is about 29-32% of magnet mass; magnet mass falls in a
broad 0.5-3.0 kg traction range; YASA P400 is 160 kW at 24-28.2 kg; the EU
strategic-material recycling benchmark is 25% by 2030.

## The five motors, and why the tier is a setting

`run.motors` maps each motor to where its numbers come from. Three are
`componentKeyLevel1` exactly as the dataset spells them. Two are OUR names, for
architectures the dataset does not carry because they are not yet in the fleet:

| motor | tier |
|---|---|
| `PMElectricMotors` | zenodo |
| `EESMElectricMotors` | zenodo |
| `IMandPMElectricMotors` | zenodo |
| `axialFluxPMElectricMotors` | report |
| `dualRotorRadialPMElectricMotors` | report |

The tier is a setting rather than a comment because **every number this project
reports has to say which of the two it came from.** A 2070 axial-flux magnet
mass and a 2020 PM magnet mass are not the same kind of statement, and a figure
that draws them in one colour says they are.

⚠️ **DeepDrive is not axial flux.** The report workbook's `Axial Flux` sheet
calls it "Double-rotor axial flux"; the critical review corrects that to a
dual-rotor RADIAL flux topology -- stator between inner and outer rotors --
citing the company's own technical description. The name follows the review.
If that is ever reversed, the name has to change with it.

SynRM, PMa-SynRM and in-wheel are deliberately absent: demonstrators in both
sources, with no bill of material in either.

## Running it

Press Run on `00_parameters.py`. It validates the settings, prints them, says
whether the two source workbooks are there, and regenerates `params.xlsx` and
`documentation/PARAMETER_REFERENCE.md`.

`99_check_environment.py` is the environment smoke test -- interpreter, pinned
packages, and a profile of any `.xlsx` in the project root. It writes nothing.
It was `00_check_environment.py` until 2026-09-18, when 00 became the
parameters as it is in every sibling project.

## Open

- **The element workbook does not exist.** Nothing here can produce an element
  layer until it does.
- **Nothing says what changes between 2010 and 2070.** `run.years` spans it; no
  rule fills it.
- **The two report-tier motors have no place to put their numbers yet.** Their
  bill of material is in a sheet with merged headers, not in the house schema.
- **The `gearBox` boundary.** `componentKeyLevel2` includes it, and the critical
  review flags e-axle boundaries as a reason published motor masses disagree.
  Whether a gearbox is part of a motor here is not decided.
