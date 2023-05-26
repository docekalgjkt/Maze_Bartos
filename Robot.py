from Translator import *
from Memory import *

class Robot:
    def __init__(self, coordinates, transcript):
        self.memory = Memory(coordinates, transcript)
        self.path = Memory.find_socket()
        self.step = None

    def next_step(self):
        self.step = self.path.pop()

if __name__ == "__main__":
    robot = Robot([0, 0], [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 2, 1, 0], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0]])