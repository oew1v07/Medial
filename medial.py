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
from scipy.ndimage.filters import laplace
from skimage.data import coins

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

    # Find border pixel locations of boolean image

    # Create empty distance image
    dist = np.zeros(image.shape)

    # Label all border pixels to have a distance of zero in distance image

    # Calculate distance to all border pixels for each non-border pixel

    # 

def coins():
    """Thresholds and removes noise of coins image

    Returns
    -------
    out: ndarray (bool)
    """
