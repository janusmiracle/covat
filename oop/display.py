from main import *
from PIL import Image
from argparse import ArgumentParser, Namespace
import os

# Display datashader image:


# ----------------------------------------------------------- #
def display_datashader_image(func):
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
        func: function
            an attractor function.
    """
    filename = "display"
    img = func()
    return export_image(img, filename)


# ----------------------------------------------------------- #
if __name__ == "__main__":
    attractor = Attractor()
    display_datashader_image(attractor.Arnold)
