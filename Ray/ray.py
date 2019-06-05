import config
from Vector import vector3 as vec3
from Cord import cord

class Ray:
    def __init__(self,x0=0,y0=0,z0=0,x1=0,y1=0,z1=0,px,py):
        self.dir = vec3.Vector(x0,y0,z0,x1,y1,z1)
        self.origin = cord.Cord(x1,y1,z1)
        self.px = px
        self.py = py
        self.color = []
