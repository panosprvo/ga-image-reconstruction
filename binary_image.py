from datetime import *
import os
import sys

import cv2
import numpy as np
from PIL import Image as im
from config import Config


def save_binary_array(binary_array):
    for i in range(100):
        if os.path.exists(f"binary_array_{str(i)}.txt"):
            continue
        else:
            np.savetxt(f"binary_array_{str(i)}.txt", binary_array, fmt='%d')
            break


def save_binary_image(img):
    for i in range(100):
        if os.path.exists(f"binary_image_{str(i)}_{datetime.now}.png"):
            continue
        else:
            cv2.imwrite(f"binary_image_{str(i)}_{datetime.now}.png", img)
            break


class BinaryImage:

    def __init__(self):
        self.config = Config()

    def binary_image_to_binary_array(self, img):
        """
        An image of black and white pixels is used to generate a numpy array of 0s and 1s.

        :param img: binary image (*.png).

        :return: a 2D binary array.
        """
        # Convert black and white pixels of the image to an array of binary arrays, each line is a new array.
        # Any pixels that have colour of greater than 0 (not black), are set to 1
        np_img = np.array(img)
        np_img[np_img > 0] = 1

        # TODO: remove this when done
        # Avoid truncation when printing np array
        np.set_printoptions(threshold=sys.maxsize, suppress=True)

        # Convert the image to a binary array.
        binary_array = np_img.astype(int)
        return np.ndarray.tolist(binary_array)

    def binary_array_to_binary_image(self, binary_array):
        """
        Generate a binary image from a binary numpy array.

        :param binary_array: 2d binary array.

        :return: a binary image.
        """
        # Convert the array to a sequence of numbers
        img = np.array(im.fromarray(binary_array * 255))
        return img

    def open_original_image(self):
        """
        This method is used only to convert the original image to be reconstructed to a binary array.

        :return: binary 2D array.
        """
        img = im.open("original_image.png")
        return self.binary_image_to_binary_array(img)


def main():
    return


if __name__ == '__main__':
    main()
