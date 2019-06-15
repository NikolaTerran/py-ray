import config
from Obj import obj as obj
import time

class Canvas:
    def __init__(self):
        self.grid = [[0 for j in range(config.xlim)] for i in range(config.ylim)]
        #self.size = config.ylim * config.xlim
        color = [0,0,255]
        x_count = 0
        y_count = 0
        while y_count < config.ylim:
            if x_count == config.xlim:
                x_count = 0
                y_count += 1
                if y_count == config.ylim:
                    break
            self.grid[y_count][x_count] = color
            x_count += 1
    def write(self,y,x,color):
        #print(str(x) + " " + str(y) + " " + str(color))

        self.grid[y][x] = color
        #print(str(self.grid[y][x]) + " y:" + str(y) + " x:" + str(x))
        #time.sleep(5)

    def push(self,name):
        file = open(name, "w")
        file.write("P3 " + str(config.xlim) + " " + str(config.ylim) + " 255\n")
        #self.grid = self.grid.array2string()
        y_count = 0
        x_count = 0
        #print(str(self.grid[y_count][x_count][0]) + " " + str(self.grid[y_count][x_count][1]) + " " + str(self.grid[y_count][x_count][2]))
        while y_count < config.ylim:
            if x_count == config.xlim:
                x_count = 0
                y_count += 1
                if y_count == config.ylim:
                    break
            #print("y_count: " + str(y_count) + "     xcount: " + str(x_count))
            #print(type(self.grid[5][0]))
            file.write(str(self.grid[y_count][x_count][0]) + " " +
                        str(self.grid[y_count][x_count][1]) + " " +
                        str(self.grid[y_count][x_count][2]) + "\n")
            x_count += 1
        #print(self.grid[0][0])
        file.close()
