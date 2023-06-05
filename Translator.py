class Translator:
    def __init__(self):
        self.MazeFile = None
        self.transcript = []
        self.width = None
        self.height = None
        #self.dictionary use if not just 0's 1's and 2

    def translate(self, MazeFile):
        self.transcript = []
        self.MazeFile = MazeFile
        file = open(self.MazeFile)
        script = file.readlines()
        for line in script:
            cut = []
            if line != "":
                for number in line.split(","):
                    cut.append(int(number))
                self.transcript.append(cut)
        self.width = len(self.transcript[0])
        self.height = len(self.transcript)
        if self.width > self.height:
            for i in range(self.width-self.height):
                fill_line = []
                for _ in range(self.width):
                    fill_line.append(1)
                self.transcript.append(fill_line)
            self.height = self.width

        elif self.width < self.height:
            for line in self.transcript:
                for _ in range(self.height-self.width):
                    line.append(1)
            self.width = self.height
        return self

    
if __name__ == "__main__":
    translator = Translator()
    translator.translate(r"C:\Users\42077\OneDrive\GitHub.me\Maze_\MazeScript2")
    print(translator.transcript)