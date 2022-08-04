import os

import cv2
import numpy as np


def save_binary_array(binary_array):
    """
    Helper method that saves a binary array in a txt file.
    :param binary_array: a 2d array.
    :return: txt file.
    """
    for i in range(100):
        if os.path.exists(f"binary_array_{str(i)}.txt"):
            continue
        else:
            np.savetxt(f"binary_array_{str(i)}.txt", binary_array, fmt='%d')
            break


def save_binary_image(img):
    """
    Hlper method that saves a binary image as a png file.
    :param img: a binary image.
    :return: png file.
    """
    for i in range(100):
        if os.path.exists(f"binary_image_{str(i)}.png"):
            continue
        else:
            cv2.imwrite(f"binary_image_{str(i)}.png", img)
            break
