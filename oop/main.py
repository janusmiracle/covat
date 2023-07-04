from trajectory import *
from datashader.utils import export_image
import matplotlib.pyplot as plt


# Plot the various attractors and output datashader images.
# ----------------------------------------------------------- #


class Attractor:
    """
    Plots the attractor trajectories and outputs a datashader image.

    Parameters:

        Trajectory(): The Trajectory class (holds all attractor trajectory calculations).
        cmap: The colormap for the datashader image. (Options-: inferno, viridis)

    Returns:

        Outputs a datashader image that can either be displayed or exported.
    """

    def __init__(self, cmap=inferno):
        self.trajectory = Trajectory()
        self.cmap = cmap

    def _plot(self, x, y):
        """
        Method that creates a canvas and aggregates points.
        """
        cvs = ds.Canvas(plot_width=600, plot_height=600)
        print("Plotting points..")
        agg = cvs.points(pd.DataFrame({"x": x, "y": y}), "x", "y")
        return agg

    def Arnold(self, a=0.15):
        x, y = self.trajectory.arnold(a, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Bedhead(self, a=-0.81, b=-0.92):
        x, y = self.trajectory.bedhead(a, b, 1, 1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Belykh(self, a=0.8, b=1.55, k=0.5):
        x, y = self.trajectory.belykh(a, b, k, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def BelykhV1(self, a=1.5, b=0.3):
        x, y = self.trajectory.belykh_v1(a, b, 0.5, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Burgers(self, a=0.9, b=0.9):
        x, y = self.trajectory.burgers(a, b, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def BusinessCycle(self, a=1.46, b=0.6):
        x, y = self.trajectory.business_cycle(a, b, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def CaoLai(self, r=3.70, p=5.00):
        x, y = self.trajectory.cao_lai(r, p, 0.5, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Cat(self):
        x, y = self.trajectory.cat(0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Cathala(self, a=0.70, b=-0.82):
        x, y = self.trajectory.cathala(a, b, 0.5, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def ChirikovStandard(self, K=0.9):  # Incomplete
        x, y = self.trajectory.chirikov(K, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Clifford(self, a=3, b=9, c=4, d=-4):
        x, y = self.trajectory.clifford(a, b, c, d, 0, 0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def CoupledLogistic(self, a=1.4, b=3.0):
        x, y = self.trajectory.coupled_logistic(a, b, 0.3, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def CrossChaotic(self, a=0.9, b=1.65):
        x, y = self.trajectory.cross_chaotic(a, b, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def DeJong(self, a=1.7, b=1.7, c=0.6, d=1.2):
        x, y = self.trajectory.dejong(a, b, c, d, 0, 0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def DualHenon(self, a=2.4, b=0.3, c=0.1):
        x, y = self.trajectory.dual_henon(a, b, c, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def ElhadjSprottC(self, a=4.0, b=0.3):
        x, y = self.trajectory.elhadj_sprott_c(a, b, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def FractalDream(self, a=-1.9956, b=-1.4528, c=-2.66206, d=0.8517):
        x, y = self.trajectory.fractal_dream(a, b, c, d, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Gingerbread(self, a=-1.753, b=-1.0):
        x, y = self.trajectory.gingerbread(a, b, 4.0, -2.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def GumowskiMira(self, a=0.008, b=0.05, mu=-0.7):
        x, y = self.trajectory.gumowski_mira(a, b, mu, 0, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def HCA(self, a=1.84, c=-0.35):
        x, y = self.trajectory.hca(a, c, 1, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def HeagyHammel(self, a=3.277, b=0.618, s=0.1):  # Incomplete
        x, y = self.trajectory.heagy_hammel(a, b, s, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Hopalong(self, a=0.4, b=1.0, c=0.0):
        x, y = self.trajectory.hopalong(a, b, c, 0.5, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Ikeda(self, c=0.00, u=0.97):
        x, y = self.trajectory.ikeda(c, u, 0.5, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def JoshiBlackmore(self, a=4.122, b=1.618):
        x, y = self.trajectory.joshi_blackmore(a, b, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def MacMillan(self, a=1.6, b=0.2):  # Incomplete
        x, y = self.trajectory.macmillan(a, b, 0.1, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.map)
        return img

    def Martin(self, a=3.4):
        x, y = self.trajectory.martin(a, 0.1, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def MaynardSmith(self, a=0.87, b=0.75):  # Incomplete
        x, y = self.trajectory.maynard_smith(a, b, 0.0, 0.0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Mira(self, a=0.31, b=1.0):
        x, y = self.trajectory.mira(a, b, 12.0, 3.0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def ModifiedLozi(self, a=-1.81, b=0.3):  # Incomplete
        x, y = self.trajectory.modified_lozi(a, b, 0.5, 0.5)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def ModifiedMira(self, a=0.04, b=1.0):
        x, y = self.trajectory.modified_mira(a, b, -1.0, 8.0)
        agg = self.trajectory.modified_mira
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def MultifoldHenon(self, a=4.0, b=0.9):
        x, y = self.trajectory.multifold_henon(a, b, 1.0, 1.0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Popcorn(self, a=0.05, b=3.0):
        x, y = self.trajectory.popcorn(a, b, 0.6, 0.2)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def ProvenzaleBalmforth(self, a=1.5, b=2.5):
        x, y = self.trajectory.provenzale_balmforth(a, b, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Separatrix(self, a=1.5):  # Incomplete
        x, y = self.trajectory.separatrix(a, 0.0, 1.0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Sine(self, a=2.0, b=0.5):
        x, y = self.trajectory.sine(a, b, 2.0, 2.0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def SineDelay(self, a=3.0, b=0.8):
        x, y = self.trajectory.sine_delay(a, b, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def SineSine(self, a=5.0):
        x, y = self.trajectory.sine_sine(a, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def StrelkovaAnishchenko(self, a=0.9, b=0.285):
        x, y = self.trajectory.strelkova_anishchenko(a, b, 0.1, 1.0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Sunflower(self, a=-1.76, b=2.0, c=0.1, d=0.75):
        x, y = self.trajectory.sunflower(a, b, c, d, 1.86, 1.86)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Svensson(self, a=1.4, b=1.4, c=1.4, d=1.4):
        x, y = self.trajectory.svensson(a, b, c, d, 0, 0)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Tinkerbell(self, a=0.90, b=-0.601, c=2.0, d=0.5):
        x, y = self.trajectory.tinkerbell(a, b, c, d, -0.72, -0.64)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def Ushiki(self, a=3.7, b=0.1, c=3.7, d=0.15):
        x, y = self.trajectory.ushiki(a, b, c, d, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img

    def YangCao(
        self,
        a=1.3,
        b=4.0,
        c=0.4,
        u=0.9,
        m=4.0,
    ):  # Incomplete
        x, y = self.trajectory.yang_cao(a, b, c, u, m, 0.1, 0.1)
        agg = self._plot(x, y)
        print("Generating image..")
        img = tf.shade(agg, cmap=self.cmap)
        return img


# ----------------------------------------------------------- #
