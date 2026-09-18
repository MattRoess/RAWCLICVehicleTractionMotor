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
READERS = ('house', 'bom')


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
        # 29.05.2026 and reviewed by Valeo, so it is CURRENT -- the `-2020`
        # in productionYear is the vintage it describes, not its age.
        # Its masses are a torque regression fitted to Drexler 2025.
        'zenodo': dict(
            file='documentation/TractionMotor/Zenodo/'
                 'RAWCLIC_BEV_motor_consolidated_data_V1.xlsx',
            sheet='consolidated_data',
            role='data', tier='tier1', vintage=2020, published=2026,
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
            file='', sheet='',
            role='data', tier='tier2', vintage=2025, published=2025,
            reads='bom',
            citation='Drexler, D., Kampker, A., Born, H., et al. Advances in '
                     'electric motors: a review and benchmarking of product '
                     'design and manufacturing technologies. Elektrotech. '
                     'Inftech. 142, 312-345 (2025). '
                     'doi:10.1007/s00502-025-01331-3'),

        # VERIFICATION ONLY. Too old to supply a mass, and therefore -- §2.1
        # -- not a data source at any layer. Declared so that a comparison
        # against them is reproducible and so that nobody proposes them as
        # data again.
        'chalmers2018': dict(
            file='', sheet='',
            role='verification', tier='tier2', vintage=2017, published=2018,
            reads='bom',
            citation='Nordelof et al., A scalable life cycle inventory of an '
                     'electrical automotive traction machine, Int J LCA, '
                     'Part I (2017), Part II (2018)'),
        'munro2020': dict(
            file='', sheet='',
            role='verification', tier='tier2', vintage=2020, published=2020,
            reads='bom',
            citation='Munro & Associates, 10-motor benchmark (2020), paid'),
        'greet': dict(
            file='', sheet='',
            role='verification', tier='tier2', vintage=2020, published=2025,
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
        'axialFluxPMElectricMotors':       'report',
        'dualRotorRadialPMElectricMotors': 'report',
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
    output: OutputParams = field(default_factory=OutputParams)

    SECTIONS = ('data', 'run', 'output')

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
            if tier not in ('zenodo', 'report'):
                issues.append(f"run.motors[{name!r}] is {tier!r}; it has to be "
                              f"'zenodo' or 'report', which is what says how far "
                              f"a number may be trusted")

        if tuple(self.run.layer_names) != ('product', 'component', 'material', 'element'):
            issues.append('run.layer_names is the house schema\'s own nesting and '
                          'is not a setting to change')

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
        if not path:
            state = 'DECLARED, file not yet in hand'
        elif os.path.isfile(path):
            state = path
        else:
            state = f'{path}\n                  NOT FOUND'
        mark = '*' if name == params.data.primary else ' '
        lines.append(f'{mark} {name:<14} {entry.get("role","?"):<12} '
                     f'{entry.get("tier","?"):<6} '
                     f'vintage {entry.get("vintage","?")}\n'
                     f'                  {state}')

    if params.data.composition_file:
        lines.append(f'  elements       {params.data.composition_file}')
    else:
        lines.append('  elements       NOT YET. No source in the registry carries '
                     'an element layer.')
    lines.append('  (* is data.primary)')
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
