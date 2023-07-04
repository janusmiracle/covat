from main import *

# Export datashader image into specified path:

# ----------------------------------------------------------- #


def export_datashader_image(func, path):
    """
    Function to export datashader images.

    Parameters:

        func: an attractor function (func)
        path: the output path for the image (str)
    """
    filename = func.__name__
    img = func()
    print("Export Complete. Image labelled {}.png at {}.".format(filename, path))
    return export_image(img, filename, export_path=path)


# ----------------------------------------------------------- #

export_datashader_image(Hopalong, "<path>")
