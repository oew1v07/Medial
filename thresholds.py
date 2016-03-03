import numpy as np
from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects
from misc import remove_small_holes

def thresholds(image):
    """Thresholds and removes noise of image

    Returns
    -------
    thresh_im: ndarray
    """

    threshold = threshold_otsu(image)

    thresh_im = image > threshold

    thresh_im = remove_small_holes(thresh_im)

    thresh_im = remove_small_objects(thresh_im)

    return thresh_im