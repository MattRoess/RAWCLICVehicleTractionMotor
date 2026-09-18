"""
src/params_schema.py
====================

**EVERY SETTING FOR THIS PROJECT IS IN THIS FILE.** Open it, change a value,
press Run on `00_parameters.py`, then on the stages in order. Nothing is
passed on a command line: none of the stages takes an argument, because a
switch that only exists on a command line is a switch nobody sees.

`params.xlsx` and `documentation/PARAMETER_REFERENCE.md` are OUTPUTS of this
file. Editing either of them changes nothing.

WHAT THIS PROJECT IS
--------------------
What BEV traction motors are made of: components, the materials those
components are made of, and the elements in those materials -- for the years
the stock-and-flow model needs, so that
`RAWCLICStockAndFlow/code/04_03_tractionmotors.py` can multiply a fleet by a
composition.

THE SOLE SOURCE IS THE ZENODO CONSOLIDATED DATASET
--------------------------------------------------
`RAWCLIC_BEV_motor_consolidated_data_V1.xlsx`, 264 rows in the RAWCLIC house
schema. Everything this project produces rests on it, and where it is silent
this project has to say so rather than fill the gap from a report.

Two things it does NOT carry, and they shape everything here:

  * **NO ELEMENTS.** `materialKeyLevel3` and `materialKeyLevel4` are empty and
    there is no `e-m` row. Materials stop at `alloySteel` and `highCuAlloys2`.
    The element layer arrives as a separate workbook, derived from this same
    source -- `composition_file` below, empty until it exists.

  * **NO YEARS.** `productionYear` holds one value, `-2020`. One vintage. A
    2010-2070 trajectory is not in the data and cannot be read out of it; it
    is a modelling decision that has to be written down as one.

⚠️ AND THE REPORTS BESIDE IT ARE NOT A SECOND SOURCE. The critical review of
2026-09-18 marks as unconfirmed the motor mass, the stator and rotor
laminations, the stator copper, the shaft, the housing, the bearings, the
cooling hardware, the sensors, and every architecture share for 2030, 2035,
2040 and 2050. What it confirms is qualitative: NdFeB carries Nd and Pr with
optional Dy or Tb, Nd is about 29-32% of magnet mass, magnet mass falls in a
broad 0.5-3.0 kg traction range. Those are directions, not a bill of material.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field, fields


class ParameterError(ValueError):
    """Raised when a setting in this file cannot be used as written."""


# The roles a source may have. `data` may supply values into the dataset;
# `verification` may only be compared against it. METHODOLOGY.md §2.1 -- and
# it is enforced here rather than remembered, because a rule that lives only
# in prose is a rule that gets broken by whoever is in a hurry.
ROLES = ('data', 'verification')

# How far a number may be trusted. `tier1` is measured and in the house
# schema; `tier2` is everything else and has to be labelled wherever it is
# drawn. METHODOLOGY.md §2.
TIERS = ('tier1', 'tier2')

# The readers that exist. A source declares which shape its file is in, so
# that adding a source is a declaration and not a code change -- until the
# shape is genuinely new, which is what `READERS` makes visible.
READERS = ('house', 'bom', 'drexler', 'spec')


@dataclass
class DataParams:
    """Every source this project knows about, and what each one may be used for."""

    # ******************************************************************
    #  THE SOURCE REGISTRY. **ADD A SOURCE BY ADDING AN ENTRY HERE.**
    #
    #  Nothing else has to change. No stage names a file; every stage asks
    #  this registry for the sources it is entitled to, so a new bill of
    #  material becomes available to the whole project by being declared.
    #
    #  Each entry:
    #    file      path from the project root. **BLANK MEANS DECLARED BUT
    #              NOT YET IN HAND** -- the source is known, the file is not
    #              here. That is not an error; it is the honest state of a
    #              source we have found and not yet obtained.
    #    sheet     worksheet, where it matters.
    #    role      'data'         may supply values into the dataset
    #              'verification' may ONLY be compared against it
    #    tier      'tier1' measured and in the house schema; 'tier2' else
    #    vintage   the year the DATA describes -- not when it was published
    #    published the year the source was issued
    #    covers    (first, last) -- THE YEARS THIS SOURCE MAY SUPPLY. Not
    #              when it was written: which years its numbers legitimately
    #              describe. A year outside this window is refused.
    #    horizon   'historic' only, today. NO SOURCE DESCRIBES THE FUTURE.
    #              Every year past the registry's coverage is a modelling
    #              decision built in §4 of METHODOLOGY.md, and it has to be
    #              visible as one rather than inherited from a measurement.
    #    reads     which reader in src/source.py understands the file
    #    citation  what a figure caption has to be able to say
    #
    #  ⚠️ `role` IS A GATE AND NOT A LABEL. A 'verification' source is
    #  refused by the data path, in code. METHODOLOGY.md §2.1: the age of a
    #  source applies to its WEIGHTS, and a source too old to supply a mass
    #  is too old to be quietly holding up a composition nobody checked.
    #  SAFE TO CHANGE: yes -- that is the point of this block.
    # ******************************************************************
    sources: dict[str, dict] = field(default_factory=lambda: {

        # TIER 1. The only measured source in the house schema. Dated
        # 29.05.2026 and reviewed by Valeo -- but it DESCRIBES 2020, and that
        # is what `covers` records.
        #
        # ⚠️ HISTORIC REVIEW ONLY. Decided 2026-09-18. The fleet it describes
        # is the 2020 fleet: 400 V, round-wire stators, magnets sized before
        # heavy-rare-earth reduction became a design driver. Read forward it
        # would assert that none of that changes, which is the one thing this
        # project exists to deny. It anchors the historic end of the
        # trajectory and supplies no year after 2020.
        'zenodo': dict(
            file='documentation/TractionMotor/Zenodo/'
                 'RAWCLIC_BEV_motor_consolidated_data_V1.xlsx',
            sheet='consolidated_data',
            role='data', tier='tier1', vintage=2020, published=2026,
            # ONE VINTAGE, so one year. `productionYear` holds a single
            # value and nothing in the workbook describes 2010 or 2015; a
            # wider window here would be this file inventing coverage the
            # data does not have.
            covers=(2020, 2020), horizon='historic',
            reads='house',
            citation='RAWCLIC Deliverable 3.1, Harmonized datasets for '
                     'secondary RM sources for the twin transition, V1, '
                     '29.05.2026'),

        # THE UPSTREAM OF TIER 1, and the recent benchmark this project has
        # been looking for. Every mass in the consolidated dataset is a
        # regression through ITS data points, so it is not a second opinion
        # -- it is the first one, at full resolution and per machine rather
        # than per segment. It also settles what a component mass in the
        # consolidated file is supposed to mean, which is the one blocking
        # finding the audit cannot resolve from inside the data.
        'drexler2025': dict(
            file='documentation/TractionMotor/s00502-025-01331-3.pdf',
            sheet='',
            role='data', tier='tier2', vintage=2023, published=2025,
            # 31 VEHICLES OF MODEL YEARS 2018-2023, so the window is the model
            # years the sample actually contains -- not the year of
            # publication. The paper compares 2018-2021 against 2022-2023 and
            # that two-period split is the only time resolution it has.
            covers=(2018, 2023), horizon='historic',
            reads='drexler',
            citation='Drexler, D., Kampker, A., Born, H., et al. Advances in '
                     'electric motors: a review and benchmarking of product '
                     'design and manufacturing technologies. Elektrotech. '
                     'Inftech. 142, 312-345 (2025). '
                     'doi:10.1007/s00502-025-01331-3'),

        # MANUFACTURER DATA SHEETS. Whole-machine mass and torque, for
        # topologies the consolidated dataset does not contain at all.
        # ⚠️ NOT A BILL OF MATERIAL -- a data sheet says what a machine
        # weighs, not what it is made of, so it cannot fill a composition
        # row. It bounds the sum instead, which is worth having: an axial
        # flux machine whose WHOLE mass is below a radial machine's active
        # parts at the same torque is a statement no regression through
        # radial motors can make.
        'yasa': dict(
            file='',            # transcribed in src/composition.py
            sheet='',
            role='data', tier='tier2', vintage=2019, published=2019,
            covers=(2019, 2019), horizon='historic',
            reads='spec',
            citation='YASA P400 R Product Sheet, Rev 13, June 2019, ID 22735, '
                     'yasa.com'),

        # VERIFICATION ONLY. Too old to supply a mass, and therefore -- §2.1
        # -- not a data source at any layer. Declared so that a comparison
        # against them is reproducible and so that nobody proposes them as
        # data again.
        'chalmers2018': dict(
            file='', sheet='',
            role='verification', tier='tier2', vintage=2017, published=2018,
            covers=(2017, 2017), horizon='historic',
            reads='bom',
            citation='Nordelof et al., A scalable life cycle inventory of an '
                     'electrical automotive traction machine, Int J LCA, '
                     'Part I (2017), Part II (2018)'),
        'munro2020': dict(
            file='', sheet='',
            role='verification', tier='tier2', vintage=2020, published=2020,
            covers=(2020, 2020), horizon='historic',
            reads='bom',
            citation='Munro & Associates, 10-motor benchmark (2020), paid'),
        'greet': dict(
            file='', sheet='',
            role='verification', tier='tier2', vintage=2020, published=2025,
            covers=(2020, 2020), horizon='historic',
            reads='bom',
            citation='Argonne National Laboratory, R&D GREET, vehicle '
                     'material composition'),
    })

    # WHICH SOURCE IS THE BASE. The one every stage starts from, and the one
    # the audit checks. It has to be a 'data' source that is present.
    # SAFE TO CHANGE: yes.
    primary: str = 'zenodo'

    # THE ELEMENT COMPOSITION, when it arrives. BLANK MEANS NOT YET: no
    # source in the registry carries an element layer, so a stage that needs
    # elements says so and stops rather than inventing them.
    # SAFE TO CHANGE: yes.
    composition_file: str = ''
    composition_sheet: str = ''

    # THE THREE PARAMETER CODES, as the house schema spells them.
    #   c-p   this component, as a share of the product
    #   m-c   this material, as a share of the component
    #   e-m   this element, as a share of the material
    # SAFE TO CHANGE: no, unless the house schema changes.
    component_of_product: str = 'c-p'
    material_of_component: str = 'm-c'
    element_of_material: str = 'e-m'

    # ---- convenience, so no stage reaches into the registry by hand ----

    @property
    def consolidated_file(self) -> str:
        """The primary source's path."""
        return self.sources.get(self.primary, {}).get('file', '')

    @property
    def consolidated_sheet(self) -> str:
        """The primary source's worksheet."""
        return self.sources.get(self.primary, {}).get('sheet', '')

    def usable(self, role: str = 'data') -> dict[str, dict]:
        """
        The declared sources with that role whose file is actually here.

        THE ROLE GATE LIVES HERE. Asking for 'data' cannot return a
        verification source, whatever a caller intends, because the filter is
        on the registry and not on the caller's memory.
        """
        return {name: entry for name, entry in self.sources.items()
                if entry.get('role') == role and entry.get('file')
                and os.path.isfile(entry['file'])}

    def declared(self, role: str = 'data') -> dict[str, dict]:
        """Sources with that role, present or not -- what the project knows of."""
        return {name: entry for name, entry in self.sources.items()
                if entry.get('role') == role}

    def covering(self, year: int, role: str = 'data') -> dict[str, dict]:
        """The sources entitled to supply that year."""
        return {name: entry for name, entry in self.declared(role).items()
                if entry.get('covers', (0, 0))[0] <= year <= entry.get('covers', (0, 0))[1]}

    @property
    def measured_until(self) -> int:
        """
        The last year any data source covers.

        **EVERYTHING AFTER THIS YEAR IS CONSTRUCTED.** Not interpolated from a
        measurement, not inherited from the newest source -- built by the
        scenarios in METHODOLOGY.md §4, on stated mechanisms. This property
        exists so that a stage can ask rather than assume, and so that moving
        the boundary is a registry edit rather than a number buried in code.
        """
        windows = [entry.get('covers', (0, 0))[1]
                   for entry in self.declared('data').values()]
        return max(windows) if windows else 0

    def year_is_measured(self, year: int) -> bool:
        """Whether any data source is entitled to supply that year."""
        return bool(self.covering(year, 'data'))


@dataclass
class RunParams:
    """What is described, and over which years."""

    # WHICH YEARS THE COMPOSITION IS DESCRIBED FOR.
    #     '2010-2070, 5'   that range, every 5th year
    #     '2010-2070'      every year in it
    #     '2020'           one year
    #
    # ⚠️ THE DATA HAS ONE VINTAGE, `-2020`. Every year outside that is a
    # modelling decision and has to be visible as one -- what changes between
    # 2010 and 2070, and on whose authority. Until that is written down, a
    # trajectory here means the 2020 composition repeated, which is a
    # statement about the world and not a neutral default.
    # SAFE TO CHANGE: yes.
    years: str = '2010-2070, 5'

    # ******************************************************************
    #  THE MOTORS DESCRIBED, and WHERE EACH ONE'S NUMBERS COME FROM.
    #
    #  'zenodo'  the consolidated dataset. Measured, in the house schema,
    #            and the vintage is `-2020`: this is the fleet as it IS.
    #  'report'  the comprehensive workbook of 2026-09-18. A promising
    #            architecture that the dataset does not carry, because it
    #            is not yet in the fleet in any quantity. Its bill of
    #            material is stated at 60% source reliability and the
    #            critical review marks its key values unconfirmed.
    #
    #  THE TIER IS A SETTING AND NOT A COMMENT because every number this
    #  project reports has to say which of the two it came from. A 2070
    #  axial-flux magnet mass and a 2020 PM magnet mass are not the same
    #  kind of statement, and a figure that draws them in one colour says
    #  they are.
    #
    #  The first three names are `componentKeyLevel1` exactly as the
    #  dataset spells them, with 110, 110 and 44 rows. THE LAST TWO ARE
    #  OUR NAMES -- the dataset has no key for them -- written in the same
    #  style so they cannot be mistaken for keys it does carry.
    #
    #  ⚠️ DeepDrive IS NOT AXIAL FLUX. The report workbook's Axial Flux
    #  sheet calls it "Double-rotor axial flux"; the critical review
    #  corrects that to a dual-rotor RADIAL flux topology, stator between
    #  inner and outer rotors, and cites the company's own technical
    #  description. The name here follows the review.
    #
    #  SynRM and in-wheel are deliberately absent: demonstrators only, with
    #  no bill of material in either source.
    #  SAFE TO CHANGE: yes. A 'zenodo' name the dataset does not carry is
    #  refused; a 'report' name is taken on trust, which is what the tier
    #  is for.
    # ******************************************************************
    motors: dict[str, str] = field(default_factory=lambda: {
        'PMElectricMotors':                'zenodo',
        'EESMElectricMotors':              'zenodo',
        'IMandPMElectricMotors':           'zenodo',
        # Both now have published masses from their makers, so they are no
        # longer 'report' guesses -- see MACHINES in src/composition.py.
        # ⚠️ 'spec' IS NOT 'zenodo'. A data sheet gives a whole-machine mass
        # and no composition at all, so these two have a mass and no bill of
        # material. Anything that needs a material split has to say so and
        # stop, rather than borrow the radial one.
        'axialFluxPMElectricMotors':       'spec',
        'dualRotorRadialPMElectricMotors': 'spec',
    })

    # THE VEHICLE SEGMENTS, as `productKeyLevel3` spells them. A-F are the
    # passenger segments and JB-JF the light commercial ones. Empty means all
    # eleven the dataset carries.
    # SAFE TO CHANGE: yes -- a name the dataset does not have is refused.
    segments: tuple[str, ...] = ()

    # THE FOUR LAYERS, finest last. The stock-and-flow model reads this shape:
    # a product holds components, a component is made of materials, a material
    # is made of elements.
    # SAFE TO CHANGE: no. It is the house schema's own nesting.
    layer_names: tuple[str, ...] = ('product', 'component', 'material', 'element')


@dataclass
class ScenarioParams:
    """
    How the composition changes between now and 2070.

    ⚠️ NONE OF THIS IS MEASURED. One year of the trajectory is read from a
    source; every other year is built here. These settings are the mechanism,
    written out so that the trajectory can be argued with instead of admired.
    """

    # ******************************************************************
    #  MATERIAL EFFICIENCY: same torque, less material.
    #
    #  THE OBSERVED RATE, from Drexler 2025, between the period averages
    #  of 2018-2021 and 2022-2023 (3 years apart):
    #      stator lamination stack   -21.1%   -7.6%/yr
    #      winding copper, all       -23.6%   -8.6%/yr
    #
    #  ⚠️ AND IT CANNOT CONTINUE. -7.6%/yr compounded to 2070 leaves 3% of
    #  the stator, which is not a motor. What Drexler measured is a step
    #  change that happened once -- hairpin winding replacing round wire,
    #  shorter active length, smaller outer diameter -- not a process that
    #  repeats every year.
    #
    #  So the curve saturates:
    #      m(t) = limit + (m2020 - limit) * exp(-k (t - 2020))
    #  with k set so the INITIAL slope matches the measured rate, and
    #  `limit` a floor that physics puts underneath.
    # ******************************************************************

    # THE FLOOR, as a share of the 2020 mass. Below these, the machine stops
    # being able to do its job.
    #
    # ⚠️ ASSUMPTIONS, NOT MEASUREMENTS. No source in the registry states them.
    # They are argued from what limits each material, and they are the single
    # biggest lever on every 2070 number here -- vary them first.
    #
    #   lamination 0.55  Iron carries flux. Non-oriented electrical steel
    #                    saturates around 2.0-2.1 T and motors run the yoke
    #                    near 1.5-1.7 T, so pushing towards saturation buys
    #                    roughly a quarter less iron -- and core loss rises
    #                    with frequency squared, which is what stops it.
    #                    Shorter active length at higher speed buys the rest.
    #   copper     0.50  Copper carries current. The slot fill factor rises
    #                    from about 45% for round wire to about 60-70% for
    #                    hairpin, against a geometric ceiling near 90% that
    #                    insulation and bending radii keep out of reach.
    #                    Direct oil cooling then allows a higher current
    #                    density in the same slot.
    #   magnet     0.60  Magnet mass falls with better flux concentration and
    #                    stronger grades, but torque needs remanence and the
    #                    material is already near its theoretical maximum.
    #   steel      0.75  Shafts and gearbox are limited by mechanical
    #                    strength, not by electromagnetics, so they fall
    #                    least.
    #   aluminium  0.70  Housing and cooling: structure plus heat path.
    # SAFE TO CHANGE: yes, and this is the first thing to test.
    floor: dict[str, float] = field(default_factory=lambda: {
        'lamination': 0.55,
        'copper': 0.50,
        'magnet': 0.60,
        'steel': 0.75,
        'aluminium': 0.70,
    })

    # ******************************************************************
    #  THE STEADY ANNUAL RATE.
    #
    #  ⚠️ THIS IS NOT DREXLER'S MEASURED RATE, AND THAT IS DELIBERATE.
    #
    #  Drexler measures -7.6%/yr for the lamination stack and -8.6%/yr for
    #  copper between 2018-2021 and 2022-2023. An earlier version of this
    #  file used those as the starting slope, and it produced a 37-41%
    #  drop between 2020 and 2030 -- which Matthias did not believe, and
    #  he was right.
    #
    #  THE MISTAKE WAS STRUCTURAL, not numerical. What Drexler measured is
    #  the rate DURING A ONE-OFF TECHNOLOGY CHANGE that happened to fall
    #  inside his window: round wire giving way to hairpin, active length
    #  and outer diameter shrinking with it. Treating that as a standing
    #  annual rate asserts that a comparable technology change arrives
    #  every year and keeps arriving until 2070. It does not.
    #
    #  So this is the rate of ORDINARY REFINEMENT -- better steel grades,
    #  tighter tolerances, incremental thermal gains -- with no technology
    #  change in it. Matthias's original instruction was 'a steady
    #  improvement, not too much, but steady', and this is that.
    #
    #  A FUTURE STEP CHANGE IS NOT DENIED, it is simply not modelled as a
    #  rate. Axial flux reaching volume, or a magnet-free architecture
    #  taking share, is a different machine and belongs in `run.motors` as
    #  its own entry -- not hidden inside a percentage.
    #
    #  NOT MEASURED. No source gives a refinement rate for anything here.
    #  SAFE TO CHANGE: yes, and this is the number to argue about.
    # ******************************************************************
    initial_rate: dict[str, float] = field(default_factory=lambda: {
        'lamination': 0.010,
        'copper': 0.010,
        'magnet': 0.012,      # slightly faster: heavy-REE reduction is active
        'steel': 0.004,
        'aluminium': 0.006,
    })

    # ⚠️ WHAT DREXLER MEASURED, KEPT SO IT IS NOT LOST. Used in the figures
    # to show the observed step against the modelled steady rate, so that the
    # gap between them is visible and arguable rather than quietly resolved.
    # SAFE TO CHANGE: no -- these are somebody else's measurements.
    observed_transition_rate: dict[str, float] = field(default_factory=lambda: {
        'lamination': 0.076,
        'copper': 0.086,
    })

    # ⚠️ BEFORE THE BASE YEAR THE SAME CURVE CANNOT BE RUN BACKWARDS.
    # Found by building it: a saturating exponential reversed is an exploding
    # one, and at -7.6%/yr it makes a 2010 stator THREE TIMES the mass of a
    # 2020 stator. No 2010 motor was that heavy.
    #
    # The reason is that the measured rate is not a constant of nature. It is
    # the rate DURING the hairpin transition, 2018-2023 -- round wire giving
    # way to flat wire, active length and outer diameter shrinking with it.
    # Before that transition the same mechanism was not acting, so the
    # backcast needs its own rate, and a slower, constant one:
    #
    #     m(t) = m2020 * (1 + backcast_rate) ** (2020 - t),  t < 2020
    #
    # ⚠️ NOT MEASURED. No source in the registry describes a 2010 motor.
    # These are the weakest numbers in the whole project. 1.5%/yr over ten
    # years makes a 2010 stator 16% heavier than a 2020 one, which is the
    # right order for a decade of ordinary refinement without a technology
    # change -- but it is a judgement, and the backcast years are labelled
    # 'backcast' in the output so nothing can mistake them for data.
    # SAFE TO CHANGE: yes.
    backcast_rate: dict[str, float] = field(default_factory=lambda: {
        'lamination': 0.015,
        'copper': 0.015,
        'magnet': 0.010,
        'steel': 0.005,
        'aluminium': 0.008,
    })

    # ******************************************************************
    #  VOLTAGE CLASS, and what it does to copper.
    #
    #  Raising the DC link voltage lowers the current for the same power,
    #  and a lower current needs less conductor. That is why 800 V is a
    #  copper story before it is a charging story.
    #
    #  ⚠️ SET BY MATTHIAS 2026-09-18: 800 V uses TWO THIRDS of the copper
    #  MASS of 400 V. Stated as mass, which is what the model needs.
    #
    #  An earlier version of this file stored a conductor DIAMETER instead
    #  and squared it to get mass. That was a misreading, and it produced
    #  0.86 kg of stator copper for an 800 V C-segment machine -- against
    #  2.04-9.54 kg measured by Drexler across 46 machines that include
    #  800 V cars. Two thirds is both what was meant and what the sample
    #  can live with.
    #
    #  WHY NOT ONE HALF, which is what halving the current would suggest:
    #  not all of the copper scales with current. Winding heads, terminals,
    #  interconnections and minimum manufacturable cross-sections do not
    #  shrink with the conductor, so the saving is less than the current
    #  ratio. Two thirds is the measured-world answer to a textbook
    #  argument.
    #
    #  1000 V IS DERIVED, not given. Fitting a power law through the one
    #  stated point, mass proportional to U**-a with (800/400)**-a = 2/3,
    #  gives a = 0.584, and (1000/400)**-a = 0.585. Written out so
    #  that changing the 800 V value and leaving 1000 V stale is visible.
    #  SAFE TO CHANGE: yes.
    # ******************************************************************
    copper_mass: dict[int, float] = field(default_factory=lambda: {
        400: 1.000,      # the reference: the fleet the dataset describes
        800: 0.667,      # set by Matthias -- two thirds of the 400 V copper
        1000: 0.585,      # derived from the 800 V point, power law
    })

    # WHICH VOLTAGE CLASS THE BASE DATASET IS. The consolidated data
    # describes the 2020 fleet, which is overwhelmingly 400 V.
    # SAFE TO CHANGE: yes.
    base_voltage: int = 400

    # ⚠️ HIGHER VOLTAGE ALSO COSTS MASS, and this model does not carry it.
    # Drexler: PEEK is emerging as the primary wire insulation for 800 V+,
    # and the stripped, welded X-pin wire ends need encapsulation because
    # air and creepage distances are short. Insulation, potting and
    # insulated bearings all grow with voltage. Only the saving is
    # modelled, so 800 V looks better than it is by an amount nobody here
    # has quantified.

    # THE YEAR THE CURVE STARTS FROM, and the composition it starts from.
    # This is the one year the dataset actually describes.
    # SAFE TO CHANGE: no, unless the primary source changes.
    base_year: int = 2020

    # ⚠️ HOW FAR THE MEASURED RATE IS TRUSTED TO KEEP RUNNING. The measured
    # rate is an average over a 3-year window in which one technology changed.
    # `rate_decays_over` is how many years the mechanism is assumed to keep
    # acting at all before the exponential has effectively reached its floor.
    # It is expressed through the curve rather than as a second parameter:
    # k = initial_rate / (1 - floor), so a high floor means a fast approach to
    # it, and a low floor a long slow decline. Written here so the reader
    # knows the shape is a CHOICE.
    # SAFE TO CHANGE: no -- it is documentation of the formula above.
    curve: str = 'saturating exponential, k = initial_rate / (1 - floor)'


@dataclass
class MonteCarloParams:
    """How uncertainty is propagated. It is never propagated any other way."""

    # ⚠️ EVERY DERIVED UNCERTAINTY COMES FROM DRAWS. Not from adding,
    # subtracting or shifting intervals. A percentile is a property of a
    # distribution, and arithmetic on two percentiles is not the percentile of
    # the result -- it only looks like one, which is what makes it dangerous.
    # SAFE TO CHANGE: yes. More draws, narrower Monte Carlo noise, slower run.
    draws: int = 200_000

    # THE SEED, so a figure can be reproduced exactly.
    # SAFE TO CHANGE: yes.
    seed: int = 20260918

    # HOW A MEAN AND A 95% INTERVAL BECOME A DISTRIBUTION. The consolidated
    # dataset gives mean, p025 and p975 and no draws, so a shape has to be
    # assumed to draw at all. 'normal' takes sigma = (p975 - p025) / (2 x 1.96).
    #
    # THIS IS AN ASSUMPTION AND NOT A READING. The underlying quantity is a
    # regression confidence interval, which is normal by construction, so the
    # assumption is a good one -- but a mass cannot go negative and a normal
    # can, so draws are clipped at zero and the clipping is counted.
    # SAFE TO CHANGE: yes.
    interval_shape: str = 'normal'

    # ⚠️ CORRELATION BETWEEN TWO MASSES OF THE SAME MOTOR, and the single most
    # consequential assumption in the correction layer.
    #
    # The stator mass and its winding mass are BOTH regressions on the same
    # vehicle's torque, fitted to the same sample. They are not independent:
    # a motor that is larger than the fit expects is larger in both. So
    # subtracting them as independent variables would inflate the lamination
    # interval by combining two errors that largely cancel.
    #
    #   1.0  perfectly correlated -- the interval NARROWS, because the two
    #        errors cancel. Defensible: one regression, one torque.
    #   0.0  independent -- the interval WIDENS by sqrt(2)-ish. Wrong here,
    #        but it is what naive subtraction implies.
    #
    # 0.9 says: the same torque drives both, and the residual scatter of the
    # winding fit is its own. NOT MEASURED -- the dataset gives no covariance.
    # Stated here so it can be argued with, and varied to see whether anything
    # depends on it.
    # SAFE TO CHANGE: yes, and worth testing at 0.0 and 1.0.
    within_motor_correlation: float = 0.9


@dataclass
class OutputParams:
    """Where what this project produces is written."""

    # WHAT THE STAGES WRITE. Not `documentation/`, which holds what was
    # received and what is written about it.
    # SAFE TO CHANGE: yes.
    data_dir: str = 'data'

    # SAFE TO CHANGE: yes.
    figures_dir: str = 'figures'


@dataclass
class Params:
    """Every setting, in the order this file writes them."""

    data: DataParams = field(default_factory=DataParams)
    run: RunParams = field(default_factory=RunParams)
    scenario: ScenarioParams = field(default_factory=ScenarioParams)
    monte_carlo: MonteCarloParams = field(default_factory=MonteCarloParams)
    output: OutputParams = field(default_factory=OutputParams)

    SECTIONS = ('data', 'run', 'scenario', 'monte_carlo', 'output')

    def validate(self) -> list[str]:
        """
        Everything wrong with the settings, as sentences. Empty when they hold.

        REPORTED TOGETHER, not one at a time. Correcting a file three times
        because it is checked three times is how a person stops reading the
        message and starts guessing.
        """
        issues: list[str] = []

        # THE REGISTRY. Every entry is checked, so a typo in a source added
        # today is reported today and not on the run that first needs it.
        for name, entry in self.data.sources.items():
            where = f'data.sources[{name!r}]'
            if entry.get('role') not in ROLES:
                issues.append(f'{where}["role"] is {entry.get("role")!r}; it has '
                              f'to be one of {ROLES}. "verification" means the '
                              f'source may be compared against and never read '
                              f'into the dataset.')
            if entry.get('tier') not in TIERS:
                issues.append(f'{where}["tier"] is {entry.get("tier")!r}; it has '
                              f'to be one of {TIERS}')
            if entry.get('reads') not in READERS:
                issues.append(f'{where}["reads"] is {entry.get("reads")!r}; it '
                              f'has to be one of {READERS}. A genuinely new file '
                              f'shape needs a reader in src/source.py before it '
                              f'can be declared.')
            covers = entry.get('covers')
            if (not isinstance(covers, (tuple, list)) or len(covers) != 2
                    or not all(isinstance(year, int) for year in covers)
                    or covers[0] > covers[1]):
                issues.append(f'{where}["covers"] is {covers!r}; it has to be '
                              f'(first_year, last_year) -- the years this source '
                              f'may supply, with first <= last')
            if entry.get('horizon') != 'historic':
                issues.append(f'{where}["horizon"] is {entry.get("horizon")!r}. '
                              f'Only "historic" is allowed: no source describes '
                              f'the future, and a year past the registry\'s '
                              f'coverage is a modelling decision, not a reading.')
            if not entry.get('citation'):
                issues.append(f'{where} has no citation. Every number this '
                              f'project reports has to be attributable, so a '
                              f'source without one cannot be used.')
            # A blank file is a source we know of and do not yet have. A named
            # file that is not there is a mistake.
            if entry.get('file') and not os.path.isfile(entry['file']):
                issues.append(f'{where}["file"] is {entry["file"]!r}, which is '
                              f'not a file. Leave it blank until the file is '
                              f'actually here.')

        if self.data.primary not in self.data.sources:
            issues.append(f'data.primary is {self.data.primary!r}, which is not '
                          f'a key in data.sources')
        else:
            entry = self.data.sources[self.data.primary]
            if entry.get('role') != 'data':
                issues.append(f'data.primary is {self.data.primary!r}, whose role '
                              f'is {entry.get("role")!r}. The base source of the '
                              f'project cannot be a verification source.')
            if not entry.get('file'):
                issues.append(f'data.primary is {self.data.primary!r} and its file '
                              f'is blank -- there is nothing to read')

        # The element workbook is allowed to be missing -- it does not exist
        # yet. Naming one that is not there is a different matter.
        if self.data.composition_file and not os.path.isfile(self.data.composition_file):
            issues.append(f'data.composition_file names '
                          f'{self.data.composition_file!r}, which is not a file. '
                          f'Leave it blank until the workbook exists.')

        if not self.run.motors:
            issues.append('run.motors is empty -- there is nothing to describe')
        for name, tier in self.run.motors.items():
            if tier not in ('zenodo', 'spec', 'report'):
                issues.append(f"run.motors[{name!r}] is {tier!r}; it has to be "
                              f"'zenodo' (measured, in the house schema), "
                              f"'spec' (a manufacturer data sheet: whole-machine "
                              f"mass, NO composition) or 'report'")

        if tuple(self.run.layer_names) != ('product', 'component', 'material', 'element'):
            issues.append('run.layer_names is the house schema\'s own nesting and '
                          'is not a setting to change')

        for name, value in self.scenario.floor.items():
            if not 0.0 < value <= 1.0:
                issues.append(f'scenario.floor[{name!r}] is {value}; it is a '
                              f'share of the {self.scenario.base_year} mass and '
                              f'has to lie in (0, 1]')
            if name not in self.scenario.initial_rate:
                issues.append(f'scenario.floor has {name!r} and '
                              f'scenario.initial_rate does not')
            if name not in self.scenario.backcast_rate:
                issues.append(f'scenario.floor has {name!r} and '
                              f'scenario.backcast_rate does not')
        for name, value in self.scenario.initial_rate.items():
            if not 0.0 <= value < 1.0:
                issues.append(f'scenario.initial_rate[{name!r}] is {value}; it '
                              f'is a fraction per year and has to lie in [0, 1)')

        if self.scenario.base_voltage not in self.scenario.copper_mass:
            issues.append(f'scenario.base_voltage is '
                          f'{self.scenario.base_voltage}, which is not a key in '
                          f'scenario.copper_mass')
        for volts, ratio in self.scenario.copper_mass.items():
            if not 0.0 < ratio <= 1.0:
                issues.append(f'scenario.copper_mass[{volts}] is {ratio}; it is '
                              f'a copper mass relative to the base voltage and '
                              f'has to lie in (0, 1]')

        if self.monte_carlo.draws < 1000:
            issues.append(f'monte_carlo.draws is {self.monte_carlo.draws}; below '
                          f'about 1000 the Monte Carlo noise is wider than the '
                          f'uncertainty being propagated')
        if self.monte_carlo.interval_shape != 'normal':
            issues.append(f'monte_carlo.interval_shape is '
                          f'{self.monte_carlo.interval_shape!r}; only "normal" '
                          f'is implemented')
        if not 0.0 <= self.monte_carlo.within_motor_correlation <= 1.0:
            issues.append(f'monte_carlo.within_motor_correlation is '
                          f'{self.monte_carlo.within_motor_correlation}; it is a '
                          f'correlation and has to lie in [0, 1]')

        if not _YEARS.fullmatch((self.run.years or '').strip()):
            issues.append(f'run.years is {self.run.years!r}. It reads '
                          f"'2010-2070, 5', '2010-2070', or '2020'.")

        return issues


# '2020', '2010-2070', or '2010-2070, 5'. Written once so the message above and
# the reader cannot disagree about what is accepted.
_YEARS = re.compile(r'\d{4}(\s*-\s*\d{4})?(\s*,\s*\d+)?')
def current() -> Params:
    """
    The settings above, checked.

    Every stage calls this rather than building Params itself, so a mistaken
    edit is reported once and clearly at the start of a run, naming the setting
    and what it should have been.
    """
    params = Params()
    issues = params.validate()
    if issues:
        raise ParameterError(
            'There is a problem with the settings in src/params_schema.py:\n\n'
            + '\n'.join(f'  - {issue}' for issue in issues)
            + '\n\nOpen that file, correct the value, and run again.')
    return params


def describe(section, name: str) -> str:
    """
    The comment block written above the setting, as one line.

    TAKES THE SECTION ITSELF, not its name. It used to look the class up in a
    dict written out by hand -- run, data, monte_carlo, figures -- and adding
    `combine` to SECTIONS without adding it there made `00_parameters.py` die
    on `KeyError: 'combine'`, after the section had been declared, defaulted,
    validated and used everywhere else. The list a person has to remember to
    add to twice is the list that gets added to once.
    """
    section_type = section if isinstance(section, type) else type(section)
    return _FIELD_COMMENTS.get((section_type.__name__, name), '') or \
        f'Setting in {section_type.__name__}.'


def years_wanted(spec: str) -> list[int]:
    """
    The years `run.years` asks for.

    Written once, here, so that the settings file and every stage agree about
    what '2010-2070, 5' means.
    """
    spec = (spec or '').strip()
    step = 1
    if ',' in spec:
        spec, _, tail = spec.partition(',')
        step = int(tail.strip())
    spec = spec.strip()
    if '-' in spec:
        first, _, last = spec.partition('-')
        return list(range(int(first), int(last) + 1, step))
    return [int(spec)]


def source_status(params: Params) -> str:
    """
    Every declared source, whether it is here, and what it may be used for.

    Printed on every run of 00_parameters. A source declared with a blank file
    is not a fault -- it is one we have found and not yet obtained -- and
    seeing the list is the point: it is the project's own account of what it
    is standing on.
    """
    lines = []
    for name, entry in params.data.sources.items():
        path = entry.get('file') or ''
        if not path and entry.get('reads') in ('spec', 'drexler'):
            state = 'transcribed with citations in src/composition.py'
        elif not path:
            state = 'DECLARED, file not yet in hand'
        elif os.path.isfile(path):
            state = path
        else:
            state = f'{path}\n                  NOT FOUND'
        mark = '*' if name == params.data.primary else ' '
        covers = entry.get('covers', ('?', '?'))
        window = (f'{covers[0]}' if covers[0] == covers[1]
                  else f'{covers[0]}-{covers[1]}')
        lines.append(f'{mark} {name:<14} {entry.get("role","?"):<12} '
                     f'{entry.get("tier","?"):<6} covers {window}\n'
                     f'                  {state}')

    if params.data.composition_file:
        lines.append(f'  elements       {params.data.composition_file}')
    else:
        lines.append('  elements       NOT YET. No source in the registry carries '
                     'an element layer.')
    lines.append('  (* is data.primary)')

    # The single most consequential fact about this project, printed every run:
    # how few of the years it reports are actually measured.
    try:
        wanted = years_wanted(params.run.years)
    except Exception:                                    # noqa: BLE001
        wanted = []
    if wanted:
        measured = [year for year in wanted if params.data.year_is_measured(year)]
        lines.append(f'\n  YEARS  {len(measured)} of {len(wanted)} measured: '
                     f'{", ".join(map(str, measured)) or "none"}')
        lines.append(f'         every other year is CONSTRUCTED by the scenarios '
                     f'in METHODOLOGY.md §4,\n         not read from a source. '
                     f'Sources stop at {params.data.measured_until}.')
    return '\n  '.join(lines)


def flatten(params: Params) -> list[list]:
    """[name, description, key, value] per setting, in the order written above."""
    rows: list[list] = []
    for section_name in params.SECTIONS:
        section = getattr(params, section_name)
        for f in fields(section):
            value = getattr(section, f.name)
            rows.append([
                f.name,
                describe(section, f.name),
                f'{section_name}.{f.name}',
                json.dumps(value) if isinstance(value, (list, tuple, dict)) else value,
            ])
    return rows


def _collect_field_comments() -> dict[tuple[str, str], str]:
    """
    Read the comment block sitting above each setting, out of this file's own
    source.

    Comments are discarded by Python at import time, so they have to be read
    back from the source to appear in params.xlsx. Doing it this way means the
    explanation a reader sees next to the value is the same text that reaches
    the spreadsheet -- there is no second copy to fall out of date.
    """
    import ast
    import inspect

    source = inspect.getsource(__import__(__name__, fromlist=['_']))
    lines = source.splitlines()
    comments: dict[tuple[str, str], str] = {}

    for node in ast.walk(ast.parse(source)):
        if not isinstance(node, ast.ClassDef):
            continue
        for statement in node.body:
            if not (isinstance(statement, ast.AnnAssign)
                    and isinstance(statement.target, ast.Name)):
                continue
            block = []
            index = statement.lineno - 2          # the line above the setting
            while index >= 0 and lines[index].strip().startswith('#'):
                block.insert(0, lines[index].strip().lstrip('#').strip())
                index -= 1
            if block:
                comments[(node.name, statement.target.id)] = ' '.join(block)
    return comments


_FIELD_COMMENTS = _collect_field_comments()
