"""write a soft that calculate the volume of a cone"""
#V=1/3*pi*r^2*H

from math import *

def volume(h, r):
    """calculates the volume of a cone"""
    return 1/3*pi*sqrt(r)*h

print("Welcome to the volume calculator")
height=input("Which height is your cone?")
rad=input("Which radius is your cone")

result=volume(int(height), int(rad))
result=round(result,2)
print("Volume is: {} cm³".format(str(result)))

