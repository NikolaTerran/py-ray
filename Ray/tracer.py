from Ray import ray
from Obj import obj
from Cord import cord
import config
import pprint
#R(t) = (1-t)C + tP

class Tracer:
    def __init__(self):
        self.ray_list = []
        for y in range(config.ylim):
           for x in range(config.xlim):
               self.ray_list.append(ray.Ray(x - config.xmax,config.ymax - y,config.pixel_z,y,x))
        #self.ray_list.append(ray.Ray(0 - config.xmax,499 - config.ymax,config.pixel_z,499,499))
    def test(self,obj,layer):
        z = False

        #limit = 100000
        #while index < limit:
        for a in self.ray_list:
            for b in obj.plane:
                z = a.intersect(b)
                if z == True:
                    layer.write(a.px,a.py,b.color)
                    break
            #if z == False:
                #print("not intersecting")


        # for b in obj.plane:
        #     z = self.ray_list[0].intersect(b)
        #     if z == True:
        #         layer.write(self.ray_list[0].px,self.ray_list[0].py,b.color)
        #         break
        # if z == False:
        #     layer.write(self.ray_list[0].px,self.ray_list[0].py,[0,0,0])

        # for a in self.ray_list:
        #     for b in obj.plane:
        #         z = a.intersect(b)
        #         if z == True:
        #             layer.write(a.px,a.py,b.color)
        #             break
        #     if z == False:
        #         layer.write(a.px,a.py,[0,0,0])
        #         #pprint.pprint(z)
