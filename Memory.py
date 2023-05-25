from Translator import *

class Queue:
    def __init__(self):
        self.queue = []
    
    def add(self, node):
        self.queue.append(node)
        
    def use(self):
        return self.queue.pop(0)

class Node:
    def __init__(self, node):
        # self ----
        self.position = node
        # previous node ----
        self.parent = None
        # children ----
        self.children = [] # S N W E

class Memory:
    def __init__(self, origin): 
        self.discovered = []
        self.path = []
        self.root = Node(origin) # starting position of robot
        self.discovered.append(self.root.position)
        self.translator = Translator()
        self.translator.translate(r"C:\Users\42077\OneDrive\GitHub.me\Maze_\MazeScript2")
        self.queue = Queue()
        self.queue.add(self.root)
        self.find_socket()

    def check_surroundings(self, node): # enter node of which children we are looking for
        for i in [1, -1]:
            try:
                if node.position[0] == 0 and i == -1:
                    continue
                else:
                    if self.translator.transcript[node.position[0]+i][node.position[1]] != 1:
                        child = Node([node.position[0]+i,node.position[1]])
                        child.parent = node
                        if child.position not in self.discovered:
                            self.discovered.append(child.position)
                            node.children.append(child)
                            self.queue.add(child)
                    else:
                        node.children.append(None)
            except IndexError:
                node.children.append(None)
        
        for j in [1, -1]:
            try:
                if node.position[1] == 0 and j == -1:
                    continue
                else:
                    if self.translator.transcript[node.position[0]][node.position[1]+j] != 1:
                        child = Node([node.position[0],node.position[1]+j])
                        child.parent = node
                        if child.position not in self.discovered:
                            self.discovered.append(child.position)
                            node.children.append(child)
                            self.queue.add(child)
                    else:
                        node.children.append(None)
            except IndexError:
                node.children.append(None)
        
        if self.translator.transcript[node.position[0]][node.position[1]] == 2:
            knot = node
            self.path.append(knot)
            while knot.parent != None:
                self.path.append(knot.parent)
                knot = knot.parent
            return self
    
    def find_socket(self):
        while self.path == []:
            self.check_surroundings(self.queue.use())
            for q in self.queue.queue:
                print(q.position, end=",")
            print(" \n")
        return self.path



if __name__ == "__main__":
    memory = Memory([0, 0])
    for q in memory.find_socket():
        print(q.position)