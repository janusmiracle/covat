from trajectory import *
from datashader.utils import export_image

# Plot the various attractors and output datashader images.

# ----------------------------------------------------------- #


# Arnold Map
def Arnold(a=0.15, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = arnold_trajectory(a, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Bedhead Attractor
def Bedhead(a=-0.81, b=-0.92, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = bedhead_trajectory(a, b, 1, 1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Belykh Map
def Belykh(a=0.8, b=1.55, k=0.5, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = belykh_trajectory(a, b, k, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Belykh Map Variant 1
def BelykhV1(a=1.5, b=0.3, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = belykh_v1_trajectory(a, b, 0.5, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Burger's Map Attractor
def Burgers(a=0.9, b=0.9, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = burgers_trajectory(a, b, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Business Cycle Map
def BusinessCycle(a=1.46, b=0.6, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = business_cycle_trajectory(a, b, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Cao-Lai Attractor
def CaoLai(r=3.70, p=5.00, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = cao_lai_trajectory(r, p, 0.5, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Cat Map
def Cat(n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = cat_trajectory(0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Cathala Attractor
def Cathala(a=0.70, b=-0.82, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = cathala_trajectory(a, b, 0.5, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Chirikov Standard Map // INCOMPLETE
def ChirikovStandard(K=0.6, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = chirikov_trajectory(K, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Clifford Attractor
def Clifford(a=3, b=9, c=4, d=-4, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = clifford_trajectory(a, b, c, d, 0, 0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Coupled Logistic Map
def CoupledLogistic(a=1.4, b=3.0, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = coupled_logistic_trajectory(a, b, 0.3, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Cross Chaotic Map
def CrossChaotic(a=0.9, b=1.65, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = cross_chaotic_trajectory(a, b, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# DeJong Attractor
def DeJong(a=1.7, b=1.7, c=0.6, d=1.2, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = dejong_trajectory(a, b, c, d, 0, 0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Dual Henon Map
def DualHenon(a=2.4, b=0.3, c=0.1, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = dual_henon_trajectory(a, b, c, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Elhadj-Sprott C Map
def ElhadjSprottC(a=4.0, b=0.3, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = elhadj_sprott_c_trajectory(a, b, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Fractal Dream Attractor
def FractalDream(a=-1.9956, b=-1.4528, c=-2.66206, d=0.8517, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = fractal_dream_trajectory(a, b, c, d, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Gingerbread Map
def Gingerbread(a=-1.753, b=-1.0, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = gingerbread_trajectory(a, b, 4.0, -2.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Gumowski-Mira Attractor
def GumowskiMira(a=0.008, b=0.05, mu=-0.7, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = gumowski_mira_trajectory(a, b, mu, 0, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# HCA Attractor
def HCA(a=1.84, c=-0.35, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = hca_trajectory(a, c, 1, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Heagy and Hammel Map // INCOMPLETE
def HeagyHammel(a=3.277, b=0.618, s=0.1, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = heagy_hammel_trajectory(a, b, s, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Hopalong Attractor
def Hopalong(a=0.4, b=1.0, c=0.0, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = hopalong_trajectory(a, b, c, 0.5, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Ikeda Attractor
def Ikeda(c=0.00, u=0.97, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = ikeda_trajectory(c, u, 0.5, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Joshi-Blackmore Attractor
def JoshiBlackmore(a=4.122, b=1.618, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = joshi_blackmore_trajectory(a, b, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# MacMillan Map // INCOMPLETE
def MacMillan(a=1.6, b=0.2, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = martin_trajectory(a, b, 0.1, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Martin Attractor
def Martin(a=3.4, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = martin_trajectory(a, 0.1, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Maynard-Smith Map // INCOMPLETE
def MaynardSmith(a=0.87, b=0.75, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = maynard_smith_trajectory(a, b, 0.0, 0.0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Mira Attractor
def Mira(a=0.31, b=1.0, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = mira_trajectory(a, b, 12.0, 3.0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Modified Lozi Attractor // INCOMPLETE
def ModifiedLozi(a=-1.81, b=0.3, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = modified_lozi_trajectory(a, b, 0.5, 0.5, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Modified Mira Map
def ModifiedMira(a=0.04, b=1.0, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = modified_mira_trajectory(a, b, -1.0, 8.0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Multifold Henon Attractor
def MultifoldHenon(a=4.0, b=0.9, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = multifold_henon_trajectory(a, b, 1.0, 1.0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Popcorn Attractor
def Popcorn(a=0.05, b=3.0, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = popcorn_trajectory(a, b, 0.6, 0.2, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Provenzale-Balmforth Map
def ProvenzaleBalmforth(a=1.5, b=2.5, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = provenzale_balmforth_trajectory(a, b, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Separatrix Map // INCOMPLETE
def Separatrix(a=1.5, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = separatrix_trajectory(a, 0.0, 1.0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Sine Map
def Sine(a=2.0, b=0.5, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = sine_trajectory(a, b, 2.0, 2.0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Sine Delay Map
def SineDelay(a=3.0, b=0.8, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = sine_delay_trajectory(a, b, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Sine Sine Map
def SineSine(a=5.0, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = sine_sine_trajectory(a, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Strelkova-Anishchenko Attractor
def StrelkovaAnishchenko(a=0.9, b=0.285, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = strelkova_anishchenko_trajectory(a, b, 0.1, 1.0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Sunflower Attractor
def Sunflower(a=-1.76, b=2.0, c=0.1, d=0.75, n=20000000, cmap=viridis):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = sunflower_trajectory(a, b, c, d, 1.86, 1.86, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Svensson Attractor
def Svensson(a=1.4, b=1.4, c=1.4, d=1.4, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = svensson_trajectory(a, b, c, d, 0, 0, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Tinkerbell Map
def Tinkerbell(a=0.90, b=-0.601, c=2.0, d=0.5, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = tinkerbell_trajectory(a, b, c, d, -0.72, -0.64, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Ushiki Attractor
def Ushiki(a=3.7, b=0.1, c=3.7, d=0.15, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = ushiki_trajectory(a, b, c, d, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img


# Yang-Cao Attractor // INCOMPLETE
def YangCao(a=1.3, b=4.0, c=0.4, u=0.9, m=4.0, n=20000000, cmap=inferno):
    cvs = ds.Canvas(plot_width=600, plot_height=600)
    xs, ys = yang_cao_trajectory(a, b, c, u, m, 0.1, 0.1, n)
    print("Plotting points..")
    agg = cvs.points(pd.DataFrame({"x": xs, "y": ys}), "x", "y")
    print("Generating image..")
    img = tf.shade(agg, cmap=cmap)
    return img
