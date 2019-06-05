from Obj import obj as obj
from Ray import tracer
import config
from Util import export as ex

object0 = obj.Object(255,255,250,0)
#left
object0.addPolygon(-250,-250,0,
                    -250,250,500,
                    -250,250,0)
object0.addPolygon(-250,-250,0,
                    -250,-250,500,
                    -250,250,500)
#right
object0.addPolygon(250,-250,0,
                    250,250,500,
                    250,250,0)
object0.addPolygon(250,-250,0,
                    250,-250,500,
                    250,250,500)
#back
object0.addPolygon(-250,-250,500,
                    250,250,500,
                    -250,250,500)
object0.addPolygon(-250,-250,500,
                    250,-250,500,
                    250,250,500)
#bot
object0.addPolygon(-250,0,500,
                    -250,0,0,
                    250,0,0)
object0.addPolygon(-250,0,500,
                    250,0,0,
                    250,0,500)

layer0 = ex.Canvas()
#trace0 = tracer.Tracer()


#layer0.write(0,0,color)
layer0.push("hi.ppm")
#print(config.xlim)

#When you die and your whole life flashes before your eyes, how much of it do you want to not have ray tracing?
