from os.path import exists
from PIL.Image import open
import numpy as np


def apple():
    if exists("apple.gif"):
        out = np.asarray(open("Images/apple.gif"))
    else:
        out = None

    return out

def bat():
    if exists("bat.gif"):
        out = np.asarray(open("Images/bat.gif"))
    else:
        out = None

    return out

def beetle():
    if exists("beetle.gif"):
        out = np.asarray(open("Images/beetle.gif"))
    else:
        out = None

    return out

def bell():
    if exists("bell.gif"):
        out = np.asarray(open("Images/bell.gif"))
    else:
        out = None

    return out

def bone():
    if exists("Bone.gif"):
        out = np.asarray(open("Images/Bone.gif"))
    else:
        out = None

    return out

def butterfly():
    if exists("butterfly.gif"):
        out = np.asarray(open("Images/butterfly.gif"))
    else:
        out = None

    return out

def camel():
    if exists("camel.gif"):
        out = np.asarray(open("Images/camel.gif"))
    else:
        out = None

    return out

def chopper():
    if exists("chopper.gif"):
        out = np.asarray(open("Images/chopper.gif"))
    else:
        out = None

    return out

def deer():
    if exists("deer.gif"):
        out = np.asarray(open("Images/deer.gif"))
    else:
        out = None

    return out

def device1():
    if exists("device1.gif"):
        out = np.asarray(open("Images/device1.gif"))
    else:
        out = None

    return out

def device2():
    if exists("device2.gif"):
        out = np.asarray(open("Images/device2.gif"))
    else:
        out = None

    return out

def elephant():
    if exists("elephant.gif"):
        out = np.asarray(open("Images/elephant.gif"))
    else:
        out = None

    return out


def frog():
    if exists("frog.gif"):
        out = np.asarray(open("Images/frog.gif"))
    else:
        out = None

    return out

def hammer():
    if exists("hammer.gif"):
        out = np.asarray(open("Images/hammer.gif"))
    else:
        out = None

    return out

def turtle():
    if exists("turtle.gif"):
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