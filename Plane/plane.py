import config
from Cord import cord as co
from Vector import vector3 as vec3
import pprint

class Plane():
    def __init__(self,x0=0,y0=0,z0=0,x1=0,y1=0,z1=0,x2=0,y2=0,z2=0,color=[0,0,0],id=""):
        self.cord = []
        self.cord.append(co.Cord(x0,y0,z0))
        self.cord.append(co.Cord(x1,y1,z1))
        self.cord.append(co.Cord(x2,y2,z2))
        v0 = vec3.Vector(x1,y1,z1,x0,y0,z0)
        v1 = vec3.Vector(x2,y2,z2,x0,y0,z0)
        v1.cross(v0)
        self.vec3 = v1
        self.color = color
        self.d = self.vec3.x * self.cord[0].x + self.vec3.y * self.cord[0].y + self.vec3.z * self.cord[0].z
        self.id = id
        #print(str(self.vec3.x) + " " + str(self.vec3.y) + " "  + str(self.vec3.z))
        #print(self.d)
