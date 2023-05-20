import tkinter as tk
import tkinter.ttk as ttk
import Translator as translator

class MazeUI:
    def __init__(self):
        # Maze info from transcript 
        self.maze_transcript = [[1,0,0,0,0,0,0,0,0,1],[0,1,1,0,0,1,0,1,1,0],[0,1,0,0,1,0,0,0,1,0],[0,0,0,1,1,0,1,0,0,0],[0,1,0,0,0,0,1,1,0,0],[0,0,1,1,0,0,0,0,1,0],[0,0,0,1,0,1,1,0,0,0],[0,1,0,0,0,1,0,0,1,0],[0,1,1,0,1,0,0,1,1,2],[1,0,0,0,0,0,0,0,0,1]] # translator.transcript
        self.maze_width = 10 #translator.width
        self.maze_height = 10 #translator.height
        self.UI()

        # canvas info

    def UI(self):
        window = tk.Tk()
        window.geometry("900x700")
        window.configure(bg="lightgray")
        window.title("Maze")
        for column in range(8):
            window.columnconfigure(column, minsize=100)
        for row in range(7):
            window.rowconfigure(row, minsize=100)

        self.draw_maze(window)
        self.draw_buttons(window)

        window.mainloop()
    
    def draw_maze(self, window):
        height = 500
        width = 500
        canvas = tk.Canvas(window, height= height, width= width)
        block_height = height / self.maze_height
        block_width = width / self.maze_width
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.maze_transcript[y][x] == 1:
                    block = canvas.create_rectangle(x*block_width, y*block_height, (x+1)*block_width,(y+1)*block_height, fill="black")
                elif self.maze_transcript[y][x] == 2:
                    socket = canvas.create_oval(x*block_width+5, y*block_height+5, (x+1)*block_width-5,(y+1)*block_height-5, fill="limegreen")
        canvas.grid( column=1, row=1, columnspan=5, rowspan=5, sticky="SNEW")

    def draw_buttons(self, window):
        select_maze = tk.Label(window, text="Select maze")
        select_maze.configure(bg="lightgray", font="Helvetica 14 bold")
        select_maze.grid(row=1, column=6, columnspan=2, sticky="EW")

        choose = ttk.Combobox(window, textvariable= tk.StringVar())
        choose['values'] = ["MazeScript0", "MazeScript1", "MazeScript2"]
        choose.grid(row=2, column=6, columnspan=2, sticky="NEW", padx=20)

        coords = tk.Label(window, text="Coordinates of Robot")
        coords.configure(bg="lightgray", font="Helvetica 14 bold")
        coords.grid(row=3, column=6, columnspan=2, sticky="EW", padx=20)

        x_coord = tk.Entry(window, width=10, justify="center")
        x_coord.insert(0, "X")
        x_coord.grid(row=4, column=6, sticky="NEW", padx=10)

        y_coord = tk.Entry(window, width=10, justify="center")
        y_coord.insert(0, "Y")
        y_coord.grid(row=4, column=7, sticky="NEW", padx=10)

        def go():
            print("help")
        play = tk.Button(window, text="Play!", command=go, bg="limegreen", font="Helvetica 25 bold")
        play.grid(row=5, column=6, columnspan=2, sticky="SNEW", padx=10)

'''
int_variable.type() - returns type of variable as <class 'int'>
'''
if __name__ == "__main__":
    maze = MazeUI()