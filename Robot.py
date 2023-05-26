from Translator import *
from Memory import *

class Robot:
    def __init__(self, y_coord, x_coord):
        self.memory = Memory()
        self.yx = [y_coord, x_coord]   # [y,x]
        self.step = None
        
    def check_surroundings(self, place):
        dir = place[0]
        x = place[2]
        y = place[1]

        possible_routs = []
        
    def navigation(self):
        navigation = self.memory.find_socket()
            
    def sprite(self):
        pass

if __name__ == "__main__":
    robot = Robot(0, 0)