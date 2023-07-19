import datashader as ds
import numpy as np, pandas as pd
import numba
from numba.experimental import jitclass
from numba import int64, float64
from colorcet import palette_n, palette
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis

# Setup @jitclass -- Runs program with high performance
spec = [("n", int64), ("x", float64[:]), ("y", float64[:])]

# File handles trajectory calculations
# ----------------------------------------------------------- #


@jitclass(spec)
class Trajectory:
    """
    Computes attractor trajectory.

    Parameters:
        n: Number of iterations // initialized to 20 million (int64)
        x: x-coordinate for point (float64)
        y: y-coordinate for point (float64)

    Returns:

        x: x-coordinate for point (float64)
        y: y-coordinate for point (float64)
    """

    def __init__(self, n=20000000):
        self.n = n
        self.x = np.zeros(self.n)
        self.y = np.zeros(self.n)

    def arnold(self, a, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = (xs[i] + ys[i] + a * np.cos(2 * np.pi * ys[i])) % 1
            ys[i + 1] = (xs[i] + 2 * ys[i]) % 1
        return xs, ys

    def bedhead(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = np.sin(xs[i] * ys[i] / b) * ys[i] + np.cos(a * xs[i] - ys[i])
            ys[i + 1] = xs[i] + np.sin(ys[i]) / b
        return xs, ys

    def _belykh_helper(self, x, y, k):
        return k * (2 * x - 1) + (2 * y - 1)

    def belykh(self, a, b, k, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            fn = self._belykh_helper(xs[i], ys[i], k)
            if fn <= 0:
                xs[i + 1] = a * xs[i]
                ys[i + 1] = b * ys[i]
            elif fn > 0:
                xs[i + 1] = a * (xs[i] - 1) + 1
                ys[i + 1] = b * (ys[i] - 1) + 1
        return xs, ys

    def _belykh_v1_helper(self, x):
        if x >= 0:
            return 1
        else:
            return -1

    def belykh_v1(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            fn = self._belykh_v1_helper(xs[i])
            xs[i + 1] = fn - a * xs[i] + b * ys[i]
            ys[i + 1] = xs[i]
        return xs, ys

    def burgers(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = (1 - a) * xs[i] - ys[i] ** 2
            ys[i + 1] = (1 + b) * ys[i] + xs[i] * ys[i]
        return xs, ys

    def business_cycle(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = xs[i] + ys[i]
            ys[i + 1] = a * ys[i] - (a + 1) * ys[i] ** 3 - b * xs[i]
        return xs, ys

    def cao_lai(self, r, p, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = r * xs[i] * (1 - xs[i])
            ys[i + 1] = ((1 / (2 * np.pi)) * (p * xs[i])) * np.sin(2 * np.pi * ys[i])
        return xs, ys

    def cat(self, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = (2 * xs[i] + ys[i]) % 1
            ys[i + 1] = (xs[i] + ys[i]) % 1
        return xs, ys

    def cathala(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = a * xs[i] + ys[i]
            ys[i + 1] = b + xs[i] ** 2
        return xs, ys

    def chirikov(self, K, x0, y0):  # Incomplete
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = xs[i] + ((K / (2 * np.pi)) * np.sin(2 * np.pi * ys[i]))
            ys[i + 1] = (ys[i] + [xs[i]]) % 1
            # xs[i + 1] = xs[i] + (K * np.sin(ys[i]))  # % 1  # (2 * np.pi)
            # ys[i + 1] = (ys[i] + xs[i + 1]) % 1  # (2 * np.pi)
        return xs, ys

    def clifford(self, a, b, c, d, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = np.sin(a * ys[i]) + c * np.cos(a * xs[i])
            ys[i + 1] = np.sin(b * xs[i]) + d * np.cos(b * ys[i])
        return xs, ys

    def coupled_logistic(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = (1 - a) * b * xs[i] * (1 - xs[i]) + a * b * ys[i] * (1 - ys[i])
            ys[i + 1] = (1 - a) * b * ys[i] * (1 - ys[i]) + a * b * xs[i] * (1 - xs[i])
        return xs, ys

    def cross_chaotic(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = 1 - a * ys[i] ** 2
            ys[i + 1] = np.cos(b * np.arccos(xs[i]))
        return xs, ys

    def dejong(self, a, b, c, d, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = np.sin(a * ys[i]) - np.cos(b * xs[i])
            ys[i + 1] = np.sin(c * xs[i]) - np.cos(d * ys[i])
        return xs, ys

    def dual_henon(self, a, b, c, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = a * xs[i] + b * ys[i] - c * xs[i] ** 3
            ys[i + 1] = xs[i]
        return xs, ys

    def elhadj_sprott_c(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = -a * xs[i] ** 2 + ys[i]
            ys[i + 1] = b - np.abs(xs[i])
        return xs, ys

    def fractal_dream(self, a, b, c, d, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = np.sin(ys[i] * b) + c * np.sin(xs[i] * b)
            ys[i + 1] = np.sin(xs[i] * a) + d * np.sin(ys[i] * a)
        return xs, ys

    def gingerbread(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = 1 - a * np.abs(xs[i]) + b * ys[i]
            ys[i + 1] = xs[i]
        return xs, ys

    def _gm_helper(self, x, mu):
        return x * mu + 2 * x * x * (1 - mu) / (1 + x * x)

    def gumowski_mira(self, a, b, mu, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = (
                a * ys[i] * (1 - b * ys[i] * ys[i]) + ys[i] + self._gm_helper(xs[i], mu)
            )
            ys[i + 1] = -xs[i] + self._gm_helper(xs[i + 1], mu)
        return xs, ys

    def hca(self, a, c, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = 1 - a * xs[i] ** 2 + c * (ys[i] ** 2 - xs[i] ** 2)
            ys[i + 1] = 1 - a * ys[i] ** 2 + c * (xs[i] ** 2 - ys[i] ** 2)
        return xs, ys

    def heagy_hammel(self, a, b, s, x0, y0):  # Incomplete
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = a * (1 - s * np.cos(2 * np.pi * ys[i])) * (xs[i] * (1 - xs[i]))
            ys[i + 1] = (ys[i] + b) % 1
        return xs, ys

    def hopalong(self, a, b, c, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = ys[i] - np.sign(xs[i]) * np.sqrt(np.abs(b * xs[i] - c))
            ys[i + 1] = a - xs[i]
        return xs, ys

    def ikeda(self, c, u, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            t = c - (6 / (1 + xs[i] ** 2 + ys[i] ** 2))
            xs[i + 1] = 1 + u * (xs[i] * np.cos(t) - ys[i] * np.sin(t))
            ys[i + 1] = u * (xs[i] * np.sin(t) + ys[i] * np.cos(t))
        return xs, ys

    def joshi_blackmore(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = (
                a
                * (np.exp((-xs[i] ** 2) - (ys[i] ** 2)))
                * (xs[i] * np.cos(2 * np.pi * b) - ys[i] * np.sin(2 * np.pi * b))
            )
            ys[i + 1] = (
                a
                * (np.exp((-xs[i] ** 2) - (ys[i] ** 2)))
                * (xs[i] * np.sin(2 * np.pi * b) + ys[i] * np.cos(2 * np.pi * b))
            )
        return xs, ys

    def macmillan(self, a, b, x0, y0):  # Incomplete
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = ys[i]
            ys[i + 1] = xs[i] + (2 * a) * (ys[i] / (1 - ys[i] ** 2)) + b * ys[i]
        return xs, ys

    def martin(self, a, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = ys[i] - np.sin(xs[i])
            ys[i + 1] = a - xs[i]
        return xs, ys

    def maynard_smith(self, a, b, x0, y0, n):  # Incomplete
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = ys[i]
            ys[i + 1] = -(a * ys[i]) + b - xs[i] ** 2
        return xs, ys

    def _mira_helper(self, a, x):
        return a * x + (2 * (1 - a) * x**2 / (1 + x**2))

    def mira(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = b * ys[i] + self._mira_helper(a, xs[i])
            ys[i + 1] = -xs[i] + self._mira_helper(a, xs[i + 1])
        return xs, ys

    def modified_lozi(self, a, b, x0, y0):  # Incomplete
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = 1 + a * (np.abs(xs[i]) - ys[i] ** 2) + ys[i]
            ys[i + 1] = b * xs[i]
        return xs, ys

    def _modified_mira_helper(self, a, b, x):
        return a * x - ((3 - a) / (a + np.exp(b * x)))

    def modified_mira(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = b * ys[i] + self._modified_mira_helper(a, b, xs[i])
            ys[i + 1] = -xs[i] + self._modified_mira_helper(a, b, xs[i + 1])
        return xs, ys

    def multifold_henon(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = 1 - a * np.sin(xs[i]) + b * ys[i]
            ys[i + 1] = xs[i]
        return xs, ys

    def popcorn(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = xs[i] - a * np.sin(ys[i] + np.tan(b * ys[i]))
            ys[i + 1] = ys[i] - a * np.sin(xs[i] + np.tan(b * xs[i]))
        return xs, ys

    def provenzale_balmforth(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            u = a * ys[i] + b
            xs[i + 1] = u * xs[i] * (1 - xs[i])
            ys[i + 1] = 4 * ys[i] * (1 - ys[i])
        return xs, ys

    def separatrix(self, a, x0, y0):  # Incomplete
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = xs[i] + np.sin(2 * np.pi * ys[i])
            ys[i + 1] = (ys[i] + (a / (2 * np.pi)) * np.log(np.abs(xs[i]))) % 1
        return xs, ys

    def sine(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = ys[i]
            ys[i + 1] = a * np.sin(xs[i]) + b * ys[i]
        return xs, ys

    def sine_delay(self, a, b, x0, x1):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, x1
        for i in np.arange(self.n - 1):
            xs[i + 1] = b * xs[i - 1] + a * np.sin(xs[i])
            ys[i + 1] = xs[i]
        return xs, ys

    def sine_sine(self, a, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = np.sin(xs[i]) - np.sin(a * ys[i])
            ys[i + 1] = xs[i]
        return xs, ys

    def strelkova_anishchenko(self, a, b, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = 1 - a * xs[i] ** 2 + b * (ys[i] - xs[i])
            ys[i + 1] = 1 - a * ys[i] ** 2 + b * (xs[i] - ys[i])
        return xs, ys

    def sunflower(self, a, b, c, d, x0, x1):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, x1
        for i in np.arange(self.n - 1):
            xs[i + 1] = ((a + b * xs[i]) * (xs[i] + xs[i - 1])) / (
                1 + c * xs[i] ** 2 + d * xs[i - 1] ** 2
            )
            ys[i + 1] = xs[i]
        return xs, ys

    def svensson(self, a, b, c, d, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = d * np.sin(a * xs[i]) - np.sin(b * ys[i])
            ys[i + 1] = c * np.cos(a * xs[i]) + np.cos(b * ys[i])
        return xs, ys

    def tinkerbell(self, a, b, c, d, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = xs[i] ** 2 - ys[i] ** 2 + a * xs[i] + b * ys[i]
            ys[i + 1] = 2 * xs[i] * ys[i] + c * xs[i] + d * ys[i]
        return xs, ys

    def ushiki(self, a, b, c, d, x0, y0):
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        for i in np.arange(self.n - 1):
            xs[i + 1] = (a - xs[i] - b * ys[i]) * xs[i]
            ys[i + 1] = (c - ys[i] - d * xs[i]) * ys[i]
        return xs, ys

    def yang_cao(self, a, b, c, u, m, x0, y0):  # Incomplete
        print("Calculating trajectory..")
        xs, ys = self.x, self.y
        xs[0], ys[0] = x0, y0
        w, s = 0.1, 0.1
        for i in np.arange(self.n - 1):
            t = c - (6 / (1 + w**2 + s**2))
            w = 1 + u * (w * np.cos(t) - s * np.sin(t))
            s = u * (w * np.sin(t) + s + np.cos(t))

            xs[i + 1] = 1 - a * s**2 + b * w
            ys[i + 1] = m * w * (1 - s)
        return xs, ys


# ----------------------------------------------------------- #
