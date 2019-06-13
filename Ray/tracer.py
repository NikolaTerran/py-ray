from Ray import ray
from Obj import obj
from Cord import cord
import config
import pprint
import threading
import math
import time
import copy
#R(t) = (1-t)C + tP

class Tracer:
    def __init__(self):
        self.ray_list = []
        for y in range(config.ylim):
           for x in range(config.xlim):
               self.ray_list.append(ray.Ray(x - config.xmax,config.ymax - y,config.pixel_z,y,x))
        #self.ray_list.append(ray.Ray(0 - config.xmax,499 - config.ymax,config.pixel_z,499,499))
    def test(self,obj,layer):
        index = 0
        t_list = []
        for x in range(config.thread):
            t_list.append(threading.Thread(target=self.ray_cast, args=(copy.deepcopy(obj),layer,index,config.thread)))
            index += 1
        # for x in range(config.thread):
        #     t_list.append(threading.Thread(target=self.ray_cast, args=(obj,layer,index,config.thread)))
        #     index += 1
        for x in t_list:
            x.start()
        for x in t_list:
            x.join()
            #thread.start_new_thread(ray_cast, (obj,index,config.thread,))
    def ray_cast(self,obj,layer,index,step):
        z = False
        debug = 0
        while index < (config.xlim * config.ylim):
            for b in obj.plane:
                z = self.ray_list[index].intersect(b)
                if z[0] == True:
                    colour = b.color.copy()
                    # print("x: " + str(z[2][0]) + ":y: " + str(z[2][1]) + ":z: " + str(z[2][2]))
                    shadow_ray = ray.Ray(z[2][0],z[2][1],z[2][2],0,0,
                         config.light_x,config.light_y,config.light_z)
                    for c in obj.plane:
                        if id(c) == id(b):
                            continue
                        sec = shadow_ray.intersect(c)
                        #print(str(a.px) + " :x y:" + str(a.py))
                        if sec[0] == True:
                            # print("debug:" + str(debug))
                            # print(z[2])
                            # print(str(c.cord[0].x) + " " + str(c.cord[0].y) + " " + str(c.cord[0].z))
                            # print(str(c.cord[1].x) + " " + str(c.cord[1].y) + " " + str(c.cord[1].z))
                            # print(str(c.cord[2].x) + " " + str(c.cord[2].y) + " " + str(c.cord[2].z))
                            # print(sec[2])
                            # print(str(b.cord[0].x) + " " + str(b.cord[0].y) + " " + str(b.cord[0].z))
                            # print(str(b.cord[1].x) + " " + str(b.cord[1].y) + " " + str(b.cord[1].z))
                            # print(str(b.cord[2].x) + " " + str(b.cord[2].y) + " " + str(b.cord[2].z))
                            d0 = math.sqrt(math.pow(z[2][0] - config.light_x,2) +
                                math.pow(z[2][1] - config.light_y,2) +
                                math.pow(z[2][2] - config.light_z,2))
                            d1 = math.sqrt(math.pow(sec[2][0] - z[2][0],2) +
                                math.pow(sec[2][1] - z[2][1],2) +
                                math.pow(sec[2][2] - z[2][2],2))

                            if d0 > d1:
                                colour[0] = 0
                                colour[1] = 0
                                colour[2] = 0
                                break
                    #print(str(a.px) + ":px py:" + str(a.py))

                    layer.write(self.ray_list[index].py,self.ray_list[index].px,colour)
                    break
            debug += 1
            index += step
            print(str(debug/(config.xlim * config.ylim) * config.thread * 100) + "%")
            # if debug >= 200000:
            #     break
    def debug(self,index):
        time.sleep(5)
        print("thread#" + str(index) + " slept for 5 sec")
