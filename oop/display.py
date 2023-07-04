from main import *
from PIL import Image
from argparse import ArgumentParser, Namespace
import os
import sys


# Display datashader image:
# ----------------------------------------------------------- #


def display_datashader_image(func):
    """
    Function to display datashader images.

    Parameters:

        func: an attractor function (func)

    """
    export_for_display(func)
    image = Image.open("display.png")
    image.show()

    # Removes exported image from folder after displaying
    curr_path = os.getcwd()
    os.remove(curr_path + "/display.png")
    return


def export_for_display(func):
    """
    Helper function for displaying datashader images.

    Params:
        func: an attractor function (func)
    """
    filename = "display"
    img = func()
    return export_image(img, filename)


# ----------------------------------------------------------- #
if __name__ == "__main__":
    attractor = Attractor(cmap=viridis)
    display_datashader_image(attractor.Ikeda)
