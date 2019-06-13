from Obj import obj as obj
from Ray import tracer
import config
from Util import export as ex
import pprint
import time

white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
object0 = obj.Object()


#left
object0.addPolygon(-250,-250,390,
                    -250,250,890,
                    -250,250,390,red,"0")
object0.addPolygon(-250,-250,390,
                    -250,-250,890,
                    -250,250,890,red,"1")
#right
object0.addPolygon(250,-250,390,
                    250,250,390,
                    250,250,890,green,"2")
object0.addPolygon(250,-250,390,
                    250,250,890,
                    250,-250,890,green,"3")
#back
object0.addPolygon(-250,-250,890,
                    250,250,890,
                    -250,250,890,white,"4")
object0.addPolygon(-250,-250,890,
                    250,-250,890,
                    250,250,890,white,"5")
#bot
object0.addPolygon(-250,-250,890,
                    -250,-250,390,
                    250,-250,390,white,"6")

object0.addPolygon(-250,-250,890,
                    250,-250,390,
                    250,-250,890,white,"7")
#top
object0.addPolygon(-250,250,890,
                    -100,250,550,
                    -100,250,750,white,"8")
object0.addPolygon(-250,250,890,
                    -100,250,750,
                    100,250,750,white,"9")
object0.addPolygon(-250,250,890,
                    100,250,750,
                    250,250,890,white,"10")
object0.addPolygon(250,250,890,
                    100,250,750,
                    250,250,390,white,"11")
object0.addPolygon(100,250,750,
                    100,250,550,
                    250,250,390,white,"12")
object0.addPolygon(100,250,550,
                    -100,250,550,
                    250,250,390,white,"13")
object0.addPolygon(-100,250,550,
                    -250,250,390,
                    250,250,390,white,"14")
object0.addPolygon(-100,250,550,
                    -250,250,890,
                    -250,250,390,white,"15")

layer0 = ex.Canvas()
trace0 = tracer.Tracer()

#index = 0
# for x in object0.cord:
#     x.debug()

#pprint.pprint(object0.cord)
start_time = time.time()
trace0.test(object0,layer0)
print("--- tracing took %s seconds ---" % (time.time() - start_time))
#layer0.write(0,0,color)
layer0.push("hi.ppm")
#print(config.xlim)

#When you die and your whole life flashes before your eyes, how much of it do you want to not have ray tracing?
