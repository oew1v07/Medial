import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, RadioButtons
import scipy.misc as misc

from scipy.ndimage.filters import laplace
from scipy.ndimage.morphology import distance_transform_edt
from os import listdir
from os.path import isfile, join
import os

# Images
figureDir = 'Images'
# http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
images = [f for f in listdir(figureDir) if isfile(join(figureDir, f))]
# http://stackoverflow.com/questions/7304117/split-filenames-with-python
imageNames = [fname.rsplit('.', 1)[0].capitalize() for fname in os.listdir(figureDir)]
filenames = dict(zip(imageNames[0::1], images[0::1]))

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.25, bottom=0.25)
min0 = 0
max0 = 25000

im = misc.imread(os.path.join(figureDir,filenames[imageNames[0]]))
im1 = ax.imshow(im)
distanceImage = distance_transform_edt(im)
lapImage = laplace(distanceImage, mode="constant")
skeleton = lapImage < 0
resultImage = np.logical_and(np.logical_not(skeleton), im )
def loadImage(filename):
    global im
    global distanceImage
    global lapImage
    global skeleton
    global resultImage
    global im1

    im = misc.imread(filename)
    distanceImage = distance_transform_edt(im)
    lapImage = laplace(distanceImage, mode="constant")
    skeleton = lapImage < 0
    resultImage = np.logical_and(np.logical_not(skeleton), im )
    im1 = ax.imshow(im)

distanceAxes = plt.axes([0.05, 0.145, 0.2, 0.04])
distanceButton = Button(distanceAxes, 'Distance', hovercolor='0.975')
def showDistance(event):
    im1 = ax.imshow(distanceImage)
    plt.draw()
distanceButton.on_clicked(showDistance)

laplaceAxes = plt.axes([0.3, 0.145, 0.2, 0.04])
laplaceButton = Button(laplaceAxes, 'Laplacian', hovercolor='0.975')
def showLaplace(event):
    im1 = ax.imshow(lapImage)
    plt.draw()
laplaceButton.on_clicked(showLaplace)

thresholdAxes = plt.axes([0.55, 0.145, 0.2, 0.04])
thresholdButton = Button(thresholdAxes, 'Threshold', hovercolor='0.975')
def showThresholdedevent(event):
    im1 = ax.imshow(skeleton)
    plt.draw()
thresholdButton.on_clicked(showThresholdedevent)

allStagesAxes = plt.axes([0.05, 0.045, 0.2, 0.04])
allStagesButton = Button(allStagesAxes, 'Result', hovercolor='0.975')
def showResult(event):
    im1 = ax.imshow(resultImage)
    plt.draw()
allStagesButton.on_clicked(showResult)

originalAx = plt.axes([0.55, 0.045, 0.2, 0.04])
originalButton = Button(originalAx, 'Original', hovercolor='0.975')
def showOriginal(event):
    im1 = ax.imshow(im)
    plt.draw()
originalButton.on_clicked(showOriginal)

# Choose the input image and reload it
imageChoiceAx = plt.axes([0.025, 0.25, 0.2, 0.6])
imageChoice = RadioButtons(imageChoiceAx, imageNames, active=0)
def changeImage(label):
    loadImage(os.path.join(figureDir,filenames[label]))
    plt.draw()
imageChoice.on_clicked(changeImage)
changeImage(imageNames[0])


plt.show()
