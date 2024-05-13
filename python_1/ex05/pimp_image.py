import numpy as np
import matplotlib.pyplot as plt


def ft_red(image):
    """
    Apply a red filter to the given image.

    Parameters:
    image (numpy.ndarray): The input image.

    Returns:
    None
    """
    if image is not None:
        red_filter_image = image * np.array([1, 0, 0])
        plt.imshow(red_filter_image)
        plt.show()


def ft_green(image):
    """
    Apply a green filter to the image.

    Parameters:
    image (numpy.ndarray): The input image.

    Returns:
    None
    """
    if image is not None:
        green_filter_image = image.copy()
        green_filter_image[:, :, 0] -= green_filter_image[:, :, 0]
        green_filter_image[:, :, 2] -= green_filter_image[:, :, 2]
        plt.imshow(green_filter_image)
        plt.show()


def ft_blue(image):
    """
    Applies a blue filter to the given image.

    Parameters:
    image (numpy.ndarray): The input image.

    Returns:
    None
    """
    if image is not None:
        blue_filter_image = image.copy()
        blue_filter_image[:, :, 0] = 0
        blue_filter_image[:, :, 1] = 0
        plt.imshow(blue_filter_image)
        plt.show()


def ft_grey(image):
    """
    Applies a greyscale filter to the given image.

    Parameters:
    image (numpy.ndarray): The input image.

    Returns:
    None
    """
    if image is not None:
        grey_filter_image = image.copy()
        green_chanel = image[:, :, 1]
        grey_filter_image[:, :, 0] = green_chanel
        grey_filter_image[:, :, 2] = green_chanel
        plt.imshow(grey_filter_image)
        plt.show()


def ft_invert(image):
    """
    Applies an invert filter to the given image.

    Paramaters:
    image (numpy.ndarray): The input image.

    Returns:
    None
    """
    if image is not None:
        invert_filter_image = 255 - image
        plt.imshow(invert_filter_image)
        plt.show()
