from tkinter import *
from time import *
from random import *

tk = Tk()

"""ball pos [0] Top left coordinate x1
ball pos [1] Top left coordinate y1
ball pos [2] Bottom right coordinate x2
ball pos [3] Bottom right coordinate y2

bat pos [0] Top left coordinate x1
bat pos [1] Top left coordinate y1
bat pos [2] Bottom right coordinate x2
bat pos [3] Bottom right coordinate y2"""

#pong classes
class Ball:
    def __init__(self, canvas, color, radius):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.dx = self.window_width/2
        self.dy = self.window_height/2
        self.bal = canvas.create_oval(self.dx-radius, self.dy-radius, self.dx+radius, self.dy+radius, fill=color)
        self.x = 0
        self.y = 1
    def movement(self):
        self.canvas.move(self.bal,self.x,self.y)
        #get position
        position = self.canvas.coords(self.bal)
        if position[1] <= 0:
            self.y = 1
        elif position[3] >=self.window_height:
            self.hit_bottom = True
        if position[0] <= 0:
            self.x = 1
        elif position [2] >= self.window_width:
            self.x = -1
    def collision(self, ball_pos, paddle_pos):
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                return True
        return False


class Paddle:
    def __init__(self, canvas, color, width, height):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.dx = self.window_width/2
        self.dy = self.window_height/2
        self.rec = canvas.create_rectangle(-width, -height, width, height, fill=color)
        self.x = 0
        self.canvas.move(self.rec, self.dx, 700)
        self.canvas.bind_all('<Left>',self.move_left)
        self.canvas.bind_all('<Right>',self.move_right)
    def get_pos(self):
        #get position
        position = self.canvas.coords(self.rec)
        if position[1] <= 0:
            self.x = 0
        elif position[3] >=self.window_height:
            self.x = 0
    def move_left(self, evt):
        self.x = -15
        self.canvas.move(self.rec,self.x,0)
    def move_right(self, evt):
        self.x = 15
        self.canvas.move(self.rec,self.x,0)


class Brick:
    def __init__(self):
        pass

#pong
def pong(root):
    #setting up window
    root.title("Break Block")
    root.configure(background="black")
    root.resizable(0, 0)
    root.geometry("1000x800")
    root.attributes("-topmost", True)
    canvas = Canvas(root, bg="black", width=1000, height=800, highlightthickness=4)
    canvas.pack()
    root.update()

    padle = Paddle(canvas, "white", 60, 10)
    bauble = Ball(canvas, "white", 10)
    while True:
        root.update()
        bauble.movement()
        padle.get_pos()
        sleep(0.003)

pong(tk)

#matching cards
def match_cards(root):
    pass

#rock paper scissors
def rps(root):
    pass