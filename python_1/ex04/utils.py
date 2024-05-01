import matplotlib.pyplot as plt
import numpy as np

def zoom_image(image_array: np.ndarray):
    center_y, center_x = image_array.shape[0]//2, image_array.shape[1]//2

    
    start_x, end_x = max(0, center_x - 75), min(image_array.shape[1], center_x + 325)
    start_y, end_y = max(0, center_y - 285), min(image_array.shape[0], center_y + 115)


    cropped_image = image_array[start_y:end_y, start_x:end_x]
    return cropped_image

def rgb_to_gray(image_array: np.ndarray):
    R,G,B = image_array[:,:,0], image_array[:,:,1], image_array[:,:,2]
    
    grayscale_image = 0.299*R + 0.587*G + 0.114*B
    return grayscale_image

def display(image_array: np.ndarray):
    plt.imshow(image_array, cmap='gray')

    plt.show()   
