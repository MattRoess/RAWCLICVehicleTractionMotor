"""
src/corrections.py
==================

Every correction applied to the consolidated dataset, declared one by one.

**THE SOURCE WORKBOOK IS NEVER EDITED.** It is a received deliverable under
`documentation/`, and a corrected copy that looks like the original is how a
project loses track of what it was actually given. Corrections are applied to
the frame after loading, and the corrected dataset is written to `data/` where
it is plainly a product of this project.

EACH ENTRY CARRIES ITS EVIDENCE. A correction without a source is a preference,
and a preference that edits data is indistinguishable from an error. `evidence`
says what establishes the defect; `applied` says whether it is in force.

`applied=False` IS A REAL STATE and not a disabled leftover: it marks a defect
that is established but whose correction is a judgement the project has not
taken. It is reported, carried in the output, and changes nothing until
somebody decides.
"""
from __future__ import annotations

import pandas as pd

# Drexler et al. (2025), transcribed in src/drexler.py. Cited here by figure.
DREXLER = 'Drexler et al. 2025, doi:10.1007/s00502-025-01331-3'

CORRECTIONS = [

    # -------------------------------------------------------------- C1
    dict(
        id='C1-stator-lamination',
        defect='The statorSheetLaminationStack material row holds the stator '
               'total exactly, in 24 of 24 filled cases, in a stator that also '
               'carries windings.',
        evidence=f'02_verify_stator.py against {DREXLER}, Fig. 11c: stator '
                 f'lamination measured on 46 machines at 7.20-35.52 kg. '
                 f'Reading the c-p row as the lamination puts 10 of 24 values '
                 f'above the measured maximum, up to 52.72 kg; reading it as '
                 f'the stator puts 23 of 24 inside the range.',
        action='lamination := c-p stator - stator windings',
        note='Total motor mass is unaffected. The material split was wrong, '
             'not the mass.',
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
        evidence=f'{DREXLER}, Fig. 30b: average total rotor copper mass 3.68 kg, '
                 f'max 4.45 kg (BMW i7 xDrive60 Individual), min 2.86 kg (BMW '
                 f'iX1 xDrive30 Premium), at 5% insulation. The consolidated '
                 f'values are 2-3x the measured maximum.',
        action='NONE -- reported only',
        note='⚠️ NOT APPLIED. The material correction (C2) is unambiguous; the '
             'mass is a second question. Replacing a segment-resolved series '
             'with one benchmark average is a modelling decision, not a '
             'correction, and the 1.5x segment-to-motor offset established in '
             '02_verify_stator.py means the two are not directly comparable '
             'either. Flagged for a decision.',
        applied=False),

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


def apply(frame: pd.DataFrame, params) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    The corrected dataset, and a log of what each correction actually changed.

    THE LOG COUNTS ROWS. A correction that matches nothing is a correction
    written against a workbook that has since changed, and it has to be visible
    rather than silently doing nothing.
    """
    data = params.data
    out = frame.copy()
    out['corrected'] = ''
    log: list[dict] = []

    def note(correction_id: str, changed: int, what: str) -> None:
        log.append(dict(id=correction_id, rows_changed=changed, what=what))

    # ---- C1 -------------------------------------------------------------
    key = ['componentKeyLevel1', 'productKeyLevel3']
    stator = out[(out.parameterCode == data.component_of_product) &
                 (out.componentKeyLevel2 == 'stator')].set_index(key)['meanValue']
    winding = out[(out.parameterCode == data.material_of_component) &
                  (out.componentKeyLevel2 == 'stator') &
                  (out.componentKeyLevel3 == 'windings')].set_index(key)['meanValue']
    is_lamination = ((out.parameterCode == data.material_of_component) &
                     (out.componentKeyLevel3 == 'statorSheetLaminationStack'))
    changed = 0
    for index in out[is_lamination].index:
        row = out.loc[index]
        pair = (row.componentKeyLevel1, row.productKeyLevel3)
        total, coil = stator.get(pair), winding.get(pair)
        if pd.isna(total) or pd.isna(coil):
            continue
        # The uncertainty columns are shifted by the same amount rather than
        # rescaled: the interval belongs to the regression that produced the
        # stator mass, and subtracting a winding does not narrow it.
        shift = total - coil - row.meanValue
        for column in ('meanValue', 'medianValue', 'modeValue', 'p025', 'p975'):
            if column in out.columns and pd.notna(out.at[index, column]):
                out.at[index, column] = out.at[index, column] + shift
        out.at[index, 'corrected'] = 'C1'
        changed += 1
    note('C1-stator-lamination', changed, 'lamination := stator - windings')

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

    # ---- C3: declared, not applied --------------------------------------
    note('C3-eesm-rotor-winding-mass', 0, 'NOT APPLIED -- flagged for decision')

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
