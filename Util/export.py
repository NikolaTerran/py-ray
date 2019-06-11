import config
from Obj import obj as obj

class Canvas:
    def __init__(self):
        self.grid = [[0 for j in range(config.ylim)] for i in range(config.xlim)]
        #self.size = config.ylim * config.xlim
        x_count = 0
        color = [0,0,0]
        y_count = 0
        while x_count < config.xlim:
            if y_count == config.ylim:
                y_count = 0
                x_count += 1
                if x_count == config.xlim:
                    break
            #print(str(counter) + str(y_counter))
            self.grid[x_count][y_count] = color
            y_count += 1
    def write(self,x,y,color):
        self.grid[x][y] = color
    def push(self,name):
        file = open(name, "w")
        file.write("P3 " + str(config.xlim) + " " + str(config.ylim) + " 255\n")
        #self.grid = self.grid.array2string()
        x_count = 0
        y_count = 0
        while x_count < config.xlim:
            if y_count == config.ylim:
                y_count = 0
                x_count += 1
                if x_count == config.xlim:
                    break
            file.write(str(self.grid[x_count][y_count][0]) + " " +
                        str(self.grid[x_count][y_count][1]) + " " +
                        str(self.grid[x_count][y_count][2]) + "\n")
            y_count += 1
        #print(self.grid[0][0])
        file.close()
