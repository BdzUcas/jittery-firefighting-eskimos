import tkinter as tk

root = tk.Tk()

#pong
def pong(root):
    root.title("Pongers")
    root.configure(background = "black")
    root.resizeable(False, False)
    root.geometry("1000x770+250-50")
    root.attributes("-topmost", True)

    class Ball:
        def __init__(self, canvas, width, velocity, windowwidth, windowheight):
            self.canvas = canvas
            self.width = width
            self.velocity = velocity
            self.windowwidth = windowwidth
            self.windowheight = windowheight
            #center ball
            self.centerx = windowwidth/2 - width/2
            self.centery = windowheight/2 - width/2
            self.vx = velocity
            self.vy = velocity
            self.make_ball = self.canvas.create_oval()

    class Paddle:
        pass

#matching cards
def match_cards(root):
    pass

#rock paper scissors
def rps(root):
    pass