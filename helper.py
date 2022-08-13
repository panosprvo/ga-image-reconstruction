# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------

import os

import cv2
import numpy as np


def save_binary_array(binary_array, index):
    """
    Helper method that saves a binary array in a txt file.

    :param index: int. Used to number an array that's being saved.
    :param binary_array: a 2d array.

    :return: txt file.
    """
    np.savetxt(f"binary_array_{str(index)}.txt", binary_array, fmt='%d')


def save_binary_image(img, index):
    """
    Helper method that saves a binary image as a png file.

    :param index: int. Used to number an image that's being saved.
    :param img: a binary image.

    :return: png file.
    """
    path = 'C:/Users/panos/Desktop/msc-computer-science-project/images'
    cv2.imwrite(os.path.join(path, f"binary_image_{str(index)}.png"), img)
