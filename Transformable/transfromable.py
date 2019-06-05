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
            self.y = self.y * cos(radian) + self.z * -sin(radian)
            self.z = t * sin(radian) + self.z * cos(radian)
        if(axis == 'y'):
            t = self.x
            self.x = self.x * cos(radian) + self.z * sin(radian)
            self.z = t * -sin(radian) + self.z * cos(radian)
        if(axis == 'z'):
            t = self.x
            self.x = self.x * cos(radian) + self.y * -sin(radian)
            self.y = t * sin(radian) + self.y * cos(radian)
    def dilate(self,x,y,z):
        self.x = self.x * self.x
        self.y = self.y * self.y
        self.z = self.z * self.z
