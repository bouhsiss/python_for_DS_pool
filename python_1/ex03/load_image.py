from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        image_array = np.asarray(Image.open(path))

        print("The shape of image is: ",image_array.shape)
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