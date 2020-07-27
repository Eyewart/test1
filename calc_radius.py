"""create a class "Cercle" which defines itself by its radius
two methods within this class: to calculate surface pi*r² and perimeter 2piR
code a soft that create an instance of this object and use these methods"""

import math

pi = math.pi

class Cercle:

    def __init__(self, radius):
        self.radius=radius

    def calc_s(self):
        return pi*math.sqrt(self.radius)

    def calc_p(self):
        return 2*pi*self.radius

