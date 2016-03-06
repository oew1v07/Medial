import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as misc

from scipy.ndimage.filters import laplace
from scipy.ndimage.morphology import distance_transform_edt


def distance2(image):
    result = np.empty_like(image)

    objectPixels = np.transpose(np.nonzero(image))
    up = np.array([0,1])
    down = np.array([0,-1])
    left = np.array([-1,0])
    right = np.array([1,0])
    sequence = [up, left, down, right]

    for pixel in objectPixels:
        pixelCopy = pixel.copy()
        run = True
        # To allow spiralling 1,1,2,2,3,3..
        distanceIncrement = 0
        # Find the nearest 2 zero pixels
        zeroCount = 0
        zeroLocations = []
        while(run):
            for direction in range(0, 4):
                if((direction == 0) or (direction == 2)):
                    distanceIncrement = distanceIncrement+1

                # Add the distance in that direction
                for x in range(0, distanceIncrement):
                    pixelCopy = pixelCopy+sequence[direction]
                    # If not white, incremenet the zero count
                    try:
                        if(image[pixelCopy].all() ==  False):
                            zeroCount = zeroCount+1
                            zeroLocations.append(pixelCopy)
                            #print(pixelCopy == pixel)
                            if(zeroCount == 2):
                                run = False
                                break
                    except IndexError:
                        pass

        # calculate distance to points
        if(zeroCount >= 2):
            distances = []
            for blackPixel in zeroLocations:
                # Calculate distance
                #print(blackPixel)
                #print(pixel)
                distance = np.linalg.norm(pixel-blackPixel)
                #print(distance)
                distances.append(distance)
            #if(distances[0] == distances[1]):
            #print(distances)
            if(distances.count(min(distances)) > 1):
                #print(distances)
                result[pixel[0], pixel[1]] == True
    return result

im = misc.imread('Images/Bone.gif')
distanceImage = distance_transform_edt(im)
distance2Img = distance2(im)
print(np.count_nonzero(distance2Img))
#resultImage = distanceImage[np.nonzero(distance2Img)]
imgplot = plt.imshow(distance2Img)
plt.show()
