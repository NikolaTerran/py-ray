import math

class Vector:
    def __init__(self,x0=0,y0=0,z0=0,x1=0,y1=0,z1=0):
        self.x = x0 - x1
        self.y = y0 - y1
        self.z = z0 - z1
    def normalize(self):
        constant = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x = self.x/constant
        self.y = self.y/constant
        self.z = self.z/constant
    def cross(self,v):
        print(type(v))
        # holdx = self.x
        # holdy = self.y
        # holdz = self.z
        # self.x = self.y * v.z - self.z * v.y
    	# self.y = self.z * v.x - self.x * v.z
    	# self.z = self.x * v.y - self.y * v.x
        self.normalize()
