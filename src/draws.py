"""
src/draws.py
============

Turns a mean and a 95% interval into draws, and draws back into an interval.

**THIS IS THE ONLY PLACE UNCERTAINTY IS COMBINED.** Anywhere a derived
quantity needs an interval, it is computed per draw and summarised at the end.
Adding, subtracting or shifting two published intervals produces something that
looks like an interval and is not one: a percentile is a property of a
distribution, and arithmetic on percentiles is not the percentile of the
result.

NOTHING HERE MAKES A NUMBER MORE CERTAIN THAN ITS SOURCE. The draws carry the
published interval and the assumptions declared in `MonteCarloParams` -- a
normal shape, a correlation that the dataset does not measure -- and those
assumptions travel with the result rather than disappearing into it.
"""
from __future__ import annotations

import numpy as np

# The 95% interval is +-1.959964 sigma for a normal. Written out rather than
# rounded to 1.96, because the factor is used to go both ways and a rounded
# constant makes a round trip drift.
Z95 = 1.959963984540054


def sigma_from_interval(p025, p975):
    """Sigma implied by a 95% interval under a normal shape."""
    return (np.asarray(p975, dtype=float) - np.asarray(p025, dtype=float)) / (2 * Z95)


def draw(mean, p025, p975, size: int, rng, correlated_with=None,
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


def summarise(values, clip_at_zero: bool = True) -> dict:
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
