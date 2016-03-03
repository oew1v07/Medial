from os.path import exists
from PIL.Image import open
import numpy as np


def apple():
    if exists("Images/apple.gif"):
        out = np.asarray(open("Images/apple.gif"))
    else:
        out = None

    return out

def bat():
    if exists("Images/bat.gif"):
        out = np.asarray(open("Images/bat.gif"))
    else:
        out = None

    return out

def beetle():
    if exists("Images/beetle.gif"):
        out = np.asarray(open("Images/beetle.gif"))
    else:
        out = None

    return out

def bell():
    if exists("Images/bell.gif"):
        out = np.asarray(open("Images/bell.gif"))
    else:
        out = None

    return out

def bone():
    if exists("Images/Bone.gif"):
        out = np.asarray(open("Images/Bone.gif"))
    else:
        out = None

    return out

def butterfly():
    if exists("Images/butterfly.gif"):
        out = np.asarray(open("Images/butterfly.gif"))
    else:
        out = None

    return out

def camel():
    if exists("Images/camel.gif"):
        out = np.asarray(open("Images/camel.gif"))
    else:
        out = None

    return out

def chopper():
    if exists("Images/chopper.gif"):
        out = np.asarray(open("Images/chopper.gif"))
    else:
        out = None

    return out

def deer():
    if exists("Images/deer.gif"):
        out = np.asarray(open("Images/deer.gif"))
    else:
        out = None

    return out

def device1():
    if exists("Images/device1.gif"):
        out = np.asarray(open("Images/device1.gif"))
    else:
        out = None

    return out

def device2():
    if exists("Images/device2.gif"):
        out = np.asarray(open("Images/device2.gif"))
    else:
        out = None

    return out

def elephant():
    if exists("Images/elephant.gif"):
        out = np.asarray(open("Images/elephant.gif"))
    else:
        out = None

    return out


def frog():
    if exists("Images/frog.gif"):
        out = np.asarray(open("Images/frog.gif"))
    else:
        out = None

    return out

def hammer():
    if exists("Images/hammer.gif"):
        out = np.asarray(open("Images/hammer.gif"))
    else:
        out = None

    return out

def turtle():
    if exists("Images/turtle.gif"):
        out = np.asarray(open("Images/turtle.gif"))
    else:
        out = None

    return out

appleImage = apple()
batImage = bat()
beetleImage = beetle()
bellImage = bell()
boneImage = bone()
butterflyImage = butterfly()
camelImage = camel()
chopperImage = chopper()
deerImage = deer()
device1Image = device1()
device2Image = device2()
elephantImage = elephant()
frogImage = frog()
hammerImage = hammer()
turtleImage = turtle()