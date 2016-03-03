"""Set of functions to calculate the medial axis transform

Steps involved:
1.  Thresholding an image to create a binary image
2.  Find all boundary pixels in the image.
3.  For each non-boundary pixel find the distance to the
    nearest boundary pixel, using Euclidean distance
4.  Calculate Laplacian of the distance image.
5.  Items with large values in the Laplacian image are 
    considered to be part of the medial axis"""

import numpy as np
import matplotlib as plt
from scipy.misc import imsave
from scipy.ndimage.filters import laplace
from scipy.ndimage.morphology import distance_transform_edt
from skimage.data import coins
from thresholds import thresholds

def medial(image, visualise=False):
    """Creates a medial axis transform image

    Args
    ----
    image: ndarray
        The image of which the medial axis is to be calculated.
        This should be a binary image.
    visualise: bool
        Option to visualise the medial axis transform.

    Returns
    -------
    out: ndarray
        A boolean image with the medial axis pixels
    """
    # Remove noise and make sure it's thresholded
    im = thresholds(image)

    # Calculate distance to all border pixels for each non-border pixel
    dist = distance_transform_edt(im)

    # Calculate laplacian
    laplace(dist, mode="constant")

    return dist


def coins_image():
    im = coins()

    thresh_im = thresholds(im)

    return thresh_im


def run_rect():

    rect = np.ones((256, 256))

    rect[20:50, 20:70] = 1

    return medial(rect)

def run_coins():
    thresh_im = coins_image()
    imsave("coins.png", thresh_im)
    return medial(thresh_im)

medial_coins = run_coins()
imsave("output.png", medial_coins)
