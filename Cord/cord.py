import math
from Transformable import trans
from Vector import vector3 as vec3

class Cord(vec3.Vector):
    def __init__(self,x0,y0,z0):
        self.x = x0
        self.y = y0
        self.z = z0
    def substract(self,v):
        #super.subtract(v)
        super.debug()
    def debug(self):
        print("haha!")
