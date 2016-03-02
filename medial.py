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
from skimage.feature import canny
from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_holes, remove_small_objects

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

    # Find border pixel locations of boolean image
    # Do canny on the boolean image
    edgeImage = canny(im)

    # Find points where boundaries are
    edges_y, edges_x = np.nonzero(edgeImage)

    # Find where thresholded image points are nonzero

    im_y, im_x = np.nonzero(im)

    # Create empty distance image
    dist = np.zeros(image.shape)

    # Calculate distance to all border pixels for each non-border pixel
    for i, y_im in enumerate(im_y):
        dists = []
        # x_im = im_x[i]
        for j, y_ed in enumerate(edges_y):
            # x_ed = edges_x[j]
            new_dist = np.sqrt((y_im - y_ed)**2 + (im_x[i] - edges_x[j])**2)
            dists.append(new_dist)

        dist[y_im, im_x[i]] = min(dists)

def thresholds(image):
    """Thresholds and removes noise of image

    Returns
    -------
    thresh_im: ndarray (bool)
    """

    threshold = threshold_otsu(image)

    thresh_im = image > threshold

    thresh_im = remove_small_holes(thresh_im)

    thresh_im = remove_small_objects(thresh_im)

    return thresh_im

def coins():
    im = coins()

    thresh_im = thresholds(im)

    return thresh_im

