import math

class Transformable:
    def __init__(self,x0,y0,z0):
        self.x = x0
        self.y = y0
        self.z = z0
    def trans(self,x0,y0,z0):
        self.x = self.x + x0
        self.y = self.y + y0
        self.z = self.z + z0
    def rotate(self,axis,radian):
        if(axis == 'x'):
            t = self.y
            self.y = self.y * math.cos(radian) + self.z * -math.sin(radian)
            self.z = t * math.sin(radian) + self.z * math.cos(radian)
        if(axis == 'y'):
            t = self.x
            self.x = self.x * math.cos(radian) + self.z * math.sin(radian)
            self.z = t * -math.sin(radian) + self.z * math.cos(radian)
        if(axis == 'z'):
            t = self.x
            self.x = self.x * math.cos(radian) + self.y * -math.sin(radian)
            self.y = t * math.sin(radian) + self.y * math.cos(radian)
    def dilate(self,x,y,z):
        self.x = self.x * self.x
        self.y = self.y * self.y
        self.z = self.z * self.z
