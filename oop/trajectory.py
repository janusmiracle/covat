import datashader as ds
import numpy as np, pandas as pd
import numba
from numba.experimental import jitclass
from numba import int64, float64

# import sys
from colorcet import palette_n, palette

# from functions import *
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis
#from numba import jit

# Testing OOP principles
spec = [("n", int64), ("x", float64[:]), ("y", float64[:])]


@jitclass(spec)
class Trajectory:
    def __init__(self, n=20000000):
        self.n = n
        self.x = np.zeros(self.n)
        self.y = np.zeros(self.n)

    def arnold(self, a, x0, y0):
        print("Calculating trajectory..")
        x, y = self.x, self.y
        x[0], y[0] = x0, y0
        for i in np.arange(self.n - 1):
            x[i + 1] = (x[i] + y[i] + a * np.cos(2 * np.pi * y[i])) % 1
            y[i + 1] = (x[i] + 2 * y[i]) % 1
        return x, y
