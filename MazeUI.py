from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from Translator import *
from Memory import *

class MazeUI:
    def __init__(self):
        # Maze info from transcript 
        self.translator = Translator()
        self.maze_transcript = None
        self.maze_width = None
        self.maze_height = None
        self.canvas = None
        self.block_height = None
        self.block_width = None
        self.robot = None
        self.memory = None
        self.previous = None
        self.batery = []
        for i in range(11):
            self.batery.append(i)
        self.bcanvas = None
        self.piece_height= None
        self.exit_button = None
        self.again = None
        self.game_over = None
        self.congrats = None
        self.batery_up = None
        self.batery_down = None
        self.error = None
        self.radio = None
        self.copy = None
        self.xText = None
        self.yText = None
        self.xInt = 0
        self.yInt = 0
        self.UI()

    def UI(self):
        window = tk.Tk()
        window.geometry("900x600")
        window.configure(bg="lightgray")
        window.title("Maze")
        # Grid -----------
        for column in range(6):
            window.columnconfigure(column, minsize=100)
        window.columnconfigure(6, minsize=80)
        window.columnconfigure(7, minsize=20)
        window.columnconfigure(8, minsize=80)
        window.columnconfigure(9, minsize=20)
        
        window.rowconfigure(0, minsize=50)
        window.rowconfigure(1, minsize=100)
        window.rowconfigure(2, minsize=50)
        window.rowconfigure(3, minsize=50)
        window.rowconfigure(4, minsize=100)
        window.rowconfigure(5, minsize=50)
        window.rowconfigure(6, minsize=50)
        window.rowconfigure(7, minsize=100)
        window.rowconfigure(8, minsize=50)

        # UI widgets ----
        self.draw_buttons(window)
        self.draw_batery(window)

        window.mainloop()
    
    def draw_maze(self, window):
        if self.canvas != None:
            self.canvas.delete("all")
        height = 500
        width = 500
        self.canvas = tk.Canvas(window, height= height, width= width)
        self.block_height = height / float(self.maze_height)
        self.block_width = width / self.maze_width
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.maze_transcript[y][x] == 1:
                    block = self.canvas.create_rectangle(x*self.block_width, y*self.block_height, (x+1)*self.block_width,(y+1)*self.block_height, fill="black")
                elif self.maze_transcript[y][x] == 2:
                    # draw better socket (with lightning bolt)
                    socket_path = self.canvas.create_rectangle(x*self.block_width, y*self.block_height, (x+1)*self.block_width,(y+1)*self.block_height, fill="white")
                    socket = self.canvas.create_oval(x*self.block_width+5, y*self.block_height+5, (x+1)*self.block_width-5,(y+1)*self.block_height-5,fill="yellow", width=2)
                else:
                    path = self.canvas.create_rectangle(x*self.block_width, y*self.block_height, (x+1)*self.block_width,(y+1)*self.block_height, fill="white")
        self.canvas.grid( column=1, row=1, columnspan=5, rowspan=7, sticky="SNEW")

    def draw_batery(self, window):
        if self.bcanvas != None:
            self.bcanvas.delete("all")
        height = 500
        width = 100
        self.piece_height = (0.95*height)/len(self.batery) 
        self.bcanvas = tk.Canvas(window, height=height, width=width, bg= "lightgray", bd=0)
        colors = []
        for n in self.batery:
            if n < len(self.batery)*0.2:
                colors.append("red")
            elif len(self.batery)*0.2 <= n <= len(self.batery)*0.5:
                colors.append("yellow")
            else:
                colors.append("limegreen")

        for i in self.batery:
            piece = self.bcanvas.create_rectangle(2,i*self.piece_height+2,width, (i*self.piece_height)+self.piece_height, fill=colors[-i-1])
        tip = self.bcanvas.create_rectangle(width-(0.2*width), 0.95*height+2, 0.2*width, height, fill="gray13")
        self.bcanvas.grid(column=0, row=1, rowspan=7, sticky="SNEW", padx=5)
        def batery_add():
            self.batery.append(self.batery[-1]+1)
            self.draw_batery(window)
        def batery_subtract():
            if len(self.batery) > 1:
                self.batery.pop()
                self.draw_batery(window)

        self.batery_up = tk.Button(text="+", font="Helvetica 14 bold", command=batery_add)
        self.batery_up.grid(row=0, column=0, sticky="SEW", padx=5, pady=5)
        self.batery_down = tk.Button(text="-", font="Helvetica 14 bold", command=batery_subtract)
        self.batery_down.grid(row=8, column=0, sticky="NEW", padx=5, pady=5)

    def draw_buttons(self, window):
        
        menubar = tk.Menu(window)
        help = tk.Menu(menubar, tearoff=0)
        file = tk.Menu(menubar, tearoff=0)
        settings = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file)
        file.add_command(label="new file", command=None)
        file.add_command(label="open file", command=None)
        menubar.add_cascade(label="Help", menu=help)
        help.add_command(label="How to play", command = None)
        help.add_command(label="Coordinates", command = None)
        help.add_command(label="Path to file", command = None)
        window.config(menu= menubar)
        
        
        select_maze = tk.Label(window, text="Select maze")
        select_maze.configure(bg="lightgray", font="Helvetica 14 bold")
        select_maze.grid(row=2, column=6, columnspan=4, sticky="SEW")
        
        def maze_Selcted(event):
            if choose.get() != "Pick the Maze":
                maze_selcted = choose.get()
                self.translator.translate(maze_selcted)
                self.maze_transcript = self.translator.transcript
                self.maze_width = self.translator.width
                self.maze_height = self.translator.height
                self.draw_maze(window)
                if x_coord.get() != "X" and y_coord.get() != "Y":
                    draw_sprite(self.canvas, [y_coord.get(), x_coord.get()]) 
        
        choose = ttk.Combobox(window, textvariable= tk.StringVar(), font="Helvetica 10 bold", state="readonly")
        choose['values'] = ["MazeScript0", "MazeScript1", "MazeScript2", "MazeScript3", "MazeScript4"]
        choose.set("Pick the Maze")
        choose.grid(row=3, column=6, columnspan=4, sticky="SNEW", padx=5, pady=5)
        choose.bind("<<ComboboxSelected>>", maze_Selcted)

        coords = tk.Label(window, text="Coordinates of Robot")
        coords.configure(bg="lightgray", font="Helvetica 14 bold")
        coords.grid(row=4, column=6, columnspan=4, sticky="SEW", padx=5, pady=10)

        def add_x():
            if self.xText.get() == "X":
                self.xText.set("0")
                if self.xText.get() != "X" and self.yText.get() != "Y":
                    move_sprite(self.block_width, 0)
            elif self.xInt < self.maze_width-1: 
                self.xInt += 1
                self.xText.set(f"{self.xInt}")
                if self.xText.get() != "X" and self.yText.get() != "Y":
                    move_sprite(self.block_width, 0)
        
        def add_y():
            if self.yText.get() == "Y":
                self.yText.set("0")
                if self.xText.get() != "X" and self.yText.get() != "Y":
                    move_sprite(0, self.block_height)

            elif self.yInt < self.maze_height-1:
                self.yInt += 1
                self.yText.set(f"{self.yInt}")
                if self.xText.get() != "X" and self.yText.get() != "Y":
                    move_sprite(0, self.block_height)
        
        def subtract_x():
            if self.xText.get() != "X":
                if self.xInt == 0:
                    self.xText.set("X")
                    self.canvas.delete(self.robot)
                    self.robot = None
                else:
                    self.xInt -= 1
                    self.xText.set(f"{self.xInt}")
                    if self.xText.get() != "X" and self.yText.get() != "Y":
                        move_sprite(-self.block_width, 0)
        
        def subtract_y():
            if self.yText.get() != "Y":
                if self.yInt == 0:
                    self.yText.set("Y")
                    self.canvas.delete(self.robot)
                    self.robot = None
                else:
                    self.yInt -= 1
                    self.yText.set(f"{self.yInt}")
                    if self.xText.get() != "X" and self.yText.get() != "Y":
                        move_sprite(0, -self.block_height)
        
        self.xText = StringVar()
        x_coord = tk.Entry(window, textvariable=self.xText, width=3, justify="center", font="Helvetica 25 bold", state="readonly")
        self.xText.set("X")
        x_coord.grid(row=5, column=6, rowspan=2, sticky="SNEW", padx=5)
        up_x = tk.Button(window, text="▲", command=add_x, bg="lightgray", font="Helvetica 10 bold")
        up_x.grid(row=5, column=7, sticky="SNEW")
        down_x = tk.Button(window, text="▼", command=subtract_x, bg="lightgray", font="Helvetica 10 bold")
        down_x.grid(row=6, column=7, sticky="SNEW")

        self.yText = StringVar()
        y_coord = tk.Entry(window, width=3, textvariable=self.yText, justify="center", font="Helvetica 25 bold", state="readonly")
        self.yText.set("Y")
        y_coord.grid(row=5, column=8, rowspan=2, sticky="SNEW", padx=5)
        up_y = tk.Button(window, text="▲", command=add_y, bg="lightgray", font="Helvetica 10 bold")
        up_y.grid(row=5, column=9, sticky="SNEW")
        down_y = tk.Button(window, text="▼", command=subtract_y, bg="lightgray", font="Helvetica 10 bold")
        down_y.grid(row=6, column=9, sticky="SNEW")

        def walk(path):
            try:
                node = path.pop()
                # move diference between x's
                move_x = (int(node.position[1]) - int(self.previous.position[1]))*self.block_width
                # move diference between y's
                move_y = (int(node.position[0]) - int(self.previous.position[0]))*self.block_height 
                move_sprite(move_x, move_y)
                move_x = None
                move_y = None
                self.previous = node
            except:
                pass

        def go():
            # diable buttons
            if self.error != None:
                self.error.destroy()
                self.error = None
            up_x["state"] = DISABLED
            up_y["state"] = DISABLED
            down_x["state"] = DISABLED
            down_y["state"] = DISABLED
            x_coord["state"] = DISABLED
            y_coord["state"] = DISABLED
            choose["state"] = DISABLED
            play["state"] = DISABLED
            self.batery_up["state"] = DISABLED
            self.batery_down["state"] = DISABLED
            if self.maze_transcript != None:
                if x_coord.get() != "X" and y_coord.get() != "Y":
                    if self.maze_transcript[int(y_coord.get())][int(x_coord.get())] != 1:
                        try:
                            self.memory = Memory([y_coord.get(), x_coord.get()], self.maze_transcript)
                            path = self.memory.find_socket()
                            self.copy = path.copy()
                            self.previous = path.pop()
                            for i in self.batery:
                                if i < len(self.copy)-1:
                                    empty = self.bcanvas.create_rectangle(0+2,i*self.piece_height+2,100, (i*self.piece_height)+self.piece_height, fill="lightgray")
                                    window.after(575, walk(path))
                            if len(self.copy)-1 <= len(self.batery):
                                draw_congrats()
                            elif len(self.copy) > len(self.batery):
                                draw_gameOver()
                        except IndexError:
                            error("<3 Robot can't reach socket. Please place him better! <3")
                            
                    else:
                        error("<3 Please do not place Robot on walls. Thank you! <3")
                else:
                    error("<3 Please set both coordinate walues. Thank you! <3")
            else:
                error("<3 Please open any maze first. Thank you! <3")  
        play = tk.Button(window, text="Play!", command=go, bg="limegreen", font="Helvetica 25 bold")
        play.grid(row=7, column=6, columnspan=4, sticky="SNEW", padx=5, pady=10)

        def move_sprite(x, y):
            if self.robot == None:
                draw_sprite(self.canvas, [self.yInt, self.xInt]) 
            else:
                self.canvas.move(self.robot, x, y)

                window.update()

        def draw_sprite(canvas, coords):
            x = coords[1]
            y = coords[0]
            # draw better sprite than circle
            self.robot = self.canvas.create_oval(x*self.block_width+5, y*self.block_height+5, (x+1)*self.block_width-5,(y+1)*self.block_height-5, fill="steelblue", width=2)
        
        def exit_game():
            def close():
                window.destroy()
            self.exit_button = tk.Button(text="Exit", command=close, bg="lightgray", font="Helvetica 10 bold")
            self.exit_button.grid(row=4, column=1, rowspan=2, columnspan=5, sticky="N")

        def draw_congrats():
            if 0 < len(self.batery) - (len(self.copy)-1) <= 3: 
                congratulations = "★★ Congratulations ★★"
            elif len(self.batery) > len(self.copy)-1:
                congratulations = "★ Congratulations ★"
            elif len(self.batery) == len(self.copy)-1:
                congratulations = "★★★ Congratulations ★★★"
            self.congrats = tk.Label(window,text=f"{congratulations}", font= "Helvetica 25 bold", fg= "green")
            self.congrats.grid(row= 2, column= 1, columnspan=5, sticky="SNEW")
            play_again()
            exit_game()
        
        def play_again():
            if self.error != None:
                self.error.destroy()
                self.error = None
            def playagain():
                up_x["state"] = NORMAL
                up_y["state"] = NORMAL
                down_x["state"] = NORMAL
                down_y["state"] = NORMAL
                x_coord["state"] = NORMAL
                y_coord["state"] = NORMAL
                choose["state"] = NORMAL
                play["state"] = NORMAL
                self.batery_up["state"] = NORMAL
                self.batery_down["state"] = NORMAL
                self.exit_button.destroy()
                self.again.destroy()
                maze_Selcted("<<ComboboxSelected>>")
                self.draw_batery(window)
                move_sprite(self.canvas, [self.xInt, self.yInt])
                if self.congrats != None:
                    self.congrats.destroy()
                    self.congrats = None
                elif self.game_over != None:
                    self.game_over.destroy()
                    self.game_over = None

            self.again = tk.Button(text="Play Again!", command=playagain, bg="lightgray", font="Helvetica 10 bold") 
            self.again.grid(row=3, column=1, columnspan=5)

        def draw_gameOver():
            self.game_over = tk.Label(window,text="Game Over", font= "Helvetica 25 bold", fg= "red")
            self.game_over.grid(row= 2, column= 1, columnspan=5, sticky="SNEW")
            play_again()
            exit_game()

        def error(error_line):
            self.error = tk.Label(text=error_line, font="Helvetica 14 bold", fg="red", bg="lightgray")
            self.error.grid(row=8, column=1, columnspan=8)
            up_x["state"] = NORMAL
            up_y["state"] = NORMAL
            down_x["state"] = NORMAL
            down_y["state"] = NORMAL
            x_coord["state"] = NORMAL
            y_coord["state"] = NORMAL
            choose["state"] = NORMAL
            play["state"] = NORMAL
            self.batery_up["state"] = NORMAL
            self.batery_down["state"] = NORMAL


if __name__ == "__main__":
    maze = MazeUI()