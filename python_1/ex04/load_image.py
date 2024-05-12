from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    This function takes as a parameter a path to an image file, loads the \
image, prints its format, and returns its pixel values in RGB format.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The pixel values of the image in RGB format.
    """

    try:
        image_array = np.asarray(Image.open(path))

        print("The shape of image is: ", image_array.shape)
    except FileNotFoundError as e:
        print("The file cannot be found: ", e)
        return None
    except PermissionError as e:
        print("The file can't be opened: ", e)
        return None
    except UnidentifiedImageError as e:
        print("The file is not an image: ", e)
        return None

    return image_array
