from tkinter import *
from time import sleep

tk = Tk()

#reference
"""ball pos [0] Top left coordinate x1
ball pos [1] Top left coordinate y1
ball pos [2] Bottom right coordinate x2
ball pos [3] Bottom right coordinate y2

bat pos [0] Top left coordinate x1
bat pos [1] Top left coordinate y1
bat pos [2] Bottom right coordinate x2
bat pos [3] Bottom right coordinate y2"""


class Ball:
    def __init__(self, canvas, color, radius):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        #speed
        self.dx = 2
        self.dy = -2
        self.bal = canvas.create_oval(
            self.window_width / 2 - radius,
            self.window_height / 2 - radius,
            self.window_width / 2 + radius,
            self.window_height / 2 + radius,
            fill=color,
        )
        self.hit_bottom = False

    def movement(self):
        self.canvas.move(self.bal, self.dx, self.dy)
        position = self.canvas.coords(self.bal)

        if position[0] <= 0:
            self.dx = abs(self.dx)
        elif position[2] >= self.window_width:
            self.dx = -abs(self.dx)

        if position[1] <= 0:
            self.dy = abs(self.dy)
        elif position[3] >= self.window_height:
            #check if it has hit the botom
            self.hit_bottom = True

    def bounce(self):
        self.dy = -self.dy

    def coords(self):
        return self.canvas.coords(self.bal)

    def collision(self, ball_pos, paddle_pos):
        #only have collision if ball is touching paddle
        if self.dy > 0:
            ball_left, ball_top, ball_right, ball_bottom = ball_pos
            paddle_left, paddle_top, paddle_right, paddle_bottom = paddle_pos
            horizontally_overlapping = ball_right >= paddle_left and ball_left <= paddle_right
            vertically_touching = ball_bottom >= paddle_top and ball_top < paddle_top
            return horizontally_overlapping and vertically_touching
        return False


class Paddle:
    def __init__(self, canvas, color, width, height):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        self.rec = canvas.create_rectangle(-width, -height, width, height, fill=color)
        self.speed = 2.5
        self.keys_pressed = {"left": False, "right": False}
        self.canvas.move(self.rec, self.window_width / 2, 700)
        #check for key press instead of binding it to the keys to make paddle movement smooth
        self.canvas.bind_all("<KeyPress-Left>", self.press_left)
        self.canvas.bind_all("<KeyRelease-Left>", self.release_left)
        self.canvas.bind_all("<KeyPress-Right>", self.press_right)
        self.canvas.bind_all("<KeyRelease-Right>", self.release_right)

    def get_pos(self):
        dx = 0
        if self.keys_pressed["left"]:
            dx = -self.speed
        if self.keys_pressed["right"]:
            dx = self.speed
        
        if dx != 0:
            position = self.canvas.coords(self.rec)
            if dx < 0 and position[0] <= 0:
                dx = 0
            elif dx > 0 and position[2] >= self.window_width:
                dx = 0
            self.canvas.move(self.rec, dx, 0)

    def press_left(self, evt):
        self.keys_pressed["left"] = True

    def release_left(self, evt):
        self.keys_pressed["left"] = False

    def press_right(self, evt):
        self.keys_pressed["right"] = True

    def release_right(self, evt):
        self.keys_pressed["right"] = False


class Brick:
    def __init__(self, canvas, x, y, width, height, color):
        self.canvas = canvas
        self.block = self.canvas.create_rectangle(x, y, x+width, y+height, fill=color)
        self.status = self.canvas.coords(self.block)
        self.active = True

    def block_coords(self):
        return self.canvas.coords(self.block)
    
    def collision(self, ball_pos):
        if not self.active:
            return False
        brick_pos = self.block_coords()
        return (ball_pos[2] >= brick_pos[0] and ball_pos[0] <= brick_pos[2] and ball_pos[3] >= brick_pos[1] and ball_pos[1] <= brick_pos[3])

    def broken(self):
        if self.active:
            self.canvas.delete(self.block)
            self.active = False


def block_break(root):
    root.title("Break Block")
    root.configure(background="black")
    root.resizable(0, 0)
    root.geometry("1000x800")
    root.attributes("-topmost", True)
    canvas = Canvas(root, bg="black", width=1000, height=800, highlightthickness=4)
    canvas.pack()
    root.update()

    paddle = Paddle(canvas, "white", 60, 10)
    ball = Ball(canvas, "white", 10)
    bricks = []
    bricks_pos = [(100, 100), (200, 100), (300, 100),
    (150, 150), (250, 150), (350, 150),
    (50, 200), (450, 200)]

    for x, y in bricks_pos:
        bricks.append(Brick(canvas, x, y, 80, 20, "white"))

    while True:
        if ball.hit_bottom:
            canvas.create_text(500, 400, text="GAME OVER", fill="white", font=("Helvetica", 32))
            root.update()
            break

        root.update()
        ball.movement()
        paddle.get_pos()

        ball_pos = ball.coords()
        paddle_pos = canvas.coords(paddle.rec)
        if ball.collision(ball_pos, paddle_pos):
            ball.bounce()

        for brick in bricks:
            if brick.collision(ball_pos):
                brick.broken()
                ball.bounce()
                break

        sleep(0.003)


block_break(tk)

#matching cards
def match_cards(root):
    pass

#rock paper scissors
def rps(root):
    pass