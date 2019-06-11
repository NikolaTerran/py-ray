from Obj import obj as obj
from Ray import tracer
import config
from Util import export as ex
import pprint

white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
object0 = obj.Object()

if True:
    #top
    object0.addPolygon(-250,-250,400,
                        -250,250,900,
                        -250,250,400,red)
    object0.addPolygon(-250,-250,400,
                        -250,-250,900,
                        -250,250,900,red)
    #right
    object0.addPolygon(250,-250,400,
                        250,250,400,
                        250,250,900,green)
    object0.addPolygon(250,-250,400,
                        250,250,900,
                        250,-250,900,green)
    #back
    object0.addPolygon(-250,-250,900,
                        250,250,900,
                        -250,250,900,white)
    object0.addPolygon(-250,-250,900,
                        250,-250,900,
                        250,250,900,white)
    #bot
    object0.addPolygon(-250,-250,900,
                        -250,-250,400,
                        250,-250,400,white)

    object0.addPolygon(-250,-250,900,
                        250,-250,400,
                        250,-250,900,white)
    #top
    object0.addPolygon(-250,250,900,
                        -100,250,550,
                        -100,250,750,white)
    object0.addPolygon(-250,250,900,
                        -100,250,750,
                        100,250,750,white)
    object0.addPolygon(-250,250,900,
                        100,250,750,
                        250,250,900,white)
    object0.addPolygon(250,250,900,
                        100,250,750,
                        250,250,400,white)
    object0.addPolygon(100,250,750,
                        100,250,550,
                        250,250,400,white)
    object0.addPolygon(100,250,550,
                        -100,250,550,
                        250,250,400,white)
    object0.addPolygon(-100,250,550,
                        -250,250,400,
                        250,250,400,white)
    object0.addPolygon(-100,250,550,
                        -250,250,900,
                        -250,250,400,white)

layer0 = ex.Canvas()
trace0 = tracer.Tracer()

#index = 0
# for x in object0.cord:
#     x.debug()

#pprint.pprint(object0.cord)

trace0.test(object0,layer0)

#layer0.write(0,0,color)
layer0.push("hi.ppm")
#print(config.xlim)

#When you die and your whole life flashes before your eyes, how much of it do you want to not have ray tracing?
