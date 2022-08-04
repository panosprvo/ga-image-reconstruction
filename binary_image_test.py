import numpy
from binary_image import *


def test_create_random_binary_image1():
    binary_image = BinaryImage()
    binary_image.config.GENOME_LENGTH = 16
    img = binary_image.create_random_binary_image()
    assert np.sum(img == 255) == 128
    assert np.sum(img == 0) == 128


def test_create_random_binary_image2():
    binary_image = BinaryImage()
    binary_image.config.GENOME_LENGTH = 64
    binary_image.config.WHITE_RATIO = 0.7
    img = binary_image.create_random_binary_image()
    assert np.sum(img == 255) == 2867
    assert np.sum(img == 0) == 1229


def test_binary_image_to_binary_array1():
    binary_image = BinaryImage()
    binary_image.config.GENOME_LENGTH = 32
    img = binary_image.create_random_binary_image()
    binary_array = binary_image.binary_image_to_binary_array(img)
    assert len(binary_array) == 32
    assert len(binary_array[0]) == 32


def test_binary_image_to_binary_array2():
    binary_image = BinaryImage()
    binary_image.config.GENOME_LENGTH = 64
    img = binary_image.create_random_binary_image()
    binary_array = binary_image.binary_image_to_binary_array(img)
    assert len(binary_array) == 64
    assert len(binary_array[0]) == 64


def test_binary_array_to_binary_image1():
    binary_array = numpy.array([[0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 0]])
    binary_image = BinaryImage()
    img = binary_image.binary_array_to_binary_image(binary_array)
    assert np.sum(img == 255) == 8
    assert np.sum(img == 0) == 8
