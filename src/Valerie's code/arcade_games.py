from tkinter import *
from time import *
from random import *

tk = Tk()

class Ball:
    def __init__(self, canvas, color, radius):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.dx = self.window_width/2
        self.dy = self.window_height/2
        self.bal = canvas.create_oval(self.dx-radius, self.dy-radius, self.dx+radius, self.dy+radius, fill=color)
        self.x = 0
        self.y = -1
    def movement(self):
        self.canvas.move(self.bal,0,-1)
        #get position
        position = self.canvas.coords(self.bal)
        if position[1] <= 0:
            self.y = 1
        elif position[3] >=self.window_height:
            self.y = -1

class Paddle:
    def __init__(self, canvas, color, window_width, window_height, width, length):
        self.canvas = canvas
        self.dx = window_width/2
        self.dy = window_height/2
        self.rec = canvas.create_rectangle(-self.dx, self.dy-length, self.dx, self.dy+length, fill=color)
        self.canvas.move(self.canvas, 200, 300)

#pong
def pong(root):
    #setting up window
    root.title("Pongers")
    root.configure(background="black")
    root.resizable(0, 0)
    root.geometry("1000x770")
    root.attributes("-topmost", True)
    canvas = Canvas(root, bg="black", width=1000, height=770, highlightthickness=4)
    canvas.pack()
    root.update()

    bauble = Ball(canvas, "white", 10)
    while True:
        root.update()
        bauble.movement()
        sleep(0.003)

pong(tk)

#matching cards
def match_cards(root):
    pass

#rock paper scissors
def rps(root):
    pass