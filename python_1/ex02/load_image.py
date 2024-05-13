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
    image_array = []

    try:
        assert isinstance(path, str), "the given path isn't a valid string"
        image_array = np.array(Image.open(path))

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
    except AssertionError as e:
        print("An assertion error has occured: ", e)

    return image_array
