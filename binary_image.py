import sys

import numpy as np
from PIL import Image as im
from config import Config
from genotype import Genotype


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

        :return: a Genotype object.
        """
        img = im.open("original_image.png")
        optimal_array = self.binary_image_to_binary_array(img)
        optimal_individual = Genotype()
        optimal_individual.genes = optimal_array
        return optimal_individual

    def create_random_binary_image(self):
        """
        A random binary image is generated with dimensions size * size and saved to file.
        :return: a binary image.
        """
        # Generate black image (sequence)
        img = np.zeros((self.config.GENOME_LENGTH * self.config.GENOME_LENGTH, 1), np.uint8)

        # Determine number of white pixels, and set (=255 is white). We arbitrarily set the ratio of white to black
        # pixels to be 50:50. At this point we have an image that is half black and half white.
        img[0:int(self.config.WHITE_RATIO * self.config.GENOME_LENGTH * self.config.GENOME_LENGTH)] = 255

        # Shuffle pixels, and reshape image
        np.random.shuffle(img)
        img = np.reshape(img, (self.config.GENOME_LENGTH, self.config.GENOME_LENGTH))
        return img


def main():
    return


if __name__ == '__main__':
    main()
