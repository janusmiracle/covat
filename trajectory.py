import datashader as ds
import numpy as np, pandas as pd

# import sys
from colorcet import palette_n, palette
from functions import *
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis
from numba import jit

# Get trajectory of 2D Attractors
ps = {k: p[::-1] for k, p in palette_n.items()}

# ----------------------------------------------------------- #


# Arnold Map
@jit(nopython=True)
def arnold_trajectory(a, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = (xs[i] + ys[i] + a * np.cos(2 * np.pi * ys[i])) % 1
        ys[i + 1] = (xs[i] + 2 * ys[i]) % 1
    return xs, ys


# Bedhead Attractor
@jit(nopython=True)
def bedhead_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = np.sin(xs[i] * ys[i] / b) * ys[i] + np.cos(a * xs[i] - ys[i])
        ys[i + 1] = xs[i] + np.sin(ys[i]) / b
    return xs, ys


# Belykh Map
@jit(nopython=True)
def belykh_trajectory(a, b, k, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        fn = belykh_helper(xs[i], ys[i], k)
        if fn <= 0:
            xs[i + 1] = a * xs[i]
            ys[i + 1] = b * ys[i]
        elif fn > 0:
            xs[i + 1] = a * (xs[i] - 1) + 1
            ys[i + 1] = b * (ys[i] - 1) + 1
    return xs, ys


# Belykh Map Variant 1
@jit(nopython=True)
def belykh_v1_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        fn = belykh_v1_helper(xs[i])
        xs[i + 1] = fn - a * xs[i] + b * ys[i]
        ys[i + 1] = xs[i]
    return xs, ys


# Burger's Map Attractor
@jit(nopython=True)
def burgers_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = (1 - a) * xs[i] - ys[i] ** 2
        ys[i + 1] = (1 + b) * ys[i] + xs[i] * ys[i]
    return xs, ys


# Business Cycle Map
@jit(nopython=True)
def business_cycle_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = xs[i] + ys[i]
        ys[i + 1] = a * ys[i] - (a + 1) * ys[i] ** 3 - b * xs[i]
    return xs, ys


# Cao-Lai Attractor
@jit(nopython=True)
def cao_lai_trajectory(r, p, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = r * xs[i] * (1 - xs[i])
        ys[i + 1] = ((1 / (2 * np.pi)) * (p * xs[i])) * np.sin(2 * np.pi * ys[i])
    return xs, ys


# Cat Map
@jit(nopython=True)
def cat_trajectory(x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = (2 * xs[i] + ys[i]) % 1
        ys[i + 1] = (xs[i] + ys[i]) % 1
    return xs, ys


# Cathala Attractor
@jit(nopython=True)
def cathala_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = a * xs[i] + ys[i]
        ys[i + 1] = b + xs[i] ** 2
    return xs, ys


# Chirikov Standard Map // INCOMPLETE
@jit(nopython=True)
def chirikov_trajectory(K, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = np.mod(x0 + K * np.sin(y0), 2 * np.pi)
        ys[i + 1] = np.mod(y0 + xs[i], 2 * np.pi)
        # xs[i + 1] = xs[i] + (K * np.sin(ys[i]))  # % 1  # (2 * np.pi)
        # ys[i + 1] = (ys[i] + xs[i + 1]) % 1  # (2 * np.pi)
    return xs, ys


# Clifford Attractor
@jit(nopython=True)
def clifford_trajectory(a, b, c, d, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = np.sin(a * ys[i]) + c * np.cos(a * xs[i])
        ys[i + 1] = np.sin(b * xs[i]) + d * np.cos(b * ys[i])
    return xs, ys


# Coupled Logistic Map
@jit(nopython=True)
def coupled_logistic_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = (1 - a) * b * xs[i] * (1 - xs[i]) + a * b * ys[i] * (1 - ys[i])
        ys[i + 1] = (1 - a) * b * ys[i] * (1 - ys[i]) + a * b * xs[i] * (1 - xs[i])
    return xs, ys


# Cross Chaotic Map
@jit(nopython=True)
def cross_chaotic_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = 1 - a * ys[i] ** 2
        ys[i + 1] = np.cos(b * np.arccos(xs[i]))
    return xs, ys


# DeJong Attractor
@jit(nopython=True)
def dejong_trajectory(a, b, c, d, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = np.sin(a * ys[i]) - np.cos(b * xs[i])
        ys[i + 1] = np.sin(c * xs[i]) - np.cos(d * ys[i])
    return xs, ys


# Dual Henon Map
@jit(nopython=True)
def dual_henon_trajectory(a, b, c, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = a * xs[i] + b * ys[i] - c * xs[i] ** 3
        ys[i + 1] = xs[i]
    return xs, ys


# Elhadj-Sprott C Map
@jit(nopython=True)
def elhadj_sprott_c_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = -a * xs[i] ** 2 + ys[i]
        ys[i + 1] = b - np.abs(xs[i])
    return xs, ys


# Fractal Dream Attractor
@jit(nopython=True)
def fractal_dream_trajectory(a, b, c, d, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = np.sin(ys[i] * b) + c * np.sin(xs[i] * b)
        ys[i + 1] = np.sin(xs[i] * a) + d * np.sin(ys[i] * a)
    return xs, ys


# Gingerbread Map
@jit(nopython=True)
def gingerbread_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = 1 - a * np.abs(xs[i]) + b * ys[i]
        ys[i + 1] = xs[i]
    return xs, ys


# Gumowski-Mira Attractor
@jit(nopython=True)
def gumowski_mira_trajectory(a, b, mu, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = a * ys[i] * (1 - b * ys[i] * ys[i]) + ys[i] + gm(xs[i], mu)
        ys[i + 1] = -xs[i] + gm(xs[i + 1], mu)
    return xs, ys


# HCA Attractor
@jit(nopython=True)
def hca_trajectory(a, c, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = 1 - a * xs[i] ** 2 + c * (ys[i] ** 2 - xs[i] ** 2)
        ys[i + 1] = 1 - a * ys[i] ** 2 + c * (xs[i] ** 2 - ys[i] ** 2)
    return xs, ys


# Heagy and Hammel Map // INCOMPLETE
@jit(nopython=True)
def heagy_hammel_trajectory(a, b, s, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = a * (1 - s * np.cos(2 * np.pi * ys[i])) * (xs[i] * (1 - xs[i]))
        ys[i + 1] = (ys[i] + b) % 1
    return xs, ys


# Hopalong Attractor
@jit(nopython=True)
def hopalong_trajectory(a, b, c, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = ys[i] - np.sign(xs[i]) * np.sqrt(np.abs(b * xs[i] - c))
        ys[i + 1] = a - xs[i]
    return xs, ys


# Ikeda Attractor
@jit(nopython=True)
def ikeda_trajectory(c, u, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        t = c - (6 / (1 + xs[i] ** 2 + ys[i] ** 2))
        xs[i + 1] = 1 + u * (xs[i] * np.cos(t) - ys[i] * np.sin(t))
        ys[i + 1] = u * (xs[i] * np.sin(t) + ys[i] * np.cos(t))
    return xs, ys


# Joshi-Blackmore Map
@jit(nopython=True)
def joshi_blackmore_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
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


# MacMillan Map // INCOMPLETE
@jit(nopython=True)
def macmillan_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = ys[i]
        ys[i + 1] = xs[i] + (2 * a) * (ys[i] / (1 - ys[i] ** 2)) + b * ys[i]
    return xs, ys


# Martin Attractor
@jit(nopython=True)
def martin_trajectory(a, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = ys[i] - np.sin(xs[i])
        ys[i + 1] = a - xs[i]
    return xs, ys


# Maynard-Smith Attractor // INCOMPLETE
@jit(nopython=True)
def maynard_smith_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = ys[i]
        ys[i + 1] = -(a * ys[i]) + b - xs[i] ** 2
    return xs, ys


# Mira Attractor
@jit(nopython=True)
def mira_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = b * ys[i] + mira_helper(a, xs[i])
        ys[i + 1] = -xs[i] + mira_helper(a, xs[i + 1])
    return xs, ys


# Modified Lozi Attractor // INCOMPLETE
@jit(nopython=True)
def modified_lozi_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = 1 + a * (np.abs(xs[i]) - ys[i] ** 2) + ys[i]
        ys[i + 1] = b * xs[i]
    return xs, ys


# Modified Mira Map
@jit(nopython=True)
def modified_mira_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = b * ys[i] + modified_mira_helper(a, b, xs[i])
        ys[i + 1] = -xs[i] + modified_mira_helper(a, b, xs[i + 1])
    return xs, ys


# Multifold Henon Attractor
@jit(nopython=True)
def multifold_henon_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = 1 - a * np.sin(xs[i]) + b * ys[i]
        ys[i + 1] = xs[i]
    return xs, ys


# Popcorn Attractor
@jit(nopython=True)
def popcorn_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = xs[i] - a * np.sin(ys[i] + np.tan(b * ys[i]))
        ys[i + 1] = ys[i] - a * np.sin(xs[i] + np.tan(b * xs[i]))
    return xs, ys


# Provenzale-Balmforth Map
@jit(nopython=True)
def provenzale_balmforth_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        u = a * ys[i] + b
        xs[i + 1] = u * xs[i] * (1 - xs[i])
        ys[i + 1] = 4 * ys[i] * (1 - ys[i])
    return xs, ys


# Separatrix Map // INCOMPLETE
@jit(nopython=True)
def separatrix_trajectory(a, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = xs[i] + np.sin(2 * np.pi * ys[i])
        ys[i + 1] = (ys[i] + (a / (2 * np.pi)) * np.log(np.abs(xs[i]))) % 1
    return xs, ys


# Sine Map
@jit(nopython=True)
def sine_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = ys[i]
        ys[i + 1] = a * np.sin(xs[i]) + b * ys[i]
    return xs, ys


# Sine Delay Map
@jit(nopython=True)
def sine_delay_trajectory(a, b, x0, x1, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, x1
    for i in np.arange(n - 1):
        xs[i + 1] = b * xs[i - 1] + a * np.sin(xs[i])
        ys[i + 1] = xs[i]
    return xs, ys


# Sine Sine Map
@jit(nopython=True)
def sine_sine_trajectory(a, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = np.sin(xs[i]) - np.sin(a * ys[i])
        ys[i + 1] = xs[i]
    return xs, ys


# Strelkova-Anishchenko Attractor
@jit(nopython=True)
def strelkova_anishchenko_trajectory(a, b, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = 1 - a * xs[i] ** 2 + b * (ys[i] - xs[i])
        ys[i + 1] = 1 - a * ys[i] ** 2 + b * (xs[i] - ys[i])
    return xs, ys


# Sunflower Attractor
@jit(nopython=True)
def sunflower_trajectory(a, b, c, d, x0, x1, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, x1
    for i in np.arange(n - 1):
        xs[i + 1] = ((a + b * xs[i]) * (xs[i] + xs[i - 1])) / (
            1 + c * xs[i] ** 2 + d * xs[i - 1] ** 2
        )
        ys[i + 1] = xs[i]
    return xs, ys


# Svensson Attractor:
@jit(nopython=True)
def svensson_trajectory(a, b, c, d, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = d * np.sin(a * xs[i]) - np.sin(b * ys[i])
        ys[i + 1] = c * np.cos(a * xs[i]) + np.cos(b * ys[i])
    return xs, ys


# Tinkerbell Map
@jit(nopython=True)
def tinkerbell_trajectory(a, b, c, d, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = xs[i] ** 2 - ys[i] ** 2 + a * xs[i] + b * ys[i]
        ys[i + 1] = 2 * xs[i] * ys[i] + c * xs[i] + d * ys[i]
    return xs, ys


# Ushiki Attractor
@jit(nopython=True)
def ushiki_trajectory(a, b, c, d, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys = np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    for i in np.arange(n - 1):
        xs[i + 1] = (a - xs[i] - b * ys[i]) * xs[i]
        ys[i + 1] = (c - ys[i] - d * xs[i]) * ys[i]
    return xs, ys


# Yang Cao Attractor // INCOMPLETE
@jit(nopython=True)
def yang_cao_trajectory(a, b, c, u, m, x0, y0, n):
    print("Calculating trajectory..")
    xs, ys, w, s = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
    xs[0], ys[0] = x0, y0
    w, s = 0.1, 0.1
    for i in np.arange(n - 1):
        t = c - (6 / (1 + w**2 + s**2))
        w = 1 + u * (w * np.cos(t) - s * np.sin(t))
        s = u * (w * np.sin(t) + s + np.cos(t))

        xs[i + 1] = 1 - a * s**2 + b * w
        ys[i + 1] = m * w * (1 - s)
    return xs, ys

