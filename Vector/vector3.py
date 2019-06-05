import math
from Transformable import trans

class Vector(trans.Transformable):
    def __init__(self,x0=0,y0=0,z0=0,x1=0,y1=0,z1=0):
        self.x = x0 - x1
        self.y = y0 - y1
        self.z = z0 - z1
        #self.normalize()
    def normalize(self):
        constant = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        #print(constant)
        #if self.x == 0 & self.y == 0 & self.z == 0:
        #    pass
        #else:
        self.x = self.x/constant
        self.y = self.y/constant
        self.z = self.z/constant

        #print(str(self.x) + " " + str(self.y) + " " + str(self.z))
    def cross(self,v):
        # print(type(v))
        holdx = self.x
        holdy = self.y
        holdz = self.z
        self.x = holdy * v.z - holdz * v.y
        self.y = holdz * v.x - holdx * v.z
        self.z = holdx * v.y - holdy * v.x
        self.normalize()
    def dot(self,v):
        return self.x * v.x + self.y * v.y + self.z * v.z
