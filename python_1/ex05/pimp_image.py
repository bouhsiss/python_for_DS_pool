import numpy as np
import matplotlib.pyplot as plt

def ft_red(image):
    red_filter_image = image * np.array([1, 0, 0])
    plt.imshow(red_filter_image)
    plt.show()

def ft_green(image):
    green_filter_image = image.copy()
    green_filter_image[:, :, 0] -= green_filter_image[:, :, 0]
    green_filter_image[:, :, 2] -= green_filter_image[:, :, 2]
    plt.imshow(green_filter_image)
    plt.show()

def ft_blue(image):
    blue_filter_image = image.copy()
    blue_filter_image[:, :, 0] = 0
    blue_filter_image[:, :, 1] = 0
    plt.imshow(blue_filter_image)
    plt.show()

def ft_grey(image):
    grey_filter_image = np.sum(image, axis=2) / 3
    plt.imshow(grey_filter_image, cmap='gray')
    plt.show()