import tkinter as tk
import Translator as translator

class MazeUI:
    def __init__(self):
        # Maze info
        #self.maze_transcript
        #self.maze_width
        #self.maze_height
        self.UI()

        # canvas info

    def UI(self):
        window = tk.Tk()
        window.geometry("800x600")
        window.configure(bg="lightgray")
        window.title("Maze")

        canvas = tk.Canvas(window, height= 500, width= 500)
        canvas.pack(padx=50, pady=50, side="left")

        window.mainloop()


maze = MazeUI()
    # button for picking maze | Maze => Transcript => self.transcript/width/height