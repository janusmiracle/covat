# from trajectory import *
from numba import jit
import numpy as np

# Helper functions for calculating trajectories.

# ----------------------------------------------------------- #


# Belykh Map
@jit(nopython=True)
def belykh_helper(x, y, k):
    return k * (2 * x - 1) + (2 * y - 1)


# Belykh Map Variant 1
@jit(nopython=True)
def belykh_v1_helper(x):
    if x >= 0:
        return 1
    else:
        return -1


# Gumowski-Mira Attractor
@jit(nopython=True)
def gm(x, mu):
    return x * mu + 2 * x * x * (1 - mu) / (1 + x * x)


# Mira Attractor
@jit(nopython=True)
def mira_helper(a, x):
    return a * x + (2 * (1 - a) * x**2 / (1 + x**2))


# Modified Mira Map
@jit(nopython=True)
def modified_mira_helper(a, b, x):
    return a * x - ((3 - a) / (a + np.exp(b * x)))
