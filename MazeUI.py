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
        self.batery = range(20)
        self.bcanvas = None
        self.piece_height= None
        self.UI()

    def UI(self):
        window = tk.Tk()
        window.geometry("900x700")
        window.configure(bg="lightgray")
        window.title("Maze")
        # Grid -----------
        for column in range(6):
            window.columnconfigure(column, minsize=100)
        window.columnconfigure(6, minsize=80)
        window.columnconfigure(7, minsize=20)
        window.columnconfigure(8, minsize=80)
        window.columnconfigure(9, minsize=20)
        
        window.rowconfigure(0, minsize=100)
        window.rowconfigure(1, minsize=100)
        window.rowconfigure(2, minsize=50)
        window.rowconfigure(3, minsize=50)
        window.rowconfigure(4, minsize=100)
        window.rowconfigure(5, minsize=50)
        window.rowconfigure(6, minsize=50)
        window.rowconfigure(7, minsize=100)
        window.rowconfigure(8, minsize=100)

        # UI widgets ----
        self.draw_buttons(window)
        self.draw_batery(window)
        self.draw_menu(window)

        window.mainloop()
    
    def draw_maze(self, window):
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
                    socket_path = self.canvas.create_rectangle(x*self.block_width, y*self.block_height, (x+1)*self.block_width,(y+1)*self.block_height, fill="white")
                    socket = self.canvas.create_oval(x*self.block_width+5, y*self.block_height+5, (x+1)*self.block_width-5,(y+1)*self.block_height-5,fill="yellow", width=2)
                else:
                    path = self.canvas.create_rectangle(x*self.block_width, y*self.block_height, (x+1)*self.block_width,(y+1)*self.block_height, fill="white")
        self.canvas.grid( column=1, row=1, columnspan=5, rowspan=7, sticky="SNEW")

    def draw_batery(self, window):
        height = 500
        width = 100
        self.piece_height = (0.95*height)/len(self.batery) 
        self.bcanvas = tk.Canvas(window, height=height, width=width, bg= "lightgray", bd=0)
        colors = []
        for n in self.batery:
            if n < len(self.batery)*0.2:
                colors.append("red")
                print("red", end=",")
            elif len(self.batery)*0.2 <= n <= len(self.batery)*0.5:
                colors.append("yellow")
                print("yellow", end=",")
            else:
                colors.append("limegreen")
                print("limegreen", end=",")

        for i in self.batery:
            piece = self.bcanvas.create_rectangle(2,i*self.piece_height+2,width, (i*self.piece_height)+self.piece_height, fill=colors[-i-1])
        tip = self.bcanvas.create_rectangle(width-(0.2*width), 0.95*height+2, 0.2*width, height, fill="gray13")
        self.bcanvas.grid(column=0, row=1, rowspan=7, sticky="SNEW", padx=5)

    def draw_buttons(self, window):
        select_maze = tk.Label(window, text="Select maze")
        select_maze.configure(bg="lightgray", font="Helvetica 14 bold")
        select_maze.grid(row=1, column=6, columnspan=4, sticky="SEW")
        
        def maze_Selcted(event):
            if choose.get() != "Pick the Maze":
                maze_selcted = choose.get()
                self.translator.translate(maze_selcted)
                self.maze_transcript = self.translator.transcript
                self.maze_width = self.translator.width
                self.maze_height = self.translator.height
                self.draw_maze(window)
                if x_coord.get() != "X" and y_coord.get() != "Y":
                    draw_sprite(self.canvas, [int(y_coord.get()), int(x_coord.get())]) 
        
        choose = ttk.Combobox(window, textvariable= tk.StringVar(), font="Helvetica 10 bold")
        choose['values'] = ["MazeScript0", "MazeScript1", "MazeScript2"]
        choose["state"] = "readonly"
        choose.set("Pick the Maze")
        choose.grid(row=2, column=6, columnspan=4, sticky="SNEW", padx=5, pady=5)
        choose.bind("<<ComboboxSelected>>", maze_Selcted)

        from_file = tk.Entry(window, justify="center", font="Helvetica 10 bold")
        from_file.insert(0, "Copy path to maze from PC")
        from_file.grid(row=3, column=6, columnspan=3, sticky="SNEW", padx=5, pady=5)
        def clear():
            from_file.delete(0, END)
        clear_from_file = tk.Button(window, text="X", command=clear,bg="lightgray", font="Helvetica 10 bold")
        clear_from_file.grid(row=3, column=9, sticky="SNEW", pady=5)

        coords = tk.Label(window, text="Coordinates of Robot")
        coords.configure(bg="lightgray", font="Helvetica 14 bold")
        coords.grid(row=4, column=6, columnspan=4, sticky="SEW", padx=5, pady=10)

        def add_x():
            self.robot
            if x_coord.get() == "X":
                x_coord.delete(0, END)
                x_coord.insert(0, "0")
                if x_coord.get() != "X" and y_coord.get() != "Y":
                    move_sprite(self.block_width, 0)
            else:
                x_now = int(x_coord.get())
                x_coord.delete(0, END)
                x_now += 1
                x_coord.insert(0, x_now)
                if x_coord.get() != "X" and y_coord.get() != "Y":
                    move_sprite(self.block_width, 0)

        
        def add_y():
            if y_coord.get() == "Y":
                y_coord.delete(0, END)
                y_coord.insert(0, "0")
                if x_coord.get() != "X" and y_coord.get() != "Y":
                    move_sprite(0, self.block_height)

            else:
                y_now = int(y_coord.get())
                y_coord.delete(0, END)
                y_now += 1
                y_coord.insert(0, y_now)
                if x_coord.get() != "X" and y_coord.get() != "Y":
                    move_sprite(0, self.block_height)
        
        def subtract_x():
            if x_coord.get() != "X":
                if x_coord.get() == "0":
                    x_coord.delete(0, END)
                    x_coord.insert(0, "X")
                else:
                    x_now = int(x_coord.get())
                    x_coord.delete(0, END)
                    x_now -= 1
                    x_coord.insert(0, x_now)
            move_sprite(-self.block_width, 0)
        
        def subtract_y():
            if y_coord.get() != "Y":
                if y_coord.get() == "0":
                    y_coord.delete(0, END)
                    y_coord.insert(0, "Y")
                else:
                    y_now = int(y_coord.get())
                    y_coord.delete(0, END)
                    y_now -= 1
                    y_coord.insert(0, y_now)
            move_sprite(0, -self.block_height)


        x_coord = tk.Entry(window, width=3, justify="center", font="Helvetica 25 bold")
        x_coord.insert(0, "X")
        x_coord.grid(row=5, column=6, rowspan=2, sticky="SNEW", padx=5)
        up_x = tk.Button(window, text="▲", command=add_x, bg="lightgray", font="Helvetica 10 bold")
        up_x.grid(row=5, column=7, sticky="SNEW")
        down_x = tk.Button(window, text="▼", command=subtract_x, bg="lightgray", font="Helvetica 10 bold")
        down_x.grid(row=6, column=7, sticky="SNEW")

        y_coord = tk.Entry(window, width=3, justify="center", font="Helvetica 25 bold")
        y_coord.insert(0, "Y")
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
                print(node.position, end=",")
            except:
                pass

        def go():
            self.memory = Memory([int(y_coord.get()), int(x_coord.get())], self.maze_transcript)
            path = self.memory.find_socket()
            copy = path.copy()
            self.previous = path.pop()
            for i in self.batery:
                if i < len(copy)-1:
                    empty = self.bcanvas.create_rectangle(0+2,i*self.piece_height+2,100, (i*self.piece_height)+self.piece_height, fill="lightgray")
                    window.after(1000, walk(path))
            if len(copy)-1 <= len(self.batery):
                self.draw_congrats(window)
            elif len(copy) > len(self.batery):
                self.draw_gameOver(window)
                
        play = tk.Button(window, text="Play!", command=go, bg="limegreen", font="Helvetica 25 bold")
        play.grid(row=7, column=6, columnspan=4, sticky="SNEW", padx=5, pady=10)

        def move_sprite(x, y):
            if self.robot == None:
                draw_sprite(self.canvas, [int(y_coord.get()), int(x_coord.get())]) 
            else:
                self.canvas.move(self.robot, x, y)

                window.update()

        def draw_sprite(canvas, coords):
            x = coords[1]
            y = coords[0]
            self.robot = self.canvas.create_oval(x*self.block_width+5, y*self.block_height+5, (x+1)*self.block_width-5,(y+1)*self.block_height-5, fill="steelblue", width=2)

    def draw_menu(self, window):
        def instructions():
            pass
        def settings():
            pass

        menu = Menu(window)
        menu.add_command(label= "Instructions", command= instructions)
        menu.add_checkbutton(label="Use path as input", command= settings)
        #menu.pack()
    
    def play_again(self, window):
        def playagain():
            pass
        again = tk.Button(text="Play Again!", command=playagain, bg="lightgray", font="Helvetica 10 bold") 
        again.grid(row=3, column=1, columnspan=5)

    def exit_game(self, window):
        def close():
            window.destroy()
        exit = tk.Button(text="Exit", command=close, bg="lightgray", font="Helvetica 10 bold")
        exit.grid(row=4, column=1, rowspan=2, columnspan=5, sticky="N")

    def draw_congrats(self, window):
        congrats = tk.Label(window,text="Congratulations", font= "Helvetica 25 bold", fg= "green")
        congrats.grid(row= 2, column= 1, columnspan=5, sticky="SNEW")
        self.play_again(window)
        self.exit_game(window)
    
    def draw_gameOver(self, window):
        congrats = tk.Label(window,text="Game Over", font= "Helvetica 25 bold", fg= "red")
        congrats.grid(row= 2, column= 1, columnspan=5, sticky="SNEW")
        self.play_again(window)
        self.exit_game(window)

        '''
        R = (5/14)*self.block_width
        r = (3/14)*self.block_width
        left= canvas.create_oval(x*(2*R-r),x*self.block_width,y*(2*R+r),y*(2*r), fill= "dimgray")
        right= canvas.create_oval(x*(2*R-r),x*(self.block_height-2*r),y*(2*R+r),y*(self.block_height), fill="dimgray") 
        body= canvas.create_oval(x*self.block_width,x*((self.block_height/2)-R),y*(2*R),y*((self.block_height/2)+R), fill="darkgray")
        glasses= canvas.create_oval(x*(self.block_width*5/14),x*r,y*2*R,y*(self.block_height-r), fill="steelblue")
        '''

# error line interface

# int_variable.type() - returns type of variable as <class 'int'>
if __name__ == "__main__":
    maze = MazeUI()