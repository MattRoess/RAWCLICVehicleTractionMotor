"""
src/drexler.py
==============

The published component statistics of Drexler et al. (2025), as a cited table.

    Drexler, D., Kampker, A., Born, H., Nankemann, M., Hartmann, S.,
    Kulawik, T. Advances in electric motors: a review and benchmarking of
    product design and manufacturing technologies.
    e+i Elektrotech. Inftech. 142, 312-345 (2025). Open access.
    doi:10.1007/s00502-025-01331-3

31 vehicles, model years **2018 to 2023**, 48 traction motors, analysed
top-down from the whole machine to stator and rotor component level.

WHY THESE NUMBERS ARE IN CODE AND NOT IN A DATA FILE. They are a dozen
published statistics, each needing a citation to the figure or passage it came
from, and `data/` is not in version control (see `.gitignore`). Written here,
every value is diffable, attributable, and changes visibly. A number that
matters this much should not live in a file nobody can review.

⚠️ THESE ARE SAMPLE STATISTICS, NOT TRUTH. n, mean, sd, min and max describe
46 machines that happened to be torn down. The minimum and maximum are the
extremes OF THAT SAMPLE -- a real motor outside them is unlikely, not
impossible -- and the mean carries the sample's own composition, which is
skewed towards whatever vehicles were available to the authors. Used as a
range check they are strong; used as a limit they would be wrong.

EACH VALUE IS TRANSCRIBED FROM THE PAPER AND NOTHING IS DERIVED. Averages,
minima and maxima are the authors'. Where the paper gives a figure statistic
and a slightly different number in the running text, BOTH are recorded and the
difference is noted rather than silently resolved.
"""
from __future__ import annotations

import pandas as pd

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
