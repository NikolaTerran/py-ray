from Ray import ray
from Obj import obj
from Cord import cord
import config
import pprint
#import threading
import math
import time
import copy
#import multiprocessing
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
        q = multiprocessing.Queue()
        size = int(config.xlim * config.ylim /4)
        # for x in range(config.thread):
        #     t_list.append(multiprocessing.Process(target=self.ray_cast, args=(obj,layer,index,config.thread,q)))
        #     index += 1
        # for x in range(config.thread):
        #     t_list.append(threading.Thread(target=self.ray_cast, args=(obj,layer,index,config.thread)))
        #     index += 1
        # for x in t_list:
        #     x.start()
        #for x in t_list:
            #print(layer.grid[0][0])
            #x.join()
        # print("!")
        # a = 0
        # for x in iter(q.get, None):
        #     print(str(x[0]) + " " + str(x[1]))
        #     layer.write(x[0],x[1],[x[2],x[3],x[4]])
            #print(x)

            #thread.start_new_thread(ray_cast, (obj,index,config.thread,))
    def ray_cast(self,obj,layer,index,step,result):
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
                    # result.extend(self.ray_list[index].py)
                    # result.extend(self.ray_list[index].px)
                    # result.extend(colour[0])
                    # result.extend( colour[1])
                    # result.extend( colour[2])
                    #print(str(result[2]) + " " + str(result[3]) + " " + str(result[4]))
                    #time.sleep(5)
                    result.put([self.ray_list[index].py,self.ray_list[index].px,colour[0],colour[1],colour[2]])
                    #layer.write(self.ray_list[index].py,self.ray_list[index].px,colour)
                    break
            debug += 1
            index += step
            print(str(debug/(config.xlim * config.ylim) * config.thread * 100) + "%")
            # if debug >= 200000:
            #     break
    def works(self,obj,layer):
        z = False
        debug = 0
        for a in self.ray_list:
            for b in obj.plane:
                z = a.intersect(b)
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
                    # result.extend(self.ray_list[index].py)
                    # result.extend(self.ray_list[index].px)
                    # result.extend(colour[0])
                    # result.extend( colour[1])
                    # result.extend( colour[2])
                    #print(str(result[2]) + " " + str(result[3]) + " " + str(result[4]))
                    #time.sleep(5)
                    #result.put([self.ray_list[index].py,self.ray_list[index].px,colour[0],colour[1],colour[2]])
                    layer.write(a.py,a.px,colour)
                    break
            debug += 1
            print(str(debug/(config.xlim * config.ylim) * 100) + "%")
            # if debug >= 200000:
            #     break
    def debug(self,index):
        time.sleep(5)
        print("thread#" + str(index) + " slept for 5 sec")
