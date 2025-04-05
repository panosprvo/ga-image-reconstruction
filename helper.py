# --------------------------------------------
# 2022, Panagiotis Provias, London, U.K.
# email: panayiotisprovias@gmail.com
# --------------------------------------------
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import os
import cv2
import numpy as np


def save_binary_array(binary_array, index):
    """
    Helper function that saves a binary array in a txt file.

    :param index: int. Used to number an array that's being saved.
    :param binary_array: a 2d array.

    :return: txt file.
    """
    np.savetxt(f"binary_array_{str(index)}.txt", binary_array, fmt='%d')


def save_binary_image(img, index, crossover_operator):
    """
    Helper function that saves a binary image as a png file.

    :param crossover_operator: character to be added to the front of the filename.
    :param index: int. Used to number an image that's being saved.
    :param img: a binary image.

    :return: png file.
    """
    path = os.path.join(os.getcwd(), "images")  # Save in the script's directory
    os.makedirs(path, exist_ok=True)  # Ensure the directory exists
    filename = os.path.join(path, f"{crossover_operator}_binary_image_{index}.png")
    cv2.imwrite(filename, img)


def create_plot(generation_list, fitness_list, crossover_operator):
    """
    Helper function that creates and saves a plot.

    :param crossover_operator: character to be added to the front of the filename.
    :param generation_list: a list holding numbers of all generations.
    :param fitness_list: a list holding the maximum fitness of each generation.

    :return: a plot.
    """
    plt.plot(generation_list, fitness_list)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    current_dir = Path(__file__).parent
    path = current_dir / 'images' / f'{crossover_operator}_plot.png'
    plt.savefig(path)
    plt.show()
