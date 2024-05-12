from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoom(image_array: np.ndarray):
    center_y, center_x = image_array.shape[0]//2, image_array.shape[1]//2

    start_x = max(0, center_x - 75)
    end_x = min(image_array.shape[1], center_x + 325)
    start_y = max(0, center_y - 285)
    end_y = min(image_array.shape[0], center_y + 115)

    cropped_image = image_array[start_y:end_y, start_x:end_x]
    return cropped_image


def rgb_to_gray(image_array: np.ndarray):
    R = image_array[:, :, 0]
    G = image_array[:, :, 1]
    B = image_array[:, :, 2]

    grayscale_image = 0.299*R + 0.587*G + 0.114*B
    return grayscale_image


def display(image_array: np.ndarray):
    plt.imshow(image_array, cmap='gray')

    plt.show()


def main():
    image_array = ft_load("python_1/ex03/animal.jpeg")

    if image_array is None:
        zoomed_image = zoom(image_array)
        grayscale_image = rgb_to_gray(zoomed_image)
        print("New shape after slicing: ", grayscale_image.shape)
        print(grayscale_image)
        display(grayscale_image)


if __name__ == "__main__":
    main()
