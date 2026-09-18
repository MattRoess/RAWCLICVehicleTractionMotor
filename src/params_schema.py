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


@dataclass
class DataParams:
    """Where the source data is, and how its rows are labelled."""

    # THE CONSOLIDATED DATASET, and the only measured source this project has.
    # Written from the project root.
    # SAFE TO CHANGE: yes -- it must point at a file that exists.
    consolidated_file: str = (
        'documentation/TractionMotor/Zenodo/RAWCLIC_BEV_motor_consolidated_data_V1.xlsx')

    # The sheet holding the rows. The other sheet, `Guideline`, documents the
    # 43 columns and is not read.
    # SAFE TO CHANGE: yes.
    consolidated_sheet: str = 'consolidated_data'

    # THE ELEMENT COMPOSITION, when it arrives. Derived from the consolidated
    # dataset rather than from anywhere else, so it inherits its boundaries.
    # BLANK MEANS NOT YET. A stage that needs elements says so and stops,
    # rather than inventing them: the consolidated file has no element layer,
    # and a model that quietly proceeds without one reports a motor made of
    # nothing but materials.
    # SAFE TO CHANGE: yes.
    composition_file: str = ''
    composition_sheet: str = ''

    # THE THREE PARAMETER CODES, as the house schema spells them. A row says
    # which of the three it is, and nothing else in the file distinguishes a
    # component share from a material share.
    #   c-p   this component, as a share of the product
    #   m-c   this material, as a share of the component
    #   e-m   this element, as a share of the material
    # SAFE TO CHANGE: no, unless the house schema changes. They are written
    # here so that no stage spells one out for itself.
    component_of_product: str = 'c-p'
    material_of_component: str = 'm-c'
    element_of_material: str = 'e-m'


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

        if not self.data.consolidated_file:
            issues.append('data.consolidated_file is empty -- it names the only '
                          'measured source this project has')
        elif not os.path.isfile(self.data.consolidated_file):
            issues.append(f'data.consolidated_file points at '
                          f'{self.data.consolidated_file!r}, which is not a file')

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
    Whether the two source workbooks are actually there, in plain language.

    Printed on every run of 00_parameters. A missing element workbook is not a
    settings error -- it does not exist yet, and the settings say so by leaving
    the name blank -- but it is the single thing most worth knowing before
    expecting a composition out of this project.
    """
    lines = []
    path = params.data.consolidated_file
    if not path:
        lines.append('consolidated  NOT SET')
    elif not os.path.isfile(path):
        lines.append(f'consolidated  {path}\n                NOT FOUND')
    else:
        try:
            import pandas as pd
            frame = pd.read_excel(path, sheet_name=params.data.consolidated_sheet)
            motors = sorted(set(frame['componentKeyLevel1'].dropna()))
            years = sorted(set(map(str, frame['productionYear'].dropna())))
            codes = sorted(set(map(str, frame['parameterCode'].dropna())))
            lines.append(f'consolidated  {path}\n'
                         f'                {len(frame)} rows, '
                         f'motors {", ".join(motors)}\n'
                         f'                productionYear {", ".join(years)}, '
                         f'parameterCode {", ".join(codes)}')
        except Exception as error:                       # noqa: BLE001
            lines.append(f'consolidated  {path}\n                unreadable: {error}')

    if not params.data.composition_file:
        lines.append('elements      NOT YET. `data.composition_file` is blank, so no '
                     'element layer\n                exists -- the consolidated '
                     'dataset has none either.')
    elif os.path.isfile(params.data.composition_file):
        lines.append(f'elements      {params.data.composition_file}')
    else:
        lines.append(f'elements      {params.data.composition_file}\n'
                     f'                NOT FOUND')
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
                json.dumps(value) if isinstance(value, (list, tuple)) else value,
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
