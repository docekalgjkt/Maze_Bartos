class Translator:
    def __init__(self):

        self.transcript = []
        self.width
        self.height
        #self.dictionary use if not just 0's 1's and 2
        self.translate()
        self.dimensions()

    def translate(self):
        while True:
            cut = []
            file = open("C:\Users\42077\OneDrive\GitHub.me\Maze_\MazeScript1")
            script = file.readlines()
            for line in script:
                if line != "":
                    for number in line.split(","):
                        cut.append(int(number))
                    self.transcript.append(cut)
                else:
                    break

    def dimensions(self):
        self.width = len(self.transcript[0])
        self.height = len(self.transcript)
        return self