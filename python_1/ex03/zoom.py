from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

image_array = ft_load("python_1/ex03/animal.jpeg")

center_y, center_x = image_array.shape[0]//2, image_array.shape[1]//2

start_x, end_x = center_x - 75, center_x + 325
start_y, end_y = center_y - 285, center_y + 115


cropped_image = image_array[start_y:end_y, start_x:end_x]

grayscale_image = np.mean(cropped_image, axis=-1, keepdims=True).astype(int)
print(grayscale_image.shape)
print(grayscale_image)

plt.imshow(grayscale_image, cmap='gray')

plt.show()