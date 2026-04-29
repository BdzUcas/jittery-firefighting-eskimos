from tkinter import *
from time import *
from random import *

tk = Tk()

#pong classes
class Ball:
    def __init__(self, canvas, color, radius):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.dx = self.window_width/2
        self.dy = self.window_height/2
        self.bal = canvas.create_oval(self.dx-radius, self.dy-radius, self.dx+radius, self.dy+radius, fill=color)
        self.x = -1
        self.y = 0
    def movement(self):
        self.canvas.move(self.bal,self.x,self.y)
        #get position
        position = self.canvas.coords(self.bal)
        if position[1] <= 0:
            self.y = 1
        elif position[3] >=self.window_height:
            self.y = -1
        if position[0] <= 0:
            self.x = 1
        elif position [2] >= self.window_width:
            self.x = -1

class Paddle:
    def __init__(self, canvas, color, width, height, player="user"):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.dx = self.window_width/2
        self.dy = self.window_height/2
        self.rec = canvas.create_rectangle(-width, -height, width, height, fill=color)
        self.y = 0
        self.canvas.bind_all('<Up>',self.move_up)
        self.canvas.bind_all('<Down>',self.move_down)
        if player == "user":
            self.canvas.move(self.rec, 50, self.dy)
        elif player == "bot":
            self.canvas.move(self.rec, 950, self.dy)
    
    def movement(self):
        self.canvas.move(self.rec,0,self.y)
        #get position
        position = self.canvas.coords(self.rec)
        if position[1] <= 0:
            self.y = 0
        elif position[3] >=self.window_height:
            self.y = 0

    def move_up(self):
        self.y = -5

    def move_down(self):
        self.y = 5
    

#pong
def pong(root):
    #setting up window
    root.title("Pongers")
    root.configure(background="black")
    root.resizable(0, 0)
    root.geometry("1000x800")
    root.attributes("-topmost", True)
    canvas = Canvas(root, bg="black", width=1000, height=800, highlightthickness=4)
    canvas.pack()
    root.update()

    bauble = Ball(canvas, "white", 10)
    padle = Paddle(canvas, "white", 10, 60, "user")
    eldap = Paddle(canvas, "white", 10, 60, "bot")
    while True:
        root.update()
        bauble.movement()
        padle.movement()
        sleep(0.003)

pong(tk)

#matching cards
def match_cards(root):
    pass

#rock paper scissors
def rps(root):
    pass