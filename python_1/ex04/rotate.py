from load_image import ft_load
from utils import zoom_image, display, rgb_to_gray
import numpy as np


def transpose_image(image_array):
    """
    Transposes the given image array.

    Args:
        image_array (numpy.ndarray): The input image array.

    Returns:
        numpy.ndarray: The transposed image array.
    """
    transpose_image = [
        [image_array[j][i] for j in range(len(image_array))]
        for i in range(len(image_array[0]))
    ]
    return np.array(transpose_image)


def main():
    image_array = ft_load("ex03/animal.jpeg")
    print(image_array)

    if image_array is not None:
        zoomed_image = zoom_image(image_array)
        transposed_image = transpose_image(zoomed_image)
        print("New shape after Transposing: ", transposed_image.shape)
        print(transposed_image)
        display(rgb_to_gray(transposed_image))


if __name__ == "__main__":
    main()
