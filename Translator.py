class Translator:
    def __init__(self):
        self.transcript = []
        self.width
        self.height
        
        self.script
        self.dictionary
        self.translate()
        self.dimensions()

    def translate(self):
        while True:
            line = []
            with open("C:\Users\42077\OneDrive\GitHub.me\Maze_\MazeScript1") as vstup:
                self.script = vstup.readline()
                if self.script != "":
                    for number in self.script.sprlit(","):
                        line.append(int(number))
                    self.transcript.append(line)
                else:
                    break

    def dimensions(self):
        self.width = len(self.transcript[0])
        self.height = len(self.transcript)
        return self