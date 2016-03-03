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
from skimage.morphology import remove_small_objects


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

    return dist


def coins_image():
    im = coins()

    thresh_im = thresholds(im)

    return thresh_im


def remove_small_holes(ar, min_size=64, connectivity=1, in_place=False):
    """Remove continguous holes smaller than the specified size.
    Parameters
    ----------
    ar : ndarray (arbitrary shape, int or bool type)
        The array containing the connected components of interest.
    min_size : int, optional (default: 64)
        The hole component size.
    connectivity : int, {1, 2, ..., ar.ndim}, optional (default: 1)
        The connectivity defining the neighborhood of a pixel.
    in_place : bool, optional (default: False)
        If `True`, remove the connected components in the input array itself.
        Otherwise, make a copy.
    Raises
    ------
    TypeError
        If the input array is of an invalid type, such as float or string.
    ValueError
        If the input array contains negative values.
    Returns
    -------
    out : ndarray, same shape and type as input `ar`
        The input array with small holes within connected components removed.
    Examples
    --------
    >>> from skimage import morphology
    >>> a = np.array([[1, 1, 1, 1, 1, 0],
    ...               [1, 1, 1, 0, 1, 0],
    ...               [1, 0, 0, 1, 1, 0],
    ...               [1, 1, 1, 1, 1, 0]], bool)
    >>> b = morphology.remove_small_holes(a, 2)
    >>> b
    array([[ True,  True,  True,  True,  True, False],
           [ True,  True,  True,  True,  True, False],
           [ True, False, False,  True,  True, False],
           [ True,  True,  True,  True,  True, False]], dtype=bool)
    >>> c = morphology.remove_small_holes(a, 2, connectivity=2)
    >>> c
    array([[ True,  True,  True,  True,  True, False],
           [ True,  True,  True, False,  True, False],
           [ True, False, False,  True,  True, False],
           [ True,  True,  True,  True,  True, False]], dtype=bool)
    >>> d = morphology.remove_small_holes(a, 2, in_place=True)
    >>> d is a
    True
    Notes
    -----
    If the array type is int, it is assumed that it contains already-labeled
    objects. The labels are not kept in the output image (this function always
    outputs a bool image). It is suggested that labeling is completed after
    using this function.
    """
    _check_dtype_supported(ar)

    #Creates warning if image is an integer image
    if ar.dtype != bool:
        warn("Any labeled images will be returned as a boolean array. "
             "Did you mean to use a boolean array?", UserWarning)

    if in_place:
        out = ar
    else:
        out = ar.copy()

    #Creating the inverse of ar
    if in_place:
        out = np.logical_not(out,out)
    else:
        out = np.logical_not(out)

    #removing small objects from the inverse of ar
    out = remove_small_objects(out, min_size, connectivity, in_place)

    if in_place:
        out = np.logical_not(out,out)
    else:
        out = np.logical_not(out)

    return out


def run_coins():
    thresh_im = coins_image()

    return medial(thresh_im)

medial_coins = run_coins()
