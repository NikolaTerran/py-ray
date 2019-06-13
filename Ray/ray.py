import config
from Vector import vector3 as vec3
from Cord import cord
from Obj import obj
import pprint
import numpy as np
import time

#R(t) = (1-t)C + tP

class Ray:
    def __init__(self,x0=0,y0=0,z0=0,
        py=0,px=0,x1=0,y1=0,z1=0,):
        #self.dir = vec3.Vector(x0,y0,z0,x1,y1,z1)
        self.origin = cord.Cord(x1,y1,z1)
        self.target = cord.Cord(x0,y0,z0)
        self.px = px
        self.py = py
        self.color = []
    def intersect(self,plane):
        tx = self.target.x
        ty = self.target.y
        tz = self.target.z

        ox = self.origin.x
        oy = self.origin.y
        oz = self.origin.z

        #print("ox:" + str(ox) + "oy:" + str(oy) + "oz:" + str(oz))

        # cx - tcx + tpx = Rx(t)
        #Ix = cx - tcx + tpx
        new_d = plane.d - plane.vec3.x * ox - plane.vec3.y * oy - plane.vec3.z * oz
        denom = plane.vec3.x * (tx - ox) + plane.vec3.y * (ty - oy) + plane.vec3.z * (tz - oz)

        if denom != 0: #parrallel
            t = new_d / denom
            array = [ox - t * ox + t * tx, oy - t * oy + t * ty, oz - t * oz + t * tz]

            # print(array)
            I1 = [plane.cord[0].x, plane.cord[1].x, plane.cord[2].x]
            I2 = [plane.cord[0].y, plane.cord[1].y, plane.cord[2].y]
            I3 = [plane.cord[0].z, plane.cord[1].z, plane.cord[2].z]
            solution = [array[0],array[1],array[2]]
            a = np.array([I1, I2, I3])
            b = np.array(solution)
            try:
                c = np.linalg.solve(a, b)
                # print(c)
                if((c >= 0).all()):
                    #print(str(array))
                    d = [True,t,array]
                    return d
            except:
                d = [False]
                return d
            d = [False]
            return d
        else:
            #print(str(self.px) + ":x y:" + str(self.py))
            d = [False]
            #print(plane.id)
            return d
