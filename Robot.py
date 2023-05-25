from Translator import *
from Memory import *

class Robot:
    def __init__(self, y_coord, x_coord):

        self.yx = [y_coord, x_coord]   # [y,x]
        
    def check_surroundings(self, place):
        dir = place[0]
        x = place[2]
        y = place[1]

        possible_routs = []
        
    def navigation(self):
        # possible_routs = self.check_surroundings(possible_route) possible_rout from last iteration
        # for route in possible_routs
            # check_surroundings(route) --> change 
                # if transcript[y][x] == 2:
                    # return final route
            # navigation()
        pass

    def memory(self):
        memory = Memory()

    def sprite(self):
        pass

if __name__ == "__main__":
    robot = Robot(0, 0)