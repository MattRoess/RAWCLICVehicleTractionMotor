"""
src/composition.py
==================

Everything between the source workbooks and the composition dataset: the
benchmark, the audit, the corrections and the draws, in one file.

    read  ->  audit  ->  verify  ->  correct  ->  audit again

ONE FILE ON PURPOSE. These four things are not independent -- a correction
exists because an audit found something, the audit checks whether the
correction worked, the correction needs the benchmark to justify itself, and
its uncertainty needs the draws. Split across four modules they had to import
each other in a ring, and the order in which they run was implied rather than
written. Here it is written.

WHAT IS IN IT, IN ORDER
  1  DREXLER      the published benchmark, transcribed and cited
  2  DRAWS        the only place uncertainty is ever combined
  3  READING      the source registry's loaders, with the role gate
  4  AUDIT        every check, each written after finding what it checks for
  5  CORRECTIONS  each one declared with the evidence that establishes it

The parameters are NOT here. They are in `src/params_schema.py`, which is the
one file to open to change how this runs.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.params_schema import Params

# ============================================================ 1 DREXLER
# ======================================================================

CITATION = ('Drexler et al., e+i Elektrotech. Inftech. 142, 312-345 (2025), '
            'doi:10.1007/s00502-025-01331-3')

# The sample. Stated in the abstract.
VEHICLES = 31
MOTORS = 48
FIRST_MODEL_YEAR = 2018
LAST_MODEL_YEAR = 2023

# The two periods the authors compare throughout. Every trend below is the
# change between them, and they are the only time resolution the paper has.
EARLY = (2018, 2021)
LATE = (2022, 2023)

# ---------------------------------------------------------------- components
# component, what, n, mean, sd, min, max, and where in the paper it is.
# `sd` is None where the paper's figure caption is ambiguous in the extracted
# text: the stator lamination caption reads "33.07 kg" against an average of
# 16.62 kg with a maximum of 35.52 kg, which cannot be a standard deviation of
# that sample. NOT GUESSED -- left out until the figure is read by eye.
COMPONENTS = [
    dict(component='stator', part='statorSheetLaminationStack',
         n=46, mean=16.62, sd=None, min=7.20, max=35.52,
         min_vehicle='MG 4 Mulan Luxury',
         max_vehicle='Audi e-tron 55 Quattro Edition One, rear motor',
         where='Fig. 11c'),
    dict(component='rotor', part='rotorSheetLaminationStack',
         n=46, mean=11.06, sd=3.45, min=4.70, max=18.72,
         min_vehicle='MG 4 Mulan',
         max_vehicle='Mercedes EQC 400 4MATIC 1886 Edition, rear motor',
         where='Fig. 21d'),
    # Copper, split by winding technology -- which is the mechanism, not a
    # category: a flat-wire (hairpin) stator fills its slots better, so it
    # needs less copper for the same machine.
    dict(component='stator', part='windings.flatWire',
         n=None, mean=4.39, sd=None, min=2.04, max=7.02,
         min_vehicle='Toyota bZ4X', max_vehicle='VW ID.3 1st Max',
         where='Fig. 15d; insulation assumed 2% of winding weight'),
    dict(component='stator', part='windings.roundWire',
         n=22, mean=6.23, sd=1.76, min=3.63, max=9.54,
         min_vehicle='Volvo EX30 Twin Motor',
         max_vehicle='Renault Zoe R135 Edition One (9.25 kg at 5% insulation)',
         where='Fig. 16e; running text gives 6.05 kg and "42% more than flat '
               'wire" -- 4.39 x 1.42 = 6.23, so the figure value is used'),
]

# Rotor lamination by topology.
ROTOR_BY_TOPOLOGY = {'IM': 13.75, 'EESM': 11.34, 'PMSM': 10.11}   # Fig. 21d text

# ------------------------------------------------------------------- trends
# THE MEASURED MATERIAL REDUCTION. This is the evidence §4.1 of
# METHODOLOGY.md asked for and did not have: same function, less material,
# observed rather than assumed.
TRENDS = [
    dict(part='statorSheetLaminationStack', early=18.77, late=14.81,
         where='Sect. on stator active length and yoke thickness',
         mechanism='reduced active length and outer diameter'),
    dict(part='windings.roundWire', early=7.82, late=5.15,
         where='Sect. on round wire stators',
         mechanism='copper price and material efficiency effort'),
    dict(part='windings.all', early=5.90, late=4.51,
         where='Sect. on round wire stators, closing paragraph',
         mechanism='reduction regardless of topology and conductor'),
]


def components() -> pd.DataFrame:
    """The per-component statistics, one row each."""
    frame = pd.DataFrame(COMPONENTS)
    frame['source'] = 'drexler2025'
    frame['citation'] = CITATION
    return frame


def trends() -> pd.DataFrame:
    """
    The early-to-late change, with the annual rate it implies.

    THE RATE IS DERIVED HERE AND SAYS SO. The paper gives two period averages,
    not a rate. Taking the midpoints of 2018-2021 and 2022-2023 puts them three
    years apart, and the compound rate follows from that. A different reading
    of the midpoints gives a different rate, which is exactly why the two
    published numbers are kept beside it.
    """
    frame = pd.DataFrame(TRENDS)
    early_mid = sum(EARLY) / 2          # 2019.5
    late_mid = sum(LATE) / 2            # 2022.5
    span = late_mid - early_mid         # 3.0 years
    frame['change'] = frame.late / frame.early - 1
    frame['annual_rate'] = (frame.late / frame.early) ** (1 / span) - 1
    frame['span_years'] = span
    frame['derived'] = 'annual_rate computed here from the two period averages'
    frame['source'] = 'drexler2025'
    return frame

# ============================================================== 1a FLEET
# ======================================================================
def fleet(path: str) -> pd.DataFrame:
    """
    The EV Database snapshot, parsed into numbers.

    Everything in that file is a string with its unit attached -- '420 Nm',
    '208 kW (283 PS)', '1847 kg' -- so the parsing is part of reading it.

    ⚠️ TORQUE AND POWER ARE VEHICLE TOTALS. `performance_total_torque` is
    what the car delivers, summed over its motors, so a dual-motor car's
    figure is not one machine's figure. `motors` is taken from the drive
    layout (AWD = 2, Front or Rear = 1) and the per-motor columns divide by
    it. That assumes the two motors are equal, which they often are not --
    it is an approximation, and it is the best the file supports.

    `year` is the earliest availability date across all countries, which is
    market entry and not the model year.
    """
    import json
    import re

    frame = pd.read_csv(path)

    def number(column):
        return pd.to_numeric(
            frame[column].astype(str).str.extract(r'([\d.]+)')[0], errors='coerce')

    out = pd.DataFrame({
        'car_id': frame.car_id,
        'name': frame.name,
        'power_kw': number('performance_total_power'),
        'torque_nm': number('performance_total_torque'),
        'battery_voltage': number('battery_nominal_voltage'),
        'vehicle_mass_kg': number('dimensions_weight_unladen'),
        'segment': frame.miscellaneous_segment.str.split(' - ').str[0].str.strip(),
        'drive': frame.performance_drive,
    })
    # ⚠️ AWD = 2 IS AN ASSUMPTION AND IT BREAKS ABOVE ABOUT 1200 Nm.
    # Matthias 2026-09-18: more than 1200 Nm is several motors, not one AWD.
    # The file only records a drive layout, never a motor count, so the
    # assumption cannot be read out of it -- but it can be tested through the
    # power it implies per machine:
    #
    #     up to  600 Nm   median 150 kW per assumed motor
    #      600- 900 Nm    median 174 kW
    #      900-1200 Nm    median 242 kW
    #     1200-1500 Nm    median 348 kW, up to 425
    #     above 1500 Nm   up to 460 kW
    #
    # 430 kW out of one traction machine is not a machine anybody builds, so
    # the Lucid Air Sapphire at 920 kW is three motors and not two, and the
    # Lightyear 0 at 1720 Nm and 130 kW is four in-wheel motors reporting
    # WHEEL torque. Below 1200 Nm only 2% of models exceed 300 kW per assumed
    # motor and the assumption holds.
    #
    # This is the real reason run.torque_grid stops at 1200 Nm: not that the
    # vehicles above it are rare, but that up there the per-motor arithmetic
    # this project rests on is simply wrong.
    out['motors'] = frame.performance_drive.map(
        {'Front': 1, 'Rear': 1, 'AWD': 2})
    out['motor_count_doubtful'] = (out.power_kw / out.motors) > 300

    def first_year(value):
        try:
            years = [int(y) for entry in json.loads(value)
                     for y in re.findall(r'(20\d\d)', str(entry.get('value', '')))]
            return min(years) if years else np.nan
        except Exception:                                   # noqa: BLE001
            return np.nan

    out['year'] = frame.availability_json.map(first_year)
    out['torque_per_motor'] = out.torque_nm / out.motors
    out['power_per_motor'] = out.power_kw / out.motors
    out['sourceName'] = 'evdatabase'
    out['sourceTier'] = 'tier2'
    return out


# ====================================================== 1b MACHINE SPECS
# ======================================================================
# Manufacturer data sheets: whole-machine mass against torque, for machines
# the consolidated dataset does not contain.
#
# ⚠️ THESE ARE NOT BILLS OF MATERIAL. A data sheet gives what the machine
# weighs, not what it is made of. They cannot fill a composition row. What
# they CAN do is bound the sum: no bill of material for this machine may add
# up to more than its published dry mass, and a topology whose whole machine
# weighs less than another's active parts is saying something no regression
# through radial motors can say.
MACHINES = [
    # --- axial flux, shaft machines --------------------------------------
    dict(name='YASA P400 R', topology='axialFluxPM', maker='YASA (Mercedes-Benz)',
         mass_kg=24.0, mass_basis='cartridge, dry, no housing, no gearbox',
         scope='active', scope_certain=True,
         torque_shaft=370.0, torque_continuous=200.0,
         power_peak_kw=160.0, speed_max_rpm=8000,
         gearbox_kg=None, gearbox='none in the data sheet',
         cooling='oil, stator', voltage='800 V',
         source='YASA P400 R Product Sheet, Rev 13, June 2019, ID 22735',
         url='yasa.com'),
    dict(name='YASA P400 C', topology='axialFluxPM', maker='YASA (Mercedes-Benz)',
         mass_kg=28.2, mass_basis='with housing, dry, no gearbox',
         scope='motor', scope_certain=True,
         torque_shaft=370.0, torque_continuous=200.0,
         power_peak_kw=160.0, speed_max_rpm=8000,
         gearbox_kg=None, gearbox='none in the data sheet',
         cooling='oil, stator', voltage='800 V',
         source='YASA P400 R Product Sheet, Rev 13, June 2019, ID 22735',
         url='yasa.com'),
    dict(name='Equipmake APM-200', topology='axialFluxPM', maker='Equipmake',
         mass_kg=42.0, mass_basis='motor only, gearbox and inverter separate',
         scope='motor', scope_certain=True,
         torque_shaft=450.0, torque_continuous=None,
         power_peak_kw=220.0, speed_max_rpm=10000,
         gearbox_kg=9.0, gearbox='integrated 5.5:1 epicyclic, 2475 Nm at the '
                                 'driveshaft',
         cooling='liquid, rotor, 60 C water/glycol', voltage='750 V DC',
         source='Equipmake APM-200 product page', url='equipmake.com'),

    # --- high torque, low speed: little or no reduction -------------------
    # ⚠️ THESE ARE ON THE SAME AXIS AND DESIGNED FOR A DIFFERENT DUTY. Shaft
    # torque is shaft torque for all of them, so they belong on one axis --
    # Matthias 2026-09-18, and he is right that excluding one while keeping
    # another was inconsistent. But a machine making 1500 Nm at about 950 rpm
    # is not a machine making 370 Nm at 8000 rpm with a gearbox behind it: it
    # trades iron for the gearbox it does not need. Compare the SYSTEM, motor
    # plus reduction, or compare nothing.
    dict(name='DeepDrive RM 1500', topology='dualRotorRadialPM',
         maker='DeepDrive', mass_kg=32.0, mass_basis='motor',
         scope='motor', scope_certain=False,
         torque_shaft=1500.0, torque_continuous=None,
         power_peak_kw=150.0, speed_max_rpm=None,
         gearbox_kg=None, gearbox='little or none, high torque low speed',
         cooling=None, voltage=None,
         source='DeepDrive RM series, compact class',
         url='deepdrive.tech'),
    dict(name='DeepDrive RM 1800', topology='dualRotorRadialPM',
         maker='DeepDrive', mass_kg=35.0, mass_basis='motor',
         scope='motor', scope_certain=False,
         torque_shaft=1800.0, torque_continuous=None,
         power_peak_kw=180.0, speed_max_rpm=None,
         gearbox_kg=None, gearbox='little or none, high torque low speed',
         cooling=None, voltage=None,
         source='DeepDrive RM series, medium and large cars',
         url='deepdrive.tech'),
    dict(name='DeepDrive RM 2400', topology='dualRotorRadialPM',
         maker='DeepDrive', mass_kg=37.0, mass_basis='motor',
         scope='motor', scope_certain=False,
         torque_shaft=2400.0, torque_continuous=None,
         power_peak_kw=250.0, speed_max_rpm=None,
         gearbox_kg=None, gearbox='little or none; also offered in-wheel',
         cooling=None, voltage=None,
         source='DeepDrive RM series', url='deepdrive.tech'),
    dict(name='Donut Lab 21" hypercar', topology='axialFluxPM in-wheel',
         maker='Donut Lab', mass_kg=40.0, mass_basis='whole in-wheel motor',
         scope='motor', scope_certain=False,
         torque_shaft=4300.0, torque_continuous=None,
         power_peak_kw=630.0, speed_max_rpm=None,
         gearbox_kg=0.0, gearbox='none, direct drive in the wheel',
         cooling=None, voltage=None,
         source='Donut Lab motor family, CES 2025', url='donutlab.com/motor/'),
]

# ⚠️ THE SCOPES ARE NOT THE SAME, AND SOME ARE NOT KNOWN.
# Matthias 2026-09-18: APM-200 and YASA might not include the same components.
# He is right, and the difference is large enough to change the comparison.
#
#   YASA P400 R   24.0 kg  CARTRIDGE, explicitly without a housing
#   YASA P400 C   28.2 kg  with housing -- the same machine, +4.2 kg (+18%)
#   APM-200       42.0 kg  "motor", with gearbox (9 kg) and inverter (12 kg)
#                          listed separately, so the housing is inside it
#   DeepDrive     32-37 kg "motor", scope NOT STATED
#   Donut Lab     40.0 kg  "in-wheel motor", scope NOT STATED, and an in-wheel
#                          machine's boundary against hub, bearing and brake
#                          is exactly where the kilograms hide
#
# `scope` says what is in the number and `scope_certain` says whether the
# source said so. ONLY 'motor' WITH scope_certain COMPARES LIKE FOR LIKE --
# which today is YASA P400 C against Equipmake APM-200, 28.2 kg at 370 Nm
# against 42.0 kg at 450 Nm. Everything else is drawn, and marked.
#
# ⚠️ AND NONE OF THEM IS THE RADIAL SCOPE EITHER. The consolidated stack this
# is compared against is stator, rotor, windings, magnets, shaft and housing,
# summed over every motor in the vehicle -- so a single-machine data sheet
# belongs beside a single-machine share of it, not beside the vehicle total.

# ⚠️ DEEPDRIVE ALSO STATES A MATERIAL CLAIM, and it is the only one of these
# sources that does: the dual rotor uses **80% less iron and 50% less magnet
# material**, and it can be built without rare earths. Stated as a comparison
# with no baseline named, so it cannot be turned into kilograms -- but it is
# the direction METHODOLOGY.md 4.2 argues for, from a manufacturer.
DEEPDRIVE_MATERIAL_CLAIM = {
    'iron_reduction': 0.80,
    'magnet_reduction': 0.50,
    'baseline': 'not stated by the source',
    'rare_earth_free_possible': True,
}

# ⚠️ WHAT IS NOT HERE, AND THE PATTERN IN WHY.
#
#   YASA 750R       790 Nm peak, 200 kW, 98 mm axial -- MASS on request only
#   Equipmake       a widely repeated 31.4 kg for the APM-200, derived by
#                   somebody from "7 kW/kg". THE PRODUCT PAGE SAYS 42 kg.
#                   A number derived from a ratio is not a measurement, and
#                   this one was wrong by a third.
#   Valeo           EESM, hairpin stator, 210 mm diameter, combined
#                   water/oil cooling, +30% power density, -30% CO2 vs PMSM,
#                   SOP 2027 -- NO mass, NO torque
#   Valeo + MAHLE   iBEE, brushless EESM, 220-350 kW peak, 800 V,
#                   >40% lower production carbon -- NO mass, NO torque
#   ZF              I2SM, in-rotor inductive excitation, 400 V and 800 V,
#                   90 mm shorter than a conventional EESM -- NO mass
#
# THE PATTERN IS THE FINDING. Suppliers who sell motors as a COMPONENT to
# integrators publish mass, because an integrator has to package it: YASA,
# Equipmake, DeepDrive, Donut Lab. Suppliers who sell into OEM programmes
# publish power bands and advantages and never a mass, because the mass is
# negotiated per programme. So the magnet-free machines that matter most for
# Europe -- Valeo, MAHLE, ZF -- are exactly the ones with no public mass, and
# no amount of further searching changes that.
#
# What they DO establish: hairpin stators, combined water and oil cooling,
# 800 V and brushless excitation are in production or near it, which is direct
# evidence for the mechanisms in METHODOLOGY.md 4.2 and 4.3.


def machines() -> pd.DataFrame:
    """
    The manufacturer data sheets, one row per machine.

    ALL TORQUES ARE SHAFT TORQUE, which is what makes one axis legitimate.
    Whether a reduction follows is a separate column, not a separate figure.
    """
    return pd.DataFrame(MACHINES)


# ============================================================== 2 DRAWS
# ======================================================================

# The 95% interval is +-1.959964 sigma for a normal. Written out rather than
# rounded to 1.96, because the factor is used to go both ways and a rounded
# constant makes a round trip drift.
Z95 = 1.959963984540054


def sigma_from_interval(p025, p975):
    """Sigma implied by a 95% interval under a normal shape."""
    return (np.asarray(p975, dtype=float) - np.asarray(p025, dtype=float)) / (2 * Z95)


def _draw(mean, p025, p975, size: int, rng, correlated_with=None,
         correlation: float = 0.0):
    """
    `size` draws for one quantity.

    `correlated_with` is another quantity's STANDARD NORMAL draws, not its
    values: two masses of the same motor share the shock that makes that motor
    bigger or smaller than the regression expects, and it is the shock that is
    shared, not the scale.

    Returns the draws and the standard normals behind them, so that a third
    quantity can be correlated with the same shock.
    """
    mean = float(mean)
    sigma = float(sigma_from_interval(p025, p975))

    fresh = rng.standard_normal(size)
    if correlated_with is None:
        shocks = fresh
    else:
        # A shared shock plus an independent remainder, mixed so the result is
        # still standard normal and correlates with the partner at exactly
        # `correlation`.
        rho = float(correlation)
        shocks = rho * correlated_with + np.sqrt(max(0.0, 1.0 - rho ** 2)) * fresh

    values = mean + sigma * shocks
    return values, shocks


def _summarise(values, clip_at_zero: bool = True) -> dict:
    """
    Mean and percentiles OF THE DRAWS, plus what had to be clipped.

    A mass cannot be negative and a normal can, so draws are clipped at zero
    and the count is reported. A clip rate that is not tiny means the normal
    shape is wrong for that quantity, and it should be visible rather than
    quietly corrected.
    """
    values = np.asarray(values, dtype=float)
    clipped = int((values < 0).sum()) if clip_at_zero else 0
    if clip_at_zero and clipped:
        values = np.clip(values, 0.0, None)
    return {
        'meanValue': float(values.mean()),
        'medianValue': float(np.median(values)),
        'p025': float(np.percentile(values, 2.5)),
        'p975': float(np.percentile(values, 97.5)),
        'STD': float(values.std(ddof=1)),
        'clipped': clipped,
        'clipped_share': clipped / values.size if values.size else 0.0,
    }

# ============================================================ 3 READING
# ======================================================================

# Columns the house schema guarantees and every check below relies on. Named
# here so a re-issued workbook that renames one fails loudly at load, rather
# than silently producing empty checks.
REQUIRED = (
    'parameterCode', 'productKeyLevel3', 'productionYear',
    'componentKeyLevel1', 'componentKeyLevel2', 'componentKeyLevel3',
    'materialKeyLevel0', 'materialKeyLevel1', 'materialKeyLevel2',
    'meanValue', 'p025', 'p975',
)

# How close two masses have to be before the audit calls them the same number.
# Not a float-comparison epsilon: the stator finding is an EXACT tie to the
# last digit, which is itself the evidence that one cell was copied from the
# other rather than computed.
IDENTICAL = 1e-9


def load(params: Params, name: str = '') -> pd.DataFrame:
    """
    One declared source, read by whichever reader it says it needs.

    `name` defaults to `data.primary`. **A VERIFICATION SOURCE IS REFUSED
    HERE**, in code, not by convention: METHODOLOGY.md §2.1 says no number
    lives only in prose is a rule that gets broken by whoever is in a hurry.
    Compare against those sources with `load_verification`, which says in its
    name what the result may be used for.
    """
    name = name or params.data.primary
    entry = params.data.sources.get(name)
    if entry is None:
        raise KeyError(f'{name!r} is not a source in data.sources. Declared: '
                       f'{sorted(params.data.sources)}')
    if entry.get('role') != 'data':
        raise PermissionError(
            f'{name!r} is a {entry.get("role")!r} source and cannot be read into '
            f'the dataset (METHODOLOGY.md §2.1). Its numbers may only be '
            f'compared against values established elsewhere -- use '
            f'load_verification({name!r}).')
    return _read(params, name, entry)


def load_verification(params: Params, name: str) -> pd.DataFrame:
    """
    A verification source, for comparison only.

    Separate from `load` so that the call site says which it is. Nothing read
    here may be written into `data/`; the comparison belongs in documentation.
    """
    entry = params.data.sources.get(name)
    if entry is None:
        raise KeyError(f'{name!r} is not a source in data.sources')
    if entry.get('role') != 'verification':
        raise PermissionError(f'{name!r} is a {entry.get("role")!r} source; '
                              f'read it with load()')
    return _read(params, name, entry)


def _read(params: Params, name: str, entry: dict) -> pd.DataFrame:
    """Dispatch to the reader the source declares, and check what came back."""
    path = entry.get('file')
    if not path:
        raise FileNotFoundError(
            f'{name!r} is declared but its file is blank -- the source is known '
            f'and not yet in hand. Put the file in place and set '
            f'data.sources[{name!r}]["file"].')

    reader = entry.get('reads')
    if reader == 'house':
        frame = pd.read_excel(path, sheet_name=entry.get('sheet') or 0)
        missing = [column for column in REQUIRED if column not in frame.columns]
        if missing:
            raise KeyError(
                f'{path} is missing the columns {missing}. `reads="house"` means '
                f'the RAWCLIC house schema; a workbook without these is a '
                f'different shape and needs its own reader.')
    elif reader == 'drexler':
        # Published statistics, transcribed and cited in src/drexler.py. The
        # paper is a PDF of prose and figures, not a table anyone can read
        # mechanically, so the transcription is the reader -- and it is in
        # code so that every value is diffable and attributable.
        frame = components()
    elif reader == 'fleet':
        frame = fleet(path)
    elif reader == 'spec':
        # Manufacturer data sheets, transcribed and cited above.
        frame = machines()
    elif reader == 'bom':
        # A published benchmark, in whatever shape its authors chose. There is
        # no such file in hand yet, so there is nothing to guess at: the reader
        # is written when the first one arrives, against that file. Declaring
        # the shape now would be inventing a schema for a document nobody here
        # has opened.
        raise NotImplementedError(
            f'{name!r} declares reads="bom" and no bom reader exists yet. '
            f'Write one in src/source.py against the actual file, then this '
            f'source loads with no other change.')
    else:
        raise ValueError(f'{name!r} declares an unknown reader {reader!r}')

    # Stamp provenance onto the rows themselves. A frame that has travelled
    # two function calls should still be able to say where it came from, so
    # that no figure can draw a tier-1 and a tier-2 number in one colour
    # without the code having had the chance to notice.
    frame = frame.copy()
    frame['sourceName'] = name
    frame['sourceTier'] = entry.get('tier')
    return frame


def _finding(check, severity, motor, segment, where, detail, **values) -> dict:
    """One row of the audit. Flat, so the whole audit is one readable table."""
    row = {'check': check, 'severity': severity, 'motor': motor,
           'segment': segment, 'where': where, 'detail': detail}
    row.update(values)
    return row


_FLEET_TORQUE: dict = {}


def load_fleet_ranges(params: Params) -> dict:
    """
    Per segment, the lowest and highest torque the fleet actually contains.

    Filled once and cached, because the audit runs twice per stage and the
    file is 1438 rows of strings that have to be parsed.
    """
    global _FLEET_TORQUE
    if _FLEET_TORQUE:
        return _FLEET_TORQUE
    try:
        fleet_frame = load(params, 'evdatabase').dropna(subset=['torque_nm'])
    except Exception:                                       # noqa: BLE001
        return _FLEET_TORQUE
    # ⚠️ p05 AND p95, NOT MIN AND MAX, and this was measured rather than
    # preferred. The first version of C6 used the true extremes and made the
    # fit WORSE: R2 on stator lamination against torque fell from 0.895 with
    # the workbook's own torques to 0.666. A single 1760 Nm vehicle drags
    # segment D's midpoint from 490 Nm to 1025 Nm while its mass stays where
    # it was, so mass and torque stop agreeing.
    #
    # Tested against the masses, on the same fit:
    #     workbook's own torques        R2 0.895
    #     fleet, midpoint of p05/p95    R2 0.857   <- used
    #     fleet, mean                   R2 0.845
    #     fleet, median                 R2 0.818
    #     fleet, midpoint of min/max    R2 0.666
    #
    # A range is meant to say where the segment's vehicles are, not where its
    # single strangest vehicle is.
    grouped = fleet_frame.groupby('segment')['torque_nm'].agg(
        low=lambda s: s.quantile(0.05),
        high=lambda s: s.quantile(0.95),
        count='count')
    _FLEET_TORQUE = {segment: (row['low'], row['high'], int(row['count']))
                     for segment, row in grouped.iterrows()}
    return _FLEET_TORQUE


def audit(frame: pd.DataFrame, params: Params) -> pd.DataFrame:
    """
    Every defect found in the workbook, one per row.

    Severity says what it costs downstream, not how surprising it is:
      blocking  a number that would be WRONG in the stock-and-flow model
      gap       a number that is simply absent, so nothing can be reported
      note      a property of the dataset worth knowing before using it
    """
    findings: list[dict] = []
    data = params.data
    load_fleet_ranges(params)

    # ------------------------------------------------------------------ 1
    # THE STATOR IS COUNTED TWICE, or the stator total is not the stator.
    #
    # For every filled case, the `statorSheetLaminationStack` material row
    # holds EXACTLY the value of the stator `c-p` row -- to the last digit,
    # 24 cases out of 24. The stator also carries a `windings` row. So the
    # stator's materials sum to about 1.24x the mass the same workbook gives
    # for the stator.
    #
    # One of the two readings is true and they are not equivalent:
    #   (a) the lamination cell was filled with the stator total, and the
    #       real lamination mass is stator - windings; or
    #   (b) the `c-p` stator cell holds the LAMINATION mass, and the real
    #       stator is lamination + windings, about 24% heavier.
    # Under (a) the motor is as heavy as stated and the split is wrong; under
    # (b) every stator in the dataset is understated. This is not the audit's
    # decision -- see documentation/SOURCE_AUDIT.md.
    cp = frame[frame.parameterCode == data.component_of_product]
    mc = frame[frame.parameterCode == data.material_of_component]
    key = ['componentKeyLevel1', 'productKeyLevel3']

    stator_cp = cp[cp.componentKeyLevel2 == 'stator'].set_index(key)['meanValue']
    lamination = mc[mc.componentKeyLevel3 ==
                    'statorSheetLaminationStack'].set_index(key)['meanValue']
    windings = mc[(mc.componentKeyLevel2 == 'stator') &
                  (mc.componentKeyLevel3 == 'windings')].set_index(key)['meanValue']

    for index in stator_cp.index:
        total, stack = stator_cp.get(index), lamination.get(index)
        coil = windings.get(index)
        if pd.isna(total) or pd.isna(stack):
            continue
        if abs(total - stack) < IDENTICAL:
            materials = stack + (0 if pd.isna(coil) else coil)
            findings.append(_finding(
                'stator-counted-twice', 'blocking', index[0], index[1],
                'stator / statorSheetLaminationStack',
                'the lamination material row equals the stator total exactly, '
                'and the stator also carries windings, so its materials sum to '
                f'{materials / total:.3f}x the stated stator mass',
                stator_total=total, lamination=stack, windings=coil,
                materials_sum=materials, ratio=materials / total))

    # ------------------------------------------------------------------ 2
    # MATERIALS THAT DO NOT ADD UP TO THEIR COMPONENT, in general. Check 1 is
    # the specific case already understood; this catches any other component
    # where the two layers disagree, including in a re-issued workbook.
    totals = cp.dropna(subset=['meanValue']).groupby(
        key + ['componentKeyLevel2'])['meanValue'].sum()
    sums = mc.dropna(subset=['meanValue']).groupby(
        key + ['componentKeyLevel2'])['meanValue'].sum()
    for index, total in totals.items():
        summed = sums.get(index)
        if summed is None or total == 0:
            continue
        ratio = summed / total
        if abs(ratio - 1) > 1e-6 and index[2] != 'stator':   # stator is check 1
            findings.append(_finding(
                'materials-do-not-sum', 'blocking', index[0], index[1], index[2],
                f'materials sum to {ratio:.3f}x the component mass',
                component_total=total, materials_sum=summed, ratio=ratio))

    # ------------------------------------------------------------------ 3
    # RARE EARTH IN A MOTOR BUILT TO AVOID IT.
    #
    # The EESM rotor `windings` rows are labelled `rareEarthMetalsAndAlloys`.
    # An externally excited synchronous machine excites its rotor with a
    # WOUND FIELD precisely so that it needs no magnet: the winding is copper.
    # Taken as written, every EESM in the fleet carries about 10.9 kg of rare
    # earth, which would be the largest rare-earth term in the whole model and
    # is the opposite of what the machine is for.
    suspect = mc[(mc.componentKeyLevel2 == 'rotor') &
                 (mc.componentKeyLevel3 == 'windings') &
                 (mc.materialKeyLevel1 == 'rareEarthMetalsAndAlloys')]
    for _, row in suspect.iterrows():
        findings.append(_finding(
            'winding-labelled-rare-earth', 'blocking',
            row.componentKeyLevel1, row.productKeyLevel3, 'rotor / windings',
            'a wound rotor field is copper; labelled '
            f'{row.materialKeyLevel1!r} under {row.materialKeyLevel0!r}',
            meanValue=row.meanValue))

    # ------------------------------------------------------------------ 4
    # A COMPONENT THAT EXISTS ONLY AS A MATERIAL ROW. `housing` and `gearBox`
    # are recorded with parameterCode `m-c` -- a material of a component --
    # while being components of the product. Housing carries no material keys
    # at all, so it is a mass belonging to nothing. Read literally by a stage
    # that walks the schema, neither has a component mass and both are lost.
    for component in sorted(set(mc.componentKeyLevel2.dropna())):
        if component in set(cp.componentKeyLevel2.dropna()):
            continue
        rows = mc[mc.componentKeyLevel2 == component]
        unmaterialed = int(rows.materialKeyLevel1.isna().sum())
        findings.append(_finding(
            'component-without-c-p', 'blocking', '(all)', '(all)', component,
            f'{len(rows)} rows, all parameterCode {data.material_of_component!r}, '
            f'and no {data.component_of_product!r} row anywhere'
            + (f'; {unmaterialed} of them name no material either'
               if unmaterialed else ''),
            rows=len(rows)))

    # ------------------------------------------------------------------ 5
    # ROWS THAT EXIST AND ARE EMPTY. Not the same as a row that is absent: the
    # workbook asserts the component is there and declines to say how much.
    for code, group in frame.groupby('parameterCode'):
        blank = group[group.meanValue.isna()]
        if blank.empty:
            continue
        for where, rows in blank.groupby(
                [blank.componentKeyLevel2.fillna('(none)'),
                 blank.componentKeyLevel3.fillna('(none)')]):
            findings.append(_finding(
                'blank-value', 'gap', '(various)', '(various)',
                f'{where[0]} / {where[1]}',
                f'{len(rows)} {code} rows present with no meanValue',
                rows=len(rows), parameterCode=code))

    # ------------------------------------------------------------------ 6
    # THE SAME NUMBER REPEATED ACROSS SEGMENTS. Vehicle segments A to F differ
    # in size by more than a factor of two, so a mass identical across many of
    # them is a filled-down cell rather than a measurement.
    for (motor, component, sub), group in mc.dropna(subset=['meanValue']).groupby(
            ['componentKeyLevel1', 'componentKeyLevel2',
             mc.componentKeyLevel3.fillna('(none)')]):
        counts = group.meanValue.round(6).value_counts()
        for value, count in counts.items():
            if count >= 4:
                findings.append(_finding(
                    'repeated-across-segments', 'note', motor, '(several)',
                    f'{component} / {sub}',
                    f'{count} segments carry the identical value {value:g}, '
                    'which segments of different size should not',
                    value=value, segments=count))

    # ------------------------------------------------------------------ 7
    # WHAT THE WORKBOOK DOES NOT HAVE AT ALL. Stated as findings so that the
    # audit is a complete account of the source rather than a list of its
    # mistakes -- these two shape the project more than any defect above.
    if data.element_of_material not in set(frame.parameterCode.dropna()):
        findings.append(_finding(
            'no-element-layer', 'gap', '(all)', '(all)', 'e-m',
            'no element rows at all: materials stop at materialKeyLevel2, so '
            'no element mass can be reported from this source'))

    years = sorted(set(frame.productionYear.dropna()))
    if len(years) == 1:
        findings.append(_finding(
            'one-vintage', 'note', '(all)', '(all)', 'productionYear',
            f'one vintage, {years[0]}: every year of a 2010-2070 trajectory '
            'is a modelling decision and none of it is measured',
            value=years[0]))

    # ------------------------------------------------------------------ 7b
    # A VALUE WITH NO UNCERTAINTY, in a dataset where every value is a
    # regression with a confidence interval. p025 == p975 means the number did
    # not come out of the fit: it was entered. This check needs no external
    # source -- the dataset contradicts itself -- and it is the strongest kind
    # of finding there is.
    filled = frame.dropna(subset=['meanValue'])
    flat = filled[filled.p025 == filled.p975]
    if not flat.empty:
        for where, rows in flat.groupby(
                [flat.componentKeyLevel1.fillna('(all)'),
                 flat.componentKeyLevel2.fillna('(none)'),
                 flat.componentKeyLevel3.fillna('(none)')]):
            findings.append(_finding(
                'zero-interval', 'blocking', where[0], '(several)',
                f'{where[1]} / {where[2]}',
                f'{len(rows)} rows have p025 == p975, the only ones among '
                f'{len(filled)} filled rows in this dataset. Every value here '
                f'is a torque regression with a confidence interval, so a '
                f'value without one was entered rather than fitted',
                rows=len(rows)))

    # ------------------------------------------------------------------ 7c
    # A MASS WITHOUT ITS TORQUE. Component mass in this dataset is a
    # regression ON TORQUE, so a row whose torque is missing cannot be placed
    # against any other row, compared with any benchmark, or projected on a
    # per-Nm basis. It is a number without its explanatory variable.
    if 'torque_min' in frame.columns:
        filled_rows = frame.dropna(subset=['meanValue'])
        no_torque = filled_rows[filled_rows.torque_min.isna()]
        if not no_torque.empty:
            for where, rows in no_torque.groupby(
                    [no_torque.componentKeyLevel2.fillna('(none)'),
                     no_torque.parameterCode.fillna('(none)')]):
                findings.append(_finding(
                    'no-torque', 'gap', '(various)', '(various)',
                    f'{where[0]} / {where[1]}',
                    f'{len(rows)} rows carry a mass and no torque, so the mass '
                    f'cannot be compared with anything or expressed per Nm',
                    rows=len(rows)))

    # ------------------------------------------------------------------ 7d
    # TORQUE RANGES THE FLEET DOES NOT CONTAIN. The consolidated dataset
    # states a torque_min and torque_max per segment, taken from the EV
    # Database, and the regressions are evaluated across that range. A later
    # snapshot of the same database says which torques the segment really
    # holds. Where the stated maximum is above anything the fleet contains,
    # the regression was evaluated outside its own sampling frame.
    if 'productKeyLevel3' in frame.columns and _FLEET_TORQUE:
        stated = frame.dropna(subset=['torque_min']).groupby(
            'productKeyLevel3')[['torque_min', 'torque_max']].first()
        for segment, row in stated.iterrows():
            actual = _FLEET_TORQUE.get(segment)
            if not actual:
                continue
            low, high, count = actual
            if row.torque_max > high * 1.02:
                findings.append(_finding(
                    'torque-beyond-fleet', 'note', '(all)', segment, 'torque_max',
                    f'stated maximum {row.torque_max:.0f} Nm against {high:.0f} Nm, '
                    f'the highest in {count} models of that segment in the EV '
                    f'Database -- a factor of {row.torque_max / high:.2f}',
                    value=row.torque_max))

    # ------------------------------------------------------------------ 8
    # ROWS THIS PROJECT HAS MARKED UNRELIABLE. Only present once corrections
    # have run. Reported by the audit so that a marked value cannot travel
    # quietly: a flag nobody reads is decoration.
    if 'reliability' in frame.columns:
        marked = frame[frame.reliability.fillna('') == 'unreliable']
        for (flag, motor), rows in marked.groupby(
                [marked.flag.fillna('?'), marked.componentKeyLevel1.fillna('(all)')]):
            findings.append(_finding(
                'marked-unreliable', 'note', motor, '(several)',
                f'{rows.componentKeyLevel2.iloc[0]} / '
                f'{rows.componentKeyLevel3.fillna("(none)").iloc[0]}',
                f'{len(rows)} rows kept as published and marked {flag!r}: '
                f'{rows.flagReason.iloc[0][:160]}...',
                rows=len(rows)))

    columns = ['check', 'severity', 'motor', 'segment', 'where', 'detail',
               'stator_total', 'lamination', 'windings', 'materials_sum',
               'component_total', 'ratio', 'meanValue', 'value', 'rows',
               'segments', 'parameterCode']
    result = pd.DataFrame(findings)
    for column in columns:
        if column not in result.columns:
            result[column] = pd.NA
    order = {'blocking': 0, 'gap': 1, 'note': 2}
    return (result[columns]
            .assign(_rank=lambda f: f.severity.map(order))
            .sort_values(['_rank', 'check', 'motor', 'segment'])
            .drop(columns='_rank')
            .reset_index(drop=True))

# ======================================================== 5 CORRECTIONS
# ======================================================================

# Drexler et al. (2025), transcribed in src/drexler.py. Cited here by figure.
DREXLER = 'Drexler et al. 2025, doi:10.1007/s00502-025-01331-3'

CORRECTIONS = [

    # -------------------------------------------------------------- C1
    dict(
        id='C1-stator-lamination',
        defect='The statorSheetLaminationStack material row holds the stator '
               'total exactly, in 24 of 24 filled cases, in a stator that also '
               'carries windings.',
        evidence=f'01_composition.py against {DREXLER}, Fig. 11c: stator '
                 f'lamination measured on 46 machines at 7.20-35.52 kg. '
                 f'Reading the c-p row as the lamination puts 10 of 24 values '
                 f'above the measured maximum, up to 52.72 kg; reading it as '
                 f'the stator puts 23 of 24 inside the range.',
        action='lamination := c-p stator - stator windings, PER DRAW',
        note='Total motor mass is unaffected. The material split was wrong, '
             'not the mass. The interval is drawn, not shifted: the '
             'lamination is a DIFFERENCE of two correlated uncertain '
             'masses, and its width is not the stator\'s width.',
        applied=True),

    # -------------------------------------------------------------- C2
    dict(
        id='C2-eesm-rotor-winding-material',
        defect='EESM rotor windings are labelled rareEarthMetalsAndAlloys '
               'under non-ferrousMetals, 11 rows.',
        evidence=f'{DREXLER}, Sect. on EESM rotors: "power is transferred from '
                 f'the battery to the rotor winding conductively via sliding '
                 f'brushes and copper sleeves", nine EESM rotors examined. An '
                 f'externally excited machine uses a wound field precisely so '
                 f'that it needs no magnet.',
        action='materialKeyLevel0/1/2 := non-ferrousMetals / CuAndCuAlloys / '
               'highCuAlloys2',
        note='Left as written, every EESM in the fleet would carry ~10.9 kg of '
             'rare earth -- the largest rare-earth term in the model, in the '
             'one machine built to avoid it.',
        applied=True),

    # -------------------------------------------------------------- C3
    dict(
        id='C3-eesm-rotor-winding-mass',
        defect='The same rows carry 7.53-10.88 kg, and the value is pinned at '
               'exactly 10.880000 across 8 of 11 segments.',
        evidence=f'Two independent lines. (1) {DREXLER}, Fig. 30b: average '
                 f'total rotor copper mass 3.68 kg, max 4.45 kg (BMW i7 '
                 f'xDrive60 Individual), min 2.86 kg (BMW iX1 xDrive30 '
                 f'Premium), at 5% insulation -- the consolidated values are '
                 f'2-3x the measured maximum. (2) THE DATASET ITSELF: these '
                 f'are the only 10 of 192 filled rows with p025 == p975 and '
                 f'STD ~1e-15. Everything else is a regression with a '
                 f'confidence interval; these were entered, not fitted.',
        action='FLAG ONLY -- the value is kept and marked unreliable',
        note='Decided 2026-09-18: do not replace the mass, mark it. Replacing '
             'a segment-resolved series with one benchmark average is a '
             'modelling decision, not a correction, and the 1.5x '
             'segment-to-motor offset established in 01_composition.py '
             'means the two are not directly comparable either. So the number '
             'stays exactly as the source has it, and every row carrying it '
             'says it cannot be relied on.',
        applied=True),

    # -------------------------------------------------------------- C4
    dict(
        id='C4-components-without-c-p',
        defect='housing, gearBox and coolingSystem are recorded as m-c rows '
               'with no c-p row anywhere, 26 rows each. A stage walking the '
               'schema drops all three.',
        evidence='Consolidated description, Sect. 3: "The housing and cooling '
                 'system was modelled as a single component, as both are '
                 'predominantly composed of aluminium and are often '
                 f'structurally integrated." {DREXLER}, Sect. 5.1.1: the motor '
                 f'housing "is usually a cast aluminium or extruded profile".',
        action='add a c-p row per motor and segment carrying the mass already '
               'present; label the housing material AlAndAlAlloys',
        note='The gearbox is inside this project\'s boundary (METHODOLOGY.md '
             '§1), so this is not cosmetic.',
        applied=True),

    # -------------------------------------------------------------- C6
    dict(
        id='C6-torque-from-fleet',
        defect='Four segments state a torque_max the fleet does not contain: '
               'C at 1100 Nm against 600, A at 345 against 212, JB at 740 '
               'against 584, B at 395 against 360.',
        evidence='EV Database snapshot 2026-09, 1438 models -- the same '
                 'database the consolidated description names as its torque '
                 'source. Several minima match it to the kilogram (A 113, '
                 'D 290, F 345, JC 220), so the lower bound was read from it '
                 'and the upper bound was not.',
        action='torque_min/max := the observed p05-p95 range of that segment',
        note='Vehicle TOTAL torque, established rather than assumed: the '
             'total matches the stated minima in 4 of 11 segments against 1 '
             'of 11 for per-motor, and JC matches exactly at both ends. The '
             'masses agree -- Zenodo equals Drexler per machine times the '
             'average motor count per segment, median ratio 1.08.',
        applied=True),

    # -------------------------------------------------------------- C5
    dict(
        id='C5-conductive-bars-material',
        defect='The induction machine\'s rotor conductiveBars are labelled '
               'CuAndCuAlloys. All 4 rows are also blank.',
        evidence=f'{DREXLER}, Sect. on IM rotors: the short-circuit cage "is '
                 f'usually made of aluminum or copper, although ALL EIGHT '
                 f'motors examined in the sample were made of aluminum", '
                 f'average aluminium mass 2.26 kg (max 3.83 kg Audi e-tron 55 '
                 f'rear, min 1.57 kg Tesla Model Y AWD Standard Range).',
        action='materialKeyLevel0/1 := non-ferrousMetals / AlAndAlAlloys',
        note='Found by the audit as a blank, and by Drexler as a wrong '
             'material. The mass stays blank: 2.26 kg is a motor average and '
             'the consolidated rows are segment averages.',
        applied=True),
]


def declared() -> pd.DataFrame:
    """The corrections as a table, for printing and for the written record."""
    return pd.DataFrame(CORRECTIONS)


def apply_corrections(frame: pd.DataFrame, params: Params) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    The corrected dataset, and a log of what each correction actually changed.

    THE LOG COUNTS ROWS. A correction that matches nothing is a correction
    written against a workbook that has since changed, and it has to be visible
    rather than silently doing nothing.
    """
    data = params.data
    out = frame.copy()
    out['corrected'] = ''
    # This project's own quality columns. NOT the house schema's dq* columns:
    # those are empty here and their 1-4 scale has no documented direction.
    out['reliability'] = ''
    out['flag'] = ''
    out['flagReason'] = ''
    out['flagSource'] = ''
    out['torqueSource'] = 'as published'
    log: list[dict] = []

    def note(correction_id: str, changed: int, what: str) -> None:
        log.append(dict(id=correction_id, rows_changed=changed, what=what))

    # ---- C1 -------------------------------------------------------------
    # ⚠️ THE INTERVAL IS DRAWN, NOT SHIFTED. The first version of this
    # correction moved p025/p975 by the same amount as the mean, which is
    # interval arithmetic wearing a disguise: it kept the stator's own width
    # for a quantity that is a DIFFERENCE of two uncertain masses. Here the
    # difference is taken per draw and the percentiles are of the result.
    #
    # The two masses are correlated -- both are regressions on the same
    # vehicle's torque, so a motor bigger than the fit expects is bigger in
    # both, and the errors largely cancel. `within_motor_correlation` carries
    # that assumption, it is NOT measured, and it matters: at rho=0.9 the
    # lamination interval is markedly narrower than the shifted one, and at
    # rho=0 it would be wider.
    rng = np.random.default_rng(params.monte_carlo.seed)
    size = params.monte_carlo.draws
    rho = params.monte_carlo.within_motor_correlation

    key = ['componentKeyLevel1', 'productKeyLevel3']
    def _rows(code, **where):
        mask = out.parameterCode == code
        for column, value in where.items():
            mask &= out[column] == value
        return out[mask].set_index(key)

    stator_rows = _rows(data.component_of_product, componentKeyLevel2='stator')
    winding_rows = _rows(data.material_of_component, componentKeyLevel2='stator',
                         componentKeyLevel3='windings')
    is_lamination = ((out.parameterCode == data.material_of_component) &
                     (out.componentKeyLevel3 == 'statorSheetLaminationStack'))
    changed = 0
    clipped_total = 0
    for index in out[is_lamination].index:
        row = out.loc[index]
        pair = (row.componentKeyLevel1, row.productKeyLevel3)
        if pair not in stator_rows.index or pair not in winding_rows.index:
            continue
        stator = stator_rows.loc[pair]
        winding = winding_rows.loc[pair]
        if pd.isna(stator.meanValue) or pd.isna(winding.meanValue):
            continue

        stator_draws, shock = _draw(
            stator.meanValue, stator.p025, stator.p975, size, rng)
        winding_draws, _ = _draw(
            winding.meanValue, winding.p025, winding.p975, size, rng,
            correlated_with=shock, correlation=rho)

        summary = _summarise(stator_draws - winding_draws)
        clipped_total += summary.pop('clipped')
        summary.pop('clipped_share')
        for column, value in summary.items():
            if column in out.columns:
                out.at[index, column] = value
        # The mode is not drawn -- nothing in the source says what it was --
        # so it is cleared rather than left holding the old stator total.
        if 'modeValue' in out.columns:
            out.at[index, 'modeValue'] = None
        out.at[index, 'corrected'] = 'C1'
        changed += 1
    note('C1-stator-lamination', changed,
         f'lamination drawn as stator - windings, {size:,} draws, rho={rho}'
         + (f', {clipped_total} draws clipped at zero' if clipped_total else ''))

    # ---- C2 -------------------------------------------------------------
    mask = ((out.parameterCode == data.material_of_component) &
            (out.componentKeyLevel2 == 'rotor') &
            (out.componentKeyLevel3 == 'windings') &
            (out.materialKeyLevel1 == 'rareEarthMetalsAndAlloys'))
    out.loc[mask, 'materialKeyLevel0'] = 'non-ferrousMetals'
    out.loc[mask, 'materialKeyLevel1'] = 'CuAndCuAlloys'
    out.loc[mask, 'materialKeyLevel2'] = 'highCuAlloys2'
    out.loc[mask, 'corrected'] = (out.loc[mask, 'corrected'] + ' C2').str.strip()
    note('C2-eesm-rotor-winding-material', int(mask.sum()),
         'rare earth -> copper on the EESM rotor winding')

    # ---- C3: the value is kept and marked ------------------------------
    # ⚠️ MARKED, NOT CHANGED. The mass stays exactly as the source has it.
    # What changes is that the row now says it cannot be relied on, so that
    # nothing downstream can use it without having been told.
    #
    # WHY NOT THE dq COLUMNS. The house schema has dqValidity, dqAccuracy,
    # dqIntegrity, dqTimeliness and dqCompleteness on a 1-4 scale. In this
    # workbook all five are EMPTY in all 264 rows, and the Guideline sheet
    # gives each one's question without saying which end of 1-4 is good.
    # Writing a number into a scale whose direction is undocumented would put
    # a value into a dataset that gets handed on, meaning the opposite of what
    # was intended half the time. Flagged in this project's own columns
    # instead, whose meaning is defined here and nowhere else.
    mask = ((out.parameterCode == data.material_of_component) &
            (out.componentKeyLevel2 == 'rotor') &
            (out.componentKeyLevel3 == 'windings') &
            (out.componentKeyLevel1 == 'EESMElectricMotors'))
    out.loc[mask, 'reliability'] = 'unreliable'
    out.loc[mask, 'flag'] = 'C3-mass-unreliable'
    out.loc[mask, 'flagReason'] = (
        'Value kept as published and NOT corrected. Drexler 2025 Fig. 30b '
        'measures total rotor copper at 3.68 kg (2.86-4.45 kg over 9 EESM '
        'rotors); these rows carry 7.53-10.88 kg, two to three times the '
        'measured maximum. The value is also pinned at exactly 10.880000 '
        'across 8 of 11 segments, which segments differing in size by more '
        'than a factor of two should not be -- a filled-down cell. And the '
        'dataset says so itself: these are the ONLY 10 rows out of 192 filled '
        'rows whose p025 equals p975, STD ~1e-15. Every other value in the '
        'workbook is a torque regression carrying a confidence interval, so '
        'these did not come out of the fit -- they were entered. Treat as an '
        'upper bound of unknown quality, not as a measurement.')
    out.loc[mask, 'flagSource'] = DREXLER
    note('C3-eesm-rotor-winding-mass', int(mask.sum()),
         'mass KEPT unchanged and marked unreliable')

    # ---- C4 -------------------------------------------------------------
    new_rows = []
    for component in ('housing', 'gearBox', 'coolingSystem'):
        rows = out[(out.parameterCode == data.material_of_component) &
                   (out.componentKeyLevel2 == component)]
        for _, row in rows.iterrows():
            promoted = row.copy()
            promoted['parameterCode'] = data.component_of_product
            promoted['parameter'] = 'mass of component (kg) in product'
            # A component row names no material: the material belongs to the
            # m-c row, which stays where it is.
            for column in ('materialKeyLevel0', 'materialKeyLevel1',
                           'materialKeyLevel2', 'materialKeyLevel3',
                           'materialKeyLevel4', 'componentKeyLevel3'):
                if column in promoted.index:
                    promoted[column] = None
            promoted['corrected'] = 'C4'
            new_rows.append(promoted)
        # The housing m-c row names no material at all, and the description
        # says housing and cooling are one predominantly aluminium component.
        if component == 'housing':
            blank = ((out.parameterCode == data.material_of_component) &
                     (out.componentKeyLevel2 == 'housing') &
                     (out.materialKeyLevel1.isna()))
            out.loc[blank, 'materialKeyLevel0'] = 'non-ferrousMetals'
            out.loc[blank, 'materialKeyLevel1'] = 'AlAndAlAlloys'
            out.loc[blank, 'corrected'] = (
                out.loc[blank, 'corrected'] + ' C4').str.strip()
    if new_rows:
        out = pd.concat([out, pd.DataFrame(new_rows)], ignore_index=True)
    note('C4-components-without-c-p', len(new_rows),
         'c-p rows added for housing, gearBox, coolingSystem; housing material '
         'set to aluminium')

    # ---- C6 -------------------------------------------------------------
    # THE TORQUE RANGES COME FROM THE FLEET, not from the workbook.
    #
    # The consolidated description says torques per model are taken from the
    # EV Database. A later snapshot of that database (1438 models) says four
    # segments state a maximum the fleet does not contain -- C at 1100 Nm
    # against 600, A at 345 against 212 -- while several minima match to the
    # kilogram. So the lower bound was read from the database and the upper
    # bound was not.
    #
    # ⚠️ VEHICLE TOTAL, NOT PER MOTOR, and that is not a choice made here.
    # Testing both against the stated minima: the vehicle total matches in 4
    # of 11 segments, per-motor in 1 of 11, and segment JC matches the total
    # exactly at both ends, 220-770 Nm. The workbook is describing the whole
    # drive of a vehicle -- all its motors together -- and the masses agree:
    # Zenodo's stator lamination equals Drexler's per-machine mean times the
    # average number of motors in that segment, median ratio 1.08 across ten
    # segments. That is what the 1.5x offset always was.
    ranges = load_fleet_ranges(params)
    changed = 0
    for segment, (low, high, count) in ranges.items():
        mask = out.productKeyLevel3 == segment
        if not mask.any():
            continue
        out.loc[mask, 'torque_min'] = low
        out.loc[mask, 'torque_max'] = high
        out.loc[mask, 'torqueSource'] = f'EV Database, {count} models'
        changed += int(mask.sum())
    note('C6-torque-from-fleet', changed,
         'torque_min/max replaced with the observed p05-p95 range per '
         f'segment ({len(ranges)} segments)')

    # ---- C5 -------------------------------------------------------------
    mask = ((out.parameterCode == data.material_of_component) &
            (out.componentKeyLevel3 == 'conductiveBars'))
    out.loc[mask, 'materialKeyLevel0'] = 'non-ferrousMetals'
    out.loc[mask, 'materialKeyLevel1'] = 'AlAndAlAlloys'
    out.loc[mask, 'materialKeyLevel2'] = None
    out.loc[mask, 'corrected'] = (out.loc[mask, 'corrected'] + ' C5').str.strip()
    note('C5-conductive-bars-material', int(mask.sum()),
         'copper -> aluminium on the induction rotor cage')

    return out, pd.DataFrame(log)


# ========================================================== 6 TRAJECTORY
# ======================================================================

# Which floor and which rate a row follows, decided from the material it is
# made of and the component it sits in. Written as a function rather than a
# lookup so that the reasoning is visible: a shaft and a lamination stack are
# both steel and they do not change for the same reasons.
# ⚠️ THE MOTOR "TYPES" ARE DRIVE CONFIGURATIONS, NOT SINGLE MACHINES.
#
# Established 2026-09-18, from Matthias's rule and confirmed in the data: in a
# two-motor car one machine is a permanent-magnet machine, used all the time,
# and the second is an induction machine added when more power and torque are
# wanted. It is the Tesla layout and the dataset carries it directly --
# `IMandPMElectricMotors` is a CONFIGURATION, not a machine.
#
# The magnets prove it. Per vehicle, segment D:
#
#     PMElectricMotors        2.78 kg of magnet over an average of 1.44
#                             motors  ->  1.93 kg per machine
#     IMandPMElectricMotors   2.06 kg of magnet in a TWO-motor car
#
# A two-motor car carries LESS magnet than the single-motor category, and
# almost exactly one magnet rotor's worth: 2.06 / 1.93 = 1.07. Segments JC and
# JD give 0.86 and 0.89. So in every case the induction machine of the pair
# contributes no magnet at all, which is the whole point of pairing them.
#
# WHAT THIS MEANS FOR THE TRAJECTORY. A shift towards all-wheel drive does not
# multiply the magnet demand -- it adds iron and copper and leaves the magnet
# where it was. Any scenario that moves the fleet between these categories has
# to move whole configurations, not scale one machine.
MOTOR_CONFIGURATION = {
    'PMElectricMotors': 'one or more permanent-magnet machines',
    'EESMElectricMotors': 'externally excited, no magnet',
    'IMandPMElectricMotors': 'one permanent-magnet machine plus one induction '
                             'machine, the second added for power and torque',
}


def material_class(row) -> str:
    """The trajectory class of one row: lamination, copper, magnet, steel, aluminium."""
    sub = str(row.get('componentKeyLevel3') or '')
    material = str(row.get('materialKeyLevel1') or '')
    component = str(row.get('componentKeyLevel2') or '')

    if 'LaminationStack' in sub:
        return 'lamination'
    if material == 'rareEarthMetalsAndAlloys':
        return 'magnet'
    if material == 'CuAndCuAlloys':
        return 'copper'
    if material == 'AlAndAlAlloys':
        return 'aluminium'
    if material == 'steelAndSteelAlloys':
        return 'steel'
    # A component row names no material. It follows whatever dominates it.
    if component in ('housing', 'coolingSystem'):
        return 'aluminium'
    if component == 'gearBox':
        return 'steel'
    if component == 'stator':
        return 'lamination'
    if component == 'rotor':
        return 'steel'
    return 'steel'


def factor(year: int, klass: str, params: Params) -> float:
    """
    The mass at `year` as a share of the base-year mass.

        m(t) / m(2020) = floor + (1 - floor) * exp(-k (t - 2020))
        k = initial_rate / (1 - floor)

    `k` is set so the INITIAL SLOPE equals the measured annual rate: at
    t = base_year the derivative is -initial_rate, which is what Drexler
    observed. The floor is what stops it continuing forever.

    ⚠️ BEFORE THE BASE YEAR A DIFFERENT RULE APPLIES. This curve reversed is an
    exploding exponential -- at -7.6%/yr it makes a 2010 stator three times a
    2020 one, which no 2010 motor was. The measured rate is the rate DURING
    the hairpin transition, not a constant of nature, so the backcast uses its
    own slower constant rate:

        m(t) = m(2020) * (1 + backcast_rate) ** (2020 - t)

    Both directions are constructed. Neither is a reading.
    """
    scenario = params.scenario
    if year < scenario.base_year:
        rate = scenario.backcast_rate[klass]
        return float((1.0 + rate) ** (scenario.base_year - year))

    floor = scenario.floor[klass]
    rate = scenario.initial_rate[klass]
    if floor >= 1.0:
        return 1.0
    k = rate / (1.0 - floor)
    return floor + (1.0 - floor) * float(np.exp(-k * (year - scenario.base_year)))


def trajectory(frame: pd.DataFrame, params: Params) -> pd.DataFrame:
    """
    The composition for every year `run.years` asks for, and every voltage
    class in `scenario.conductor_diameter`.

    ⚠️ ONE OF THESE YEARS IS READ FROM A SOURCE. The rest is this function.
    Every row carries `yearBasis` -- measured, projected or backcast -- so that
    no figure can draw a measured and a constructed value in one colour without
    the code having had the chance to notice.

    THE UNCERTAINTY IS THE BASE YEAR'S, SCALED. It is not widened with distance
    from the measurement, which would be inventing a second uncertainty on top
    of the first and dressing a modelling choice as a statistical one. What a
    2070 value is uncertain about is whether the mechanism is right, and that
    is not a confidence interval -- it is `scenario.floor`, and it is tested by
    changing it.

    VOLTAGE ACTS ON COPPER ONLY, and directly on its MASS. Nothing else in the
    machine changes with the DC link voltage in this model -- which is a known
    omission, because insulation grows with voltage and is not carried here.
    """
    from src.params_schema import years_wanted

    years = years_wanted(params.run.years)
    value_columns = [c for c in ('meanValue', 'medianValue', 'modeValue',
                                 'STD', 'p025', 'p975') if c in frame.columns]

    base = frame.copy()
    # Computed once. Doing it per year and per voltage class was the same
    # answer 39 times over.
    base['materialClass'] = [material_class(row) for _, row in base.iterrows()]

    # ⚠️ TORQUE IS THE EXPLANATORY VARIABLE, and it was in the workbook all
    # along -- `torque_min` and `torque_max`, columns 42 and 43. Not using it
    # is what made every earlier figure unreadable: mass plotted against the
    # year shows the spread between vehicle SEGMENTS, which is size, and hides
    # the only thing being modelled, which is mass per unit of torque.
    base['torque'] = (base.torque_min + base.torque_max) / 2.0
    base['torqueSpan'] = base.torque_max - base.torque_min

    out = []
    for volts, copper_factor in params.scenario.copper_mass.items():
        for year in years:
            block = base.copy()
            block['productionYear'] = year
            block['voltageClass'] = volts
            factors = block.materialClass.map(
                lambda klass: factor(year, klass, params))
            # ⚠️ ONLY THE STATOR WINDING SCALES WITH THE DC LINK VOLTAGE.
            # The first version scaled every copper row, which quietly
            # included the EESM ROTOR winding -- and that winding is fed
            # through slip rings from a separate excitation circuit, not from
            # the DC link. Raising the traction voltage from 400 V to 800 V
            # does not change the field winding's current at all, so its
            # copper must not move with it.
            scales = ((block.materialClass == 'copper') &
                      (block.componentKeyLevel2 == 'stator'))
            factors = factors * np.where(scales, copper_factor, 1.0)
            block['trajectoryFactor'] = factors
            for column in value_columns:
                block[column] = block[column] * factors
            # The figure that matters: kg per Nm. A mass without its torque is
            # not comparable to anything.
            block['massPerTorque'] = block.meanValue / block.torque
            measured = params.data.year_is_measured(year)
            block['yearIsMeasured'] = measured
            block['yearBasis'] = (
                'measured' if measured else
                ('backcast' if year < params.scenario.base_year else 'projected'))
            out.append(block)

    return pd.concat(out, ignore_index=True)



# ============================================================= 7 FIGURES
# ======================================================================
# Colours by MATERIAL, not by component, because the question these figures
# answer is which materials a fleet of motors will need.
MATERIAL_COLOUR = {
    'lamination': '#5B7C99',
    'copper': '#B5651D',
    'magnet': '#8E44AD',
    'steel': '#7F8C8D',
    'aluminium': '#16A085',
}
MATERIAL_LABEL = {
    'lamination': 'Elektroblech (Blechpaket)',
    'copper': 'Kupfer',
    'magnet': 'Magnet (NdFeB)',
    'steel': 'Stahl (Welle, Getriebe)',
    'aluminium': 'Aluminium (Gehäuse, Kühlung)',
}


def _mark_measured(axis, params, years):
    """
    Shade the years a source actually covers.

    THE MOST IMPORTANT THING ON THE FIGURE. A source covers 2018-2023 and
    nothing else; everything to the right is a curve somebody chose. A reader
    who cannot see that distinction is being misled by a plot that is
    otherwise correct.

    Drawn as a BAND and not as lines, because a line per measured year says
    "four measurements" when what exists is one window.
    """
    covered = [entry.get('covers') for entry in params.data.declared('data').values()
               if entry.get('covers')]
    if not covered:
        return
    first = min(window[0] for window in covered)
    last = max(window[1] for window in covered)
    axis.axvspan(first, last, color='#C0392B', alpha=0.10, zorder=0, lw=0)
    axis.axvline(first, color='#C0392B', lw=1.0, alpha=0.5, zorder=1)
    axis.axvline(last, color='#C0392B', lw=1.0, alpha=0.5, zorder=1)


MOTOR_LABEL = {
    'PMElectricMotors': 'PMSM  (Permanentmagnet)',
    'EESMElectricMotors': 'EESM  (fremderregt)',
    'IMandPMElectricMotors': 'IM + PM  (Asynchron)',
    'axialFluxPMElectricMotors': 'Axialfluss  (YASA-Typ)',
    'dualRotorRadialPMElectricMotors': 'Doppelrotor radial  (DeepDrive)',
}


def figure_factors(params, out_path: str, current: pd.DataFrame = None) -> str:
    """
    Mass against torque, one row per MOTOR TYPE, one curve per year.

    ⚠️ ONE REGRESSION FOR ALL TOPOLOGIES IS WRONG, and an earlier version did
    that. The three machines do not put their mass in the same places: an EESM
    carries a wound rotor field instead of magnets, an induction rotor carries
    a cage, and Drexler measures the difference directly -- rotor lamination
    averages 13.75 kg for IM, 11.34 kg for EESM and 10.11 kg for PMSM. Fitting
    them together produces a line describing no machine that exists.

    So each topology gets its own fit, its own points and its own family of
    year curves. What can then be compared across a row is the SLOPE: how many
    grams of a material each machine needs per Nm of torque.
    """
    import matplotlib.pyplot as plt

    if current is None:
        raise ValueError('figure_factors needs the current composition')

    columns = [
        ('Stator-Blechpaket', 'lamination',
         lambda f: f.componentKeyLevel3 == 'statorSheetLaminationStack'),
        ('Stator-Wicklung (Kupfer)', 'copper',
         lambda f: ((f.componentKeyLevel2 == 'stator') &
                    (f.componentKeyLevel3 == 'windings'))),
        ('Rotor-Blechpaket', 'lamination',
         lambda f: f.componentKeyLevel3 == 'rotorSheetLaminationStack'),
    ]
    show_years = [params.scenario.base_year, 2030, 2050, 2070]
    shades = ['#1a1a1a', '#4a6fa5', '#7aa6c2', '#b3cede']
    # A torque every one of the three topologies actually covers, so the
    # comparison is an interpolation for all of them and an extrapolation for
    # none.
    REFERENCE_TORQUE = 500.0

    base = current[(current.voltageClass == params.scenario.base_voltage) &
                   (current.productionYear == params.scenario.base_year) &
                   (current.parameterCode == params.data.material_of_component)]
    motors = [m for m in params.run.motors if m in set(base.componentKeyLevel1)]

    figure, axes = plt.subplots(len(motors), len(columns),
                                figsize=(5.1 * len(columns), 3.5 * len(motors)),
                                squeeze=False)

    for row_index, motor in enumerate(motors):
        for column_index, (title, klass, picker) in enumerate(columns):
            axis = axes[row_index][column_index]
            colour = MATERIAL_COLOUR[klass]

            block = base[(base.componentKeyLevel1 == motor) & picker(base) &
                         base.torque_min.notna() & base.meanValue.notna()].copy()
            if block.empty:
                axis.text(0.5, 0.5, 'keine Daten', ha='center', va='center',
                          transform=axis.transAxes, fontsize=9, color='#999999')
                axis.set_xticks([])
                axis.set_yticks([])
                continue
            block['torque'] = (block.torque_min + block.torque_max) / 2.0

            # An intercept needs three points, not four: a machine of zero
            # torque still has a shaft, end plates and a housing, so forcing
            # the line through the origin asserts something false about every
            # small machine. The induction fit has n=3 and gets an intercept
            # like the others.
            slope, intercept = np.polyfit(block.torque, block.meanValue, 1)
            span = np.linspace(0, block.torque.max() * 1.08, 40)

            for colour_year, year in zip(shades, show_years):
                scale = (factor(year, klass, params) /
                         factor(params.scenario.base_year, klass, params))
                axis.plot(span, (intercept + slope * span) * scale, lw=2.0,
                          color=colour_year,
                          label=str(year) if column_index == 0 and row_index == 0
                          else None)

            axis.plot(block.torque, block.meanValue, 'o', ms=6, mfc='white',
                      mec=colour, mew=1.6, ls='none', zorder=6)
            # ⚠️ THE SLOPES ARE NOT COMPARABLE ACROSS TOPOLOGIES. A fit with
            # an intercept and a fit through the origin put the same machine's
            # mass into different coefficients: the induction fit reads
            # 50.5 g/Nm against 35.8 for PMSM, which looks like +41% and is
            # +8% at 500 Nm once the 5.5 kg intercept is counted. So the panel
            # states the MASS AT A REFERENCE TORQUE, which is comparable
            # whatever shape the fit has.
            at_reference = intercept + slope * REFERENCE_TORQUE
            axis.annotate(f'{at_reference:.1f} kg bei {REFERENCE_TORQUE:.0f} Nm',
                          xy=(0.04, 0.93), xycoords='axes fraction',
                          fontsize=9, color=colour, va='top', weight='bold')
            axis.annotate(f'Fit: {slope * 1000:.1f} g/Nm'
                          + (f' + {intercept:.1f} kg' if intercept
                             else ' (durch Ursprung)'),
                          xy=(0.04, 0.845), xycoords='axes fraction',
                          fontsize=7.5, color='#777777', va='top')
            axis.plot([REFERENCE_TORQUE], [at_reference], marker='*', ms=13,
                      color='#C0392B', zorder=8)
            axis.annotate(f'n={len(block)}', xy=(0.96, 0.06),
                          xycoords='axes fraction', fontsize=7.5,
                          color='#888888', ha='right')

            if row_index == 0:
                axis.set_title(title, fontsize=11)
            if row_index == len(motors) - 1:
                axis.set_xlabel('Drehmoment [Nm]')
            if column_index == 0:
                axis.set_ylabel(f'{MOTOR_LABEL.get(motor, motor)}\nkg je Motor',
                                fontsize=9)
            axis.set_ylim(bottom=0)
            axis.set_xlim(left=0)
            axis.grid(alpha=0.22, lw=0.6)

    handles, labels = axes[0][0].get_legend_handles_labels()
    figure.legend(handles, labels, loc='lower center', ncol=len(show_years),
                  fontsize=9.5, frameon=False, title='Jahr',
                  bbox_to_anchor=(0.5, -0.008))
    figure.suptitle('Masse gegen Drehmoment, je Motortyp und Jahr \u2014 '
                    'gleiches Drehmoment, weniger Material.\n'
                    'Vergleichbar ist der rote Stern: Masse bei 500 Nm. '
                    'Die Fit-Koeffizienten sind es NICHT \u2014 '
                    'IM ist durch den Ursprung gefittet (n=3).', fontsize=11.5)
    figure.tight_layout(rect=(0, 0.045, 1, 1))
    figure.savefig(out_path, dpi=160)
    plt.close(figure)
    return out_path


def figure_motor_mass(frame: pd.DataFrame, params, out_path: str) -> str:
    """
    The composition of each motor type over time -- the stock-and-flow output.

    ONE PANEL PER MOTOR TYPE, materials stacked, 2020 to 2070. This is what
    the stock-and-flow model multiplies a fleet by, so it is drawn the way it
    will be used: kilograms per vehicle, by material, per year.

    ⚠️ SEGMENT D, because it is the only segment all three radial topologies
    share. PMSM and EESM cover A-F and JB-JE; the induction machine appears in
    D, JC and JD only. Picking C would have silently dropped the induction
    machine, which an earlier version of this figure did.

    ⚠️ THE AXIAL MACHINES HAVE NO COMPOSITION AND ARE NOT DRAWN HERE. Their
    makers publish a whole-machine mass and nothing about what is inside it,
    so a stacked bar for them would be invention. They appear in
    04_topologies.png as the single number they actually are.
    """
    import matplotlib.pyplot as plt

    segment = 'D'
    rows = frame[(frame.productKeyLevel3 == segment) &
                 (frame.voltageClass == params.scenario.base_voltage) &
                 (frame.parameterCode == params.data.material_of_component) &
                 (frame.productionYear >= params.scenario.base_year)]
    motors = [m for m in params.run.motors if m in set(rows.componentKeyLevel1)]
    if not motors:
        motors = sorted(set(rows.componentKeyLevel1))

    figure, axes = plt.subplots(1, len(motors),
                                figsize=(4.9 * len(motors), 5.4), sharey=True,
                                squeeze=False)
    axes = axes[0]

    for axis, motor in zip(axes, motors):
        block = rows[rows.componentKeyLevel1 == motor]
        pivot = block.pivot_table(index='productionYear', columns='materialClass',
                                  values='meanValue', aggfunc='sum').fillna(0.0)
        order = [k for k in MATERIAL_COLOUR if k in pivot.columns]
        axis.stackplot(pivot.index, *[pivot[k] for k in order],
                       colors=[MATERIAL_COLOUR[k] for k in order],
                       labels=[MATERIAL_LABEL[k] for k in order], alpha=0.92)

        first, last = pivot.sum(axis=1).iloc[0], pivot.sum(axis=1).iloc[-1]
        axis.annotate(f'{first:.0f} kg', xy=(pivot.index[0], first),
                      xytext=(4, 6), textcoords='offset points', fontsize=9,
                      weight='bold')
        axis.annotate(f'{last:.0f} kg\n({last / first - 1:+.0%})',
                      xy=(pivot.index[-1], last), xytext=(-40, 8),
                      textcoords='offset points', fontsize=9, weight='bold')

        unreliable = block[block.get('reliability', '') == 'unreliable'] \
            if 'reliability' in block.columns else block.iloc[0:0]
        title = MOTOR_LABEL.get(motor, motor)
        if not unreliable.empty:
            title += '\n⚠ enthält eine als unsicher markierte Masse'
        axis.set_title(title, fontsize=10.5)
        axis.set_xlabel('Jahr')
        axis.grid(alpha=0.22, lw=0.6)

    axes[0].set_ylabel(f'kg je Fahrzeug, Segment {segment}')
    handles, labels = axes[0].get_legend_handles_labels()
    figure.legend(handles, labels, loc='lower center', ncol=5, fontsize=9,
                  frameon=False, bbox_to_anchor=(0.5, -0.012))
    figure.suptitle(
        f'Zusammensetzung je Motortyp über die Zeit, Segment {segment}, '
        f'{params.scenario.base_voltage} V \u2014 Eingang für das '
        f'Stock-and-Flow-Modell\n'
        'Nur 2020 ist gemessen; alles danach folgt scenario.floor und '
        'scenario.initial_rate', fontsize=11.5)
    figure.tight_layout(rect=(0, 0.055, 1, 1))
    figure.savefig(out_path, dpi=160)
    plt.close(figure)
    return out_path


def figure_critical(frame: pd.DataFrame, params, out_path: str) -> str:
    """
    Copper by voltage class, and magnet by motor type.

    ⚠️ THE FIRST VERSION OF THIS FIGURE SUMMED OVER VOLTAGE CLASSES, which
    added the 400 V, 800 V and 1000 V variants of the same motor together and
    reported 9.2 kg of copper where the 400 V machine has 7.8 kg. A variant is
    an alternative, not a part. Filtered now, and the left panel shows the
    variants as what they are.
    """
    import matplotlib.pyplot as plt

    rows = frame[(frame.productKeyLevel3 == 'C') &
                 (frame.parameterCode == params.data.material_of_component) &
                 (frame.productionYear >= params.scenario.base_year)]
    figure, axes = plt.subplots(1, 2, figsize=(13, 5.4))

    # ---- copper, by voltage class, one motor type -----------------------
    axis = axes[0]
    copper = rows[(rows.materialClass == 'copper') &
                  (rows.componentKeyLevel1 == 'PMElectricMotors')]
    shades = {400: '#B5651D', 800: '#D99058', 1000: '#E8BFA0'}
    for volts, group in copper.groupby('voltageClass'):
        series = group.groupby('productionYear')['meanValue'].sum()
        ratio = params.scenario.copper_mass[volts]
        axis.plot(series.index, series.values, lw=2.4,
                  color=shades.get(volts, '#B5651D'),
                  label=f'{volts} V   Kupfermasse {ratio:.0%} von 400 V')
    _mark_measured(axis, params, sorted(set(rows.productionYear)))
    axis.set_title('Kupfer je Spannungsklasse, PMSM', fontsize=11.5)
    axis.set_ylim(bottom=0)
    axis.set_ylabel('kg je Motor, Segment C')

    # ---- magnet and rare earth, by motor type ---------------------------
    axis = axes[1]
    magnet = rows[(rows.materialClass == 'magnet') &
                  (rows.voltageClass == params.scenario.base_voltage)]
    for motor, group in magnet.groupby('componentKeyLevel1'):
        series = group.groupby('productionYear')['meanValue'].sum()
        if series.sum() == 0:
            continue
        unreliable = bool((group.get('reliability', pd.Series(dtype=str))
                           == 'unreliable').any())
        axis.plot(series.index, series.values, lw=2.4,
                  ls='--' if unreliable else '-',
                  label=motor + (' \u2014 Masse unsicher' if unreliable else ''))
    _mark_measured(axis, params, sorted(set(rows.productionYear)))
    axis.set_title('Seltene Erden (Magnet) je Motortyp', fontsize=11.5)
    axis.set_ylim(bottom=0)
    axis.set_ylabel('kg je Motor, Segment C')

    for axis in axes:
        axis.set_xlabel('Jahr')
        axis.legend(fontsize=9, framealpha=0.95)
        axis.grid(alpha=0.22, lw=0.6)

    figure.suptitle('Kritische Werkstoffe je Motor \u2014 '
                    'rot hinterlegt: von Quellen gedeckt, sonst konstruiert',
                    fontsize=12.5)
    figure.tight_layout()
    figure.savefig(out_path, dpi=160)
    plt.close(figure)
    return out_path


def _regression_band(block: pd.DataFrame, params, span, draws: int = 0):
    """
    A regression and its uncertainty band, from DRAWS rather than from formulae.

    ⚠️ THE BAND IS NOT A TEXTBOOK CONFIDENCE INTERVAL. Each segment's mass is
    itself uncertain -- the consolidated dataset gives p025 and p975 for every
    row -- so the line is refitted on every draw and the band is the
    percentiles OF THE FITTED LINES. Fitting once to the means and putting a
    formula's interval around it would describe scatter between segments and
    ignore the uncertainty the source actually states.

    Component masses within one motor are drawn with the same shared shock at
    `monte_carlo.within_motor_correlation`, for the reason given there: they
    are regressions on the same vehicle's torque and move together.

    `draws` defaults to `monte_carlo.draws`: the solve is batched, so the full
    200,000 costs little more than a small sample would.
    """
    draws = draws or params.monte_carlo.draws
    rng = np.random.default_rng(params.monte_carlo.seed)
    rho = params.monte_carlo.within_motor_correlation

    torques = np.sort(block.torque.unique())
    totals = np.zeros((draws, len(torques)))
    shock = rng.standard_normal(draws)          # shared across the whole motor

    for index, torque in enumerate(torques):
        rows = block[block.torque == torque]
        for _, row in rows.iterrows():
            if pd.isna(row.p025) or pd.isna(row.p975) or row.p975 == row.p025:
                totals[:, index] += float(row.meanValue)
                continue
            values, _ = _draw(row.meanValue, row.p025, row.p975, draws, rng,
                              correlated_with=shock, correlation=rho)
            totals[:, index] += values

    # One least squares solve for every draw at once.
    design = np.column_stack([np.ones_like(torques), torques])
    projection = design @ np.linalg.inv(design.T @ design)
    beta = totals @ projection                                  # (draws, 2)
    lines = beta[:, 0:1] + beta[:, 1:2] * span[None, :]         # (draws, span)

    return (np.median(lines, axis=0),
            np.percentile(lines, 2.5, axis=0),
            np.percentile(lines, 97.5, axis=0),
            torques, totals.mean(axis=0))


def figure_topologies(current: pd.DataFrame, params, out_path: str) -> str:
    """
    Every machine with a published mass, against shaft torque, with bands.

    ONE AXIS, AND IT IS SHAFT TORQUE. Whether a reduction follows is a
    property of the machine, not a reason for a second figure.

    ⚠️ LINEAR AXES, DELIBERATELY. An earlier version used a log torque axis,
    and a straight line on a log axis LOOKS LIKE A CURVE -- which made the
    linear regressions appear to be fitted curves. Two linear panels instead:
    the left one over the range the consolidated data actually covers, the
    right one wide enough to hold the high-torque machines.

    ⚠️ THE MANUFACTURER POINTS HAVE NO BAND because they have no stated
    uncertainty. A data sheet gives one number. Drawing an interval around it
    would be inventing one.
    """
    import matplotlib.pyplot as plt

    base = current[(current.voltageClass == params.scenario.base_voltage) &
                   (current.productionYear == params.scenario.base_year) &
                   (current.parameterCode == params.data.material_of_component) &
                   (current.componentKeyLevel2 != 'gearBox')]

    figure, axes = plt.subplots(1, 2, figsize=(15, 6.2))
    colours = {'PMElectricMotors': '#8E44AD', 'EESMElectricMotors': '#2980B9',
               'IMandPMElectricMotors': '#16A085'}
    styles = {'axialFluxPM': ('*', '#C0392B', 'Axialfluss'),
              'axialFluxPM in-wheel': ('P', '#E67E22', 'Axialfluss, Radnabe'),
              'dualRotorRadialPM': ('^', '#D35400', 'Doppelrotor radial')}
    limit = 0.0

    for axis_index, axis in enumerate(axes):
        for motor in params.run.motors:
            block = base[base.componentKeyLevel1 == motor].dropna(
                subset=['meanValue', 'torque_min']).copy()
            if block.empty:
                continue
            block['torque'] = (block.torque_min + block.torque_max) / 2.0
            low_t, high_t = block.torque.min(), block.torque.max()
            limit = max(limit, high_t)
            span = np.linspace(low_t * 0.9, high_t, 40)
            median, low, high, torques, means = _regression_band(
                block, params, span)
            colour = colours.get(motor, '#7F8C8D')
            axis.fill_between(span, low, high, color=colour, alpha=0.17, lw=0)
            axis.plot(span, median, lw=2.4, color=colour,
                      label=(f'{MOTOR_LABEL.get(motor, motor)}, radial'
                             if axis_index == 0 else None))
            axis.plot(torques, means, 'o', ms=5.5, mfc='white', mec=colour,
                      mew=1.4, ls='none')

        for topology, group in machines().groupby('topology'):
            marker, colour, label = styles.get(topology, ('s', '#555', topology))
            for certain, part in group.groupby('scope_certain'):
                axis.plot(part.torque_shaft, part.mass_kg, marker, ms=13,
                          color=colour if certain else 'white',
                          mec=colour, mew=1.8, ls='none', zorder=8,
                          label=(f'{label}'
                                 + ('' if certain else ', Umfang unklar')
                                 if axis_index == 1 else None))
            for _, row in group.iterrows():
                drop = -25 if str(row['name']).endswith('P400 R') else -11
                axis.annotate(
                    f'{str(row["name"]).replace("Equipmake ", "").replace("DeepDrive ", "").replace("Donut Lab ", "")}  '
                    f'{row.mass_kg:.0f} kg',
                    xy=(row.torque_shaft, row.mass_kg), xytext=(8, drop),
                    textcoords='offset points', fontsize=7.8, color=colour)

        axis.set_xlabel('Drehmoment an der Motorwelle [Nm]')
        axis.set_ylabel('Masse ohne Getriebe [kg]')
        axis.set_ylim(0, None)
        axis.grid(alpha=0.22, lw=0.6)
        axis.legend(fontsize=8.5, framealpha=0.95, loc='upper left')

    axes[0].set_xlim(0, limit * 1.05)
    axes[0].set_title(f'Bereich der Datenbasis, bis {limit:.0f} Nm',
                      fontsize=11.5)
    axes[1].set_xlim(0, 4600)
    axes[1].axvspan(limit, 4600, color='#000000', alpha=0.05, lw=0)
    axes[1].set_title('Gesamtbild \u2014 grau: jenseits der Datenbasis',
                      fontsize=11.5)

    figure.suptitle(
        'Alle Maschinen mit veröffentlichter Masse, gegen Wellendrehmoment.  '
        'Getriebe überall ausgeschlossen.\n'
        'Bänder: 95% aus Monte-Carlo-Ziehungen, Regression je Ziehung neu '
        'gefittet.  Herstellerpunkte haben keine angegebene Unsicherheit.',
        fontsize=11.5)
    figure.tight_layout()
    figure.savefig(out_path, dpi=160)
    plt.close(figure)
    return out_path


def figure_fleet(params, out_path: str) -> str:
    """
    What the fleet actually asks of its motors, and how that changed.

    THE QUESTION THIS ANSWERS. Every mass in this project is a regression on
    torque, and the whole trajectory says "same torque, less material". That
    claim is only worth anything if the torque really does stay the same. This
    figure checks it against 1438 models.

    ⚠️ MEDIANS WITHIN A SEGMENT, NOT ACROSS THE FLEET. A fleet-wide median
    moves when the model mix moves: the 2015 fleet was a handful of premium
    cars and the 2017 fleet was small hatchbacks, so a fleet median swings
    from 482 to 225 Nm between them and says nothing about engineering. Held
    within a segment, and only where at least five models support the point.
    """
    import matplotlib.pyplot as plt

    frame = load(params, 'evdatabase')
    frame = frame[frame.year.between(2020, 2026) & frame.torque_nm.notna()]
    segments = ['B', 'C', 'D', 'F', 'JB', 'JC', 'JD']
    colours = plt.get_cmap('tab10')

    figure, axes = plt.subplots(1, 2, figsize=(14, 5.6))
    for axis, (column, label) in zip(axes, [
            ('torque_per_motor', 'Drehmoment je Motor [Nm]'),
            ('power_per_motor', 'Leistung je Motor [kW]')]):
        for index, segment in enumerate(segments):
            block = frame[frame.segment == segment]
            counts = block.groupby('year')[column].count()
            medians = block.groupby('year')[column].median().where(counts >= 5)
            medians = medians.dropna()
            if len(medians) < 3:
                continue
            axis.plot(medians.index, medians.values, 'o-', ms=5, lw=2,
                      color=colours(index), label=f'{segment} (n={len(block)})')
        axis.set_xlabel('Jahr des Markteintritts')
        axis.set_ylabel(label)
        axis.set_ylim(bottom=0)
        axis.grid(alpha=0.25, lw=0.6)
        axis.legend(fontsize=8, ncol=2, framealpha=0.95, loc='lower right')

    axes[0].set_title('Drehmoment je Motor: weitgehend flach',
                      fontsize=11.5)
    axes[1].set_title('Leistung je Motor: leicht steigend, nicht überall',
                      fontsize=11.5)
    figure.suptitle(
        'Was die Flotte von ihren Motoren verlangt, EV Database, 1438 Modelle\n'
        'Median je Segment, nur wo mindestens 5 Modelle das Jahr tragen',
        fontsize=12)
    figure.tight_layout()
    figure.savefig(out_path, dpi=160)
    plt.close(figure)
    return out_path


# ================================================= 8 COMPOSITION BY TORQUE
# ======================================================================
def composition_by_torque(frame: pd.DataFrame, params: Params) -> pd.DataFrame:
    """
    The composition as a function of TORQUE and YEAR, with no segment in it.

    ⚠️ SEGMENTS ARE HOW THE SOURCE WAS AGGREGATED, NOT WHAT DRIVES THE MASS.
    Matthias 2026-09-18. A segment is a market category: it says what kind of
    car it is, not what the motor has to do. The same segment holds 180 Nm and
    600 Nm cars, and two cars in different segments with the same torque need
    the same machine. So the segments are used to FIT the relationship and
    then dropped.

    For every configuration and every material, mass against torque is fitted
    across the segments, and the fit is evaluated on `run.torque_grid` and
    scaled by the year factor. The stock-and-flow model then asks for a torque
    and a year and gets kilograms -- with no segment to decide and no question
    about which segment a 2060 vehicle belongs to.

    THE UNCERTAINTY IS DRAWN, as everywhere else: the fit is repeated on every
    draw and the reported interval is the percentiles of the fitted values.

    ⚠️ `n_segments` AND `torque_low`/`torque_high` TRAVEL WITH EVERY ROW. A
    grid point outside the range the fit was made on is an extrapolation, and
    the consumer has to be able to see that without re-deriving it.
    """
    from src.params_schema import years_wanted

    grid = np.array(years_wanted(params.run.torque_grid), dtype=float)
    years = years_wanted(params.run.years)
    rng = np.random.default_rng(params.monte_carlo.seed)
    rho = params.monte_carlo.within_motor_correlation
    draws = params.monte_carlo.draws

    # ⚠️ THE CORRECTED BASE FRAME, NOT THE TRAJECTORY. The trajectory already
    # holds one block per voltage class, and grouping it without the voltage
    # key silently adds the 400 V, 800 V and 1000 V variants of the same
    # vehicle together -- which reported 313 kg at 500 Nm where the answer is
    # about 104. A variant is an alternative, not a part. This function
    # applies the voltage and the year itself, so it must be given the base.
    if 'voltageClass' in frame.columns and frame.voltageClass.nunique() > 1:
        raise ValueError(
            'composition_by_torque expects the corrected base composition, '
            'not the trajectory: it applies voltage and year itself, and a '
            'frame carrying several voltage classes would be counted once per '
            'class.')

    frame = frame.copy()
    if 'materialClass' not in frame.columns:
        frame['materialClass'] = [material_class(row)
                                  for _, row in frame.iterrows()]

    material = frame[frame.parameterCode == params.data.material_of_component]
    rows: list[dict] = []

    keys = ['componentKeyLevel1', 'componentKeyLevel2', 'componentKeyLevel3',
            'materialKeyLevel1', 'materialClass']

    # ⚠️ TWO PASSES, BECAUSE A SLOPE CAN BE BORROWED. Configurations with
    # enough segments are fitted first and their per-draw slopes kept; a
    # configuration below run.min_segments_for_slope then takes the mean of
    # those slopes for the same component and material, and fits only its own
    # level. Matthias 2026-09-18: IM+PM should use the slope of the other two.
    donors: dict[tuple, list] = {}
    prepared = []
    for key, block in material.groupby(keys, dropna=False):
        block = block.dropna(subset=['meanValue', 'torque_min']).copy()
        if block.empty:
            continue
        block['torque'] = (block.torque_min + block.torque_max) / 2.0
        points = block.groupby('torque')['meanValue'].mean()
        if len(points) < 2:
            continue
        prepared.append((key, block, np.asarray(points.index, dtype=float)))

    # Enough segments first, so their slopes exist when the others need them.
    prepared.sort(key=lambda item: -len(item[2]))

    for key, block, torques in prepared:
        enough = len(torques) >= params.run.min_segments_for_slope
        donor_key = (key[1], key[2], key[4])       # component, sub, material

        shock = rng.standard_normal(draws)
        sampled = np.zeros((draws, len(torques)))
        for index, torque in enumerate(torques):
            for _, row in block[block.torque == torque].iterrows():
                if pd.isna(row.p025) or row.p975 == row.p025:
                    sampled[:, index] += float(row.meanValue)
                else:
                    values, _ = _draw(row.meanValue, row.p025, row.p975,
                                      draws, rng, correlated_with=shock,
                                      correlation=rho)
                    sampled[:, index] += values

        # ⚠️ THE BAND IS THE UNCERTAINTY OF THE FIT, not of the values.
        # Matthias 2026-09-18. Drawing the source's own intervals and
        # refitting gives a band of about 1%, while the points scatter 8%
        # around the line -- because that band only carries how uncertain each
        # value is, and not how badly a straight line in torque describes
        # them. A user asking "what does a 700 Nm machine weigh" needs the
        # second one.
        #
        # So the segments are BOOTSTRAPPED as well: each draw resamples them
        # with replacement and refits. A draw that happens to miss the
        # segments pinning one end gets a visibly different line, which is
        # exactly the uncertainty a fit on eleven points really has, and it
        # widens towards the ends of the range where there is least to hold
        # the line down.
        # ⚠️ VECTORISED, BECAUSE 200,000 DRAWS EACH REFIT A REGRESSION.
        # A Python loop over the draws was fine at 5000 and is not at
        # 200,000. The bootstrap fit is solved for every draw at once through
        # the normal equations: build X'X and X'y per draw with einsum, then
        # one batched solve. Same arithmetic, three orders of magnitude
        # faster.
        picks = rng.integers(0, len(torques), size=(draws, len(torques)))
        picked_torque = torques[picks]                       # (draws, n)
        picked_value = np.take_along_axis(sampled, picks, axis=1)

        design = np.stack([np.ones_like(picked_torque), picked_torque], axis=2)
        gram = np.einsum('dni,dnj->dij', design, design)
        moment = np.einsum('dni,dn->di', design, picked_value)

        # A resample can land on one torque, leaving the system singular.
        # Those draws fall back to the mean, which is what a single point
        # supports.
        spread = picked_torque.max(axis=1) - picked_torque.min(axis=1)
        usable = spread > 0
        beta = np.zeros((draws, 2))
        if usable.any():
            # moment must be a batch of COLUMN vectors, not one matrix.
            beta[usable] = np.linalg.solve(
                gram[usable], moment[usable][..., None])[..., 0]
        if (~usable).any():
            beta[~usable, 0] = picked_value[~usable].mean(axis=1)

        if enough:
            donors.setdefault(donor_key, []).append(beta[:, 1])
        else:
            # ⚠️ SLOPE BORROWED. The level stays this configuration's own --
            # its points fix where it sits -- and only the climb is taken
            # from the configurations that have enough segments to establish
            # one, per draw so the donors' own uncertainty travels with it.
            pool = donors.get(donor_key)
            if pool:
                borrowed = np.mean(np.stack(pool, axis=0), axis=0)
                level = sampled.mean(axis=1)
                centre = torques.mean()
                beta = np.column_stack([level - borrowed * centre, borrowed])

        fitted = beta[:, 0:1] + beta[:, 1:2] * grid[None, :]
        slope_borrowed = not enough and bool(donors.get(donor_key))

        median = np.median(fitted, axis=0)
        low = np.percentile(fitted, 2.5, axis=0)
        high = np.percentile(fitted, 97.5, axis=0)

        motor, component, sub, material_key, klass = key
        for volts, copper_factor in params.scenario.copper_mass.items():
            voltage_scale = (copper_factor
                             if (klass == 'copper' and component == 'stator')
                             else 1.0)
            for year in years:
                scale = factor(year, klass, params) * voltage_scale
                for index, torque in enumerate(grid):
                    rows.append({
                        'componentKeyLevel1': motor,
                        'componentKeyLevel2': component,
                        'componentKeyLevel3': sub,
                        'materialKeyLevel1': material_key,
                        'materialClass': klass,
                        'torque_nm': torque,
                        'productionYear': year,
                        'voltageClass': volts,
                        'meanValue': max(0.0, median[index] * scale),
                        'p025': max(0.0, low[index] * scale),
                        'p975': max(0.0, high[index] * scale),
                        'yearBasis': ('measured'
                                      if params.data.year_is_measured(year)
                                      else ('backcast'
                                            if year < params.scenario.base_year
                                            else 'projected')),
                        'n_segments': len(torques),
                        'slope_borrowed': slope_borrowed,
                        'torque_low': torques.min(),
                        'torque_high': torques.max(),
                        'extrapolated': bool(torque < torques.min()
                                             or torque > torques.max()),
                    })

    result = pd.DataFrame(rows)
    spec = _spec_by_torque(result, params)
    if not spec.empty:
        result = pd.concat([result, spec], ignore_index=True)
    return result


def _spec_by_torque(radial: pd.DataFrame, params: Params) -> pd.DataFrame:
    """
    The newer machines on the same grid, from a data sheet and a split.

    THE DATA SHEET GIVES THE TOTAL, THE SPLIT COMES FROM `spec_composition`.
    Nothing is invented: if `shares` is empty the machine is skipped and the
    composition tables simply do not contain it, which is the honest state
    while no source says what is inside it.

    ⚠️ THE TORQUE DEPENDENCE IS BORROWED, and shaped rather than sloped. One
    machine cannot carry a slope. With `torque_slope_from='radial'` the radial
    total curve is SCALED THROUGH the anchor point -- m(T) = m_radial(T) x
    anchor / m_radial(T_anchor) -- rather than given the radial slope with a
    new intercept, which produced a negative mass below 130 Nm when it was
    tried on the topology figure. Scaling keeps the shape and cannot go
    negative.
    """
    from src.params_schema import years_wanted

    configured = {name: entry for name, entry in params.run.spec_composition.items()
                  if entry.get('shares')}
    if not configured:
        return pd.DataFrame()

    grid = np.array(years_wanted(params.run.torque_grid), dtype=float)
    years = years_wanted(params.run.years)
    sheets = machines().set_index('name')

    # The radial total, as the shape to borrow.
    radial_total = radial[(radial.productionYear == params.scenario.base_year) &
                          (radial.voltageClass == params.scenario.base_voltage) &
                          (radial.componentKeyLevel1 == 'PMElectricMotors')]
    shape = radial_total.groupby('torque_nm')['meanValue'].sum()

    rows = []
    for motor, entry in configured.items():
        anchor_name = entry.get('anchor')
        if anchor_name not in sheets.index:
            continue
        anchor = sheets.loc[anchor_name]
        anchor_torque = float(anchor.torque_shaft)
        anchor_mass = float(anchor.mass_kg)

        slope = entry.get('torque_slope_from')
        if slope == 'radial':
            at_anchor = float(np.interp(anchor_torque, shape.index, shape.values))
            totals = np.interp(grid, shape.index, shape.values) * \
                (anchor_mass / at_anchor) if at_anchor else np.zeros_like(grid)
        else:
            totals = float(slope) * grid

        # ⚠️ THE INTERVAL, AND WHY IT IS NOT ZERO. A data sheet states one
        # number, so there is no published interval -- which is not the same
        # as no uncertainty. These are the least certain numbers here.
        #
        # Two parts, combined in quadrature. The borrowed SHAPE inherits the
        # radial fit's own relative width at that torque, which already grows
        # away from the radial data. The derived SHARES carry
        # spec_share_uncertainty. Neither is measured, and both are declared.
        radial_band = radial_total.groupby('torque_nm')[['meanValue', 'p025',
                                                         'p975']].sum()
        shape_rel = np.interp(
            grid, radial_band.index,
            ((radial_band.p975 - radial_band.p025) /
             (2 * radial_band.meanValue)).values)
        width = np.sqrt(shape_rel ** 2 +
                        params.run.spec_share_uncertainty ** 2)

        for klass, share in entry['shares'].items():
            for volts, copper_factor in params.scenario.copper_mass.items():
                voltage_scale = copper_factor if klass == 'copper' else 1.0
                for year in years:
                    scale = factor(year, klass, params) * voltage_scale * share
                    for index, torque in enumerate(grid):
                        rows.append({
                            'componentKeyLevel1': motor,
                            'componentKeyLevel2': '(not resolved)',
                            'componentKeyLevel3': None,
                            'materialKeyLevel1': None,
                            'materialClass': klass,
                            'torque_nm': torque,
                            'productionYear': year,
                            'voltageClass': volts,
                            'meanValue': totals[index] * scale,
                            'p025': totals[index] * scale * (1 - width[index]),
                            'p975': totals[index] * scale * (1 + width[index]),
                            'yearBasis': ('measured'
                                          if params.data.year_is_measured(year)
                                          else ('backcast'
                                                if year < params.scenario.base_year
                                                else 'projected')),
                            'n_segments': 1,
                            'torque_low': anchor_torque,
                            'torque_high': anchor_torque,
                            'extrapolated': bool(abs(torque - anchor_torque) > 1),
                            'basis': f'{anchor_name}, {anchor_mass:.1f} kg at '
                                     f'{anchor_torque:.0f} Nm, split from '
                                     f'run.spec_composition',
                        })
    return pd.DataFrame(rows)


def verify_by_torque(grid: pd.DataFrame, corrected: pd.DataFrame,
                     params) -> pd.DataFrame:
    """
    How well the torque fit reproduces the values it was fitted on.

    NOT A GOODNESS OF FIT FOR ITS OWN SAKE. The grid replaces the segment
    dimension, so the only honest question is whether a torque and a year give
    back what the segment rows say. This compares the fitted value at each
    segment's own torque against that segment's own mass.
    """
    frame = corrected.copy()
    if 'materialClass' not in frame.columns:
        frame['materialClass'] = [material_class(row)
                                  for _, row in frame.iterrows()]
    frame = frame[(frame.parameterCode == params.data.material_of_component)]
    frame = frame.dropna(subset=['meanValue', 'torque_min']).copy()
    frame['torque'] = (frame.torque_min + frame.torque_max) / 2.0

    base = grid[(grid.productionYear == params.scenario.base_year) &
                (grid.voltageClass == params.scenario.base_voltage)]

    rows = []
    for (motor, klass), block in frame.groupby(['componentKeyLevel1',
                                                'materialClass']):
        actual = block.groupby('torque')['meanValue'].sum()
        curve = base[(base.componentKeyLevel1 == motor) &
                     (base.materialClass == klass)]
        if curve.empty or actual.empty:
            continue
        predicted_by_torque = curve.groupby('torque_nm')['meanValue'].sum()
        fitted = np.interp(actual.index, predicted_by_torque.index,
                           predicted_by_torque.values)
        residual = fitted - actual.values
        denominator = ((actual.values - actual.values.mean()) ** 2).sum()
        rows.append({
            'motor': motor, 'material': klass, 'n': len(actual),
            'mean_kg': actual.mean(),
            'mean_abs_error_kg': np.abs(residual).mean(),
            'mean_abs_error_pct': np.abs(residual).mean() / actual.mean(),
            'max_abs_error_kg': np.abs(residual).max(),
            'r2': 1 - (residual ** 2).sum() / denominator if denominator else np.nan,
        })
    return pd.DataFrame(rows).sort_values(['motor', 'material'])


def figure_by_torque(grid: pd.DataFrame, params, out_path: str,
                     corrected: pd.DataFrame = None) -> str:
    """
    Each material against torque, with the fit's own uncertainty.

    ⚠️ ONE PANEL PER MATERIAL, NOT A STACK. A stacked area hides exactly what
    this figure is for: the band belongs to each fitted line, and five bands
    on top of each other cannot be read. Stacked composition is
    02_motor_mass.png; this one is about how well each relationship is known.

    THE BAND IS THE FIT'S UNCERTAINTY. Segments are bootstrapped and the line
    refitted on every draw, so the band widens towards the ends of the range
    where fewer points hold it down -- 12% at 500 Nm, 46% at 100 Nm. Drawing
    only the sources' own intervals would have given about 1% everywhere,
    which would be a statement about the workbook rather than about the fit.
    """
    import matplotlib.pyplot as plt

    motor = 'PMElectricMotors'
    years = [params.scenario.base_year, 2040, 2070]
    block = grid[(grid.componentKeyLevel1 == motor) &
                 (grid.voltageClass == params.scenario.base_voltage)]
    if block.empty:
        raise ValueError(f'no rows for {motor}')

    observed = {}
    if corrected is not None:
        frame = corrected.copy()
        if 'materialClass' not in frame.columns:
            frame['materialClass'] = [material_class(row)
                                      for _, row in frame.iterrows()]
        frame = frame[(frame.componentKeyLevel1 == motor) &
                      (frame.parameterCode == params.data.material_of_component)]
        frame = frame.dropna(subset=['meanValue', 'torque_min']).copy()
        frame['torque'] = (frame.torque_min + frame.torque_max) / 2.0
        # ⚠️ THE ERROR BARS ARE VERTICAL, AND THEY ARE THE STATED ONES.
        # An earlier version drew the segment's p05-p95 TORQUE spread as a
        # horizontal bar, which makes no sense and Matthias said so: a segment
        # is a diagonal cloud of vehicles along the line, because the heavier
        # ones are also the higher-torque ones. A horizontal bar asserts that
        # the mass stays put across that torque span, which is the opposite of
        # what the whole figure says.
        #
        # What a point legitimately carries is the uncertainty the source
        # states for that mass -- p025 to p975, per draw across the components
        # that make up the material. That is vertical, and it is real.
        for klass, part in frame.groupby('materialClass'):
            observed[klass] = (
                part.groupby('torque')['meanValue'].sum(),
                part.groupby('torque')['p025'].sum(),
                part.groupby('torque')['p975'].sum())

    classes = [k for k in MATERIAL_COLOUR if k in set(block.materialClass)]
    figure, axes = plt.subplots(1, len(classes), figsize=(3.5 * len(classes), 5.2))
    high = float(block.torque_high.max())
    fades = [1.0, 0.55, 0.3]

    for axis, klass in zip(axes, classes):
        colour = MATERIAL_COLOUR[klass]
        rows = block[block.materialClass == klass]

        base = rows[rows.productionYear == params.scenario.base_year]
        band = base.pivot_table(index='torque_nm', values=['p025', 'p975'],
                                aggfunc='sum')
        axis.fill_between(band.index, band.p025, band.p975, color=colour,
                          alpha=0.2, lw=0)

        for fade, year in zip(fades, years):
            line = rows[rows.productionYear == year].pivot_table(
                index='torque_nm', values='meanValue', aggfunc='sum')
            axis.plot(line.index, line.meanValue, lw=2.2, color=colour,
                      alpha=fade, label=str(year))

        if klass in observed:
            values, low, high_v = observed[klass]
            axis.errorbar(values.index, values.values,
                          yerr=[np.maximum(0, values.values - low.values),
                                np.maximum(0, high_v.values - values.values)],
                          fmt='o', ms=5.5, mfc='white', mec='#111111', mew=1.3,
                          ecolor='#111111', elinewidth=1.0, capsize=2.5,
                          ls='none', zorder=9)

        axis.axvspan(high, float(block.torque_nm.max()), color='#000000',
                     alpha=0.06, lw=0)
        width = float(((band.p975 - band.p025) /
                       base.groupby('torque_nm').meanValue.sum()).reindex(
                           [500.0]).iloc[0])
        axis.set_title(f'{MATERIAL_LABEL[klass].split(" (")[0]}\n'
                       f'\u00b1{width / 2:.0%} bei 500 Nm', fontsize=10)
        axis.set_xlabel('Drehmoment [Nm]')
        axis.set_ylim(bottom=0)
        axis.grid(alpha=0.22, lw=0.6)

    axes[0].set_ylabel('kg je Fahrzeug')
    handles, labels = axes[0].get_legend_handles_labels()
    figure.legend(handles, labels, loc='lower center', ncol=3, fontsize=9,
                  frameon=False, title='Jahr', bbox_to_anchor=(0.5, -0.02))
    figure.suptitle(
        f'Masse je Werkstoff gegen Drehmoment \u2014 '
        f'{MOTOR_LABEL.get(motor, motor)}, {params.scenario.base_voltage} V.  '
        'Kein Segment.\n'
        'Band: Unsicherheit DES FITS (Bootstrap der Segmente), nur 2020.  '
        'Punkte: Segmentwerte mit der angegebenen Massenunsicherheit',
        fontsize=11)
    figure.tight_layout(rect=(0, 0.07, 1, 1))
    figure.savefig(out_path, dpi=160)
    plt.close(figure)
    return out_path


def figure_all_types(grid: pd.DataFrame, params, out_path: str,
                     corrected: pd.DataFrame = None) -> str:
    """
    All five motor types against torque, each with its own uncertainty.

    ⚠️ THE BANDS ARE MEANT TO BE LARGE WHERE THEY ARE LARGE. Matthias
    2026-09-18: it is extrapolation, therefore the uncertainty ranges are
    essential even if they turn out big. The two spec machines are built from
    a single data sheet, so their band carries the borrowed shape's own width
    plus `spec_share_uncertainty` on the derived split -- about +/-26-29%,
    against +/-6-12% for the three fitted from eleven segments.

    A star marks the one machine each spec type actually rests on. Everything
    to either side of it is extrapolation from that single point.
    """
    import matplotlib.pyplot as plt

    years = [params.scenario.base_year, 2045, 2070]
    fades = [1.0, 0.6, 0.35]
    motors = [m for m in params.run.motors if m in set(grid.componentKeyLevel1)]
    sheets = machines().set_index('name')

    figure, axes = plt.subplots(1, len(motors), figsize=(3.6 * len(motors), 5.4),
                                sharex=True)
    for axis, motor in zip(axes, motors):
        block = grid[(grid.componentKeyLevel1 == motor) &
                     (grid.voltageClass == params.scenario.base_voltage)]
        fitted = motor not in params.run.spec_composition
        colour = '#2C5F8A' if fitted else '#B5651D'

        for fade, year in zip(fades, years):
            rows = block[block.productionYear == year]
            total = rows.groupby('torque_nm')[['meanValue', 'p025',
                                               'p975']].sum()
            axis.fill_between(total.index, total.p025, total.p975,
                              color=colour, alpha=0.13 * fade, lw=0)
            axis.plot(total.index, total.meanValue, lw=2.2, color=colour,
                      alpha=fade, label=str(year))

        base = block[block.productionYear == params.scenario.base_year]
        total = base.groupby('torque_nm')[['meanValue', 'p025', 'p975']].sum()
        width = float(((total.p975 - total.p025) /
                       (2 * total.meanValue)).mean())

        if not fitted:
            anchor_name = params.run.spec_composition[motor]['anchor']
            if anchor_name in sheets.index:
                anchor = sheets.loc[anchor_name]
                axis.plot([anchor.torque_shaft], [anchor.mass_kg], marker='*',
                          ms=17, color='#C0392B', mec='white', mew=1.1,
                          zorder=9)
                axis.annotate(f'{anchor_name}\n{anchor.mass_kg:.0f} kg',
                              xy=(float(anchor.torque_shaft),
                                  float(anchor.mass_kg)),
                              xytext=(-6, 12), textcoords='offset points',
                              fontsize=7.4, color='#C0392B', ha='right')
        # ⚠️ THE COUNT IS READ, NOT WRITTEN. An earlier version printed
        # "11 Segmente" for every fitted type, which is wrong for the
        # induction configuration -- it appears in three segments only, and
        # that is exactly why its band is enormous.
        count = int(base.n_segments.max()) if 'n_segments' in base else 0
        source = (f'{count} Segmente' if fitted else '1 Datenblatt')
        warn = '  \u26a0' if fitted and count < 5 else ''
        axis.set_title(f'{MOTOR_LABEL.get(motor, motor)}\n'
                       f'{source}   \u00b1{width:.0%}{warn}', fontsize=9.5)
        if fitted and count < 5:
            axis.annotate('Bootstrap auf wenigen Punkten:\n'
                          'die Steigung ist kaum bestimmt',
                          xy=(0.5, 0.03), xycoords='axes fraction',
                          fontsize=7.6, ha='center', color='#A93226',
                          style='italic')
            # Keep the panel readable; the band's own number is in the title.
            axis.set_ylim(0, float(total.meanValue.max()) * 2.2)
        axis.set_xlabel('Drehmoment [Nm]')
        axis.set_ylim(bottom=0)
        axis.grid(alpha=0.22, lw=0.6)
        axis.legend(fontsize=8, framealpha=0.95, loc='upper left', title='Jahr')

    axes[0].set_ylabel('Masse je Fahrzeug [kg]')
    figure.suptitle(
        'Alle fünf Motortypen: Masse gegen Drehmoment, '
        f'{params.scenario.base_voltage} V, kein Segment.\n'
        f'Bänder: 95% aus {params.monte_carlo.draws:,} Monte-Carlo-Ziehungen.  '
        'Blau: aus Segmenten gefittet.  Orange: aus EINEM Datenblatt, '
        'Stern = die Maschine', fontsize=11)
    figure.tight_layout()
    figure.savefig(out_path, dpi=160)
    plt.close(figure)
    return out_path
