from trajectory import *
from datashader.utils import export_image
import matplotlib.pyplot as plt


# Testing OOP principles


class Attractor:
    def __init__(self, cmap=inferno):
        self.trajectory = Trajectory()
        self.cmap = cmap

    def _plot(self, x, y):
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
