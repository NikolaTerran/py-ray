import math
from Transformable import trans

class Cord(trans.Transformable):
    def __init__(self,x0,y0,z0):
        self.x = x0
        self.y = y0
        self.z = z0
