"""
src/source.py
=============

Reads the Zenodo consolidated dataset, and says what is wrong with it.

THE AUDIT IS THE FIRST STAGE ON PURPOSE. This workbook is the only measured
source the project has (`METHODOLOGY.md` §2, tier 1), so every mass this
project ever reports rests on it. A defect in it does not announce itself
downstream -- it arrives as a plausible number in a figure. The checks below
were each written after finding the thing they check for, and they stay in the
code so that a corrected or re-issued workbook is tested against the same list
rather than against somebody's memory.

NOTHING HERE CORRECTS ANYTHING. The audit reports; it does not write to the
workbook and it does not patch values in memory. What to do about a finding is
a decision with a source behind it, and it belongs in the documentation and in
whatever stage applies it -- not hidden in a loader.
"""
from __future__ import annotations

import pandas as pd

from src.params_schema import Params

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
    from Chalmers, Munro 2020 or GREET enters the dataset, and a rule that
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
        from src.drexler import components
        frame = components()
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
