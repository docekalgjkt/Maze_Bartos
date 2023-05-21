from Translator import *

class Robot:
    def __init__(self):
        self.translator = Translator()
        translator.translate(r"C:\Users\42077\OneDrive\GitHub.me\Maze_\MazeScript2")
        self.transcript = self.translator.transcript
        self.xy = [0,0]
        self.check_surroundings()
        
    def check_surroundings(self):
        x = self.xy[0]
        y = self.xy[1]

        possible_routs = []
        # S
        try:
            if self.transcript[y+1][x] != "1":
                possible_routs.append(self.transcript[y+1][x])
        except IndexError:
            pass
        # N
        try:
            if self.transcript[y-1][x] != "1":
                possible_routs.append(self.transcript[y-1][x])
        except IndexError:
            pass
        
        # E
        try:
            if self.transcript[y][x-1] != "1":
                possible_routs.append(self.transcript[y][x-1])
        except IndexError:
            pass
        
        # W
        try:
            if self.transcript[y][x+1] != "1":
                possible_routs.append(self.transcript[y][x+1])
        except IndexError:
            pass
        
        print(possible_routs)
    
    def navigation(self):
        pass

    def sprite(self):
        pass