from load_image import ft_load
from utils import zoom_image, display, rgb_to_gray
import numpy as np


def transpose_image(image_array):
    print(len(image_array))
    transpose_image = [[image_array[j][i] for j in range(len(image_array))] for i in range(len(image_array[0]))]
    return np.array(transpose_image)

def main():
    image_array = ft_load("python_1/ex03/animal.jpeg")

    if not image_array is None:
        zoomed_image = zoom_image(image_array)
        transposed_image = transpose_image(zoomed_image)
        print("New shape after Transposing: ",transposed_image.shape)
        print(transposed_image)
        display(rgb_to_gray(transposed_image))

if __name__ == "__main__":
    main()