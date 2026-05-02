from tkinter import *
from time import sleep


tk = Tk()

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

    def bounce_y(self):
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
        self.canvas.bind_all("<KeyPress-Left>", self.on_key_press_left)
        self.canvas.bind_all("<KeyRelease-Left>", self.on_key_release_left)
        self.canvas.bind_all("<KeyPress-Right>", self.on_key_press_right)
        self.canvas.bind_all("<KeyRelease-Right>", self.on_key_release_right)

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

    def on_key_press_left(self, evt):
        self.keys_pressed["left"] = True

    def on_key_release_left(self, evt):
        self.keys_pressed["left"] = False

    def on_key_press_right(self, evt):
        self.keys_pressed["right"] = True

    def on_key_release_right(self, evt):
        self.keys_pressed["right"] = False


class Brick:
    def __init__(self):
        pass


def break_blocks(root):
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
            ball.bounce_y()

        sleep(0.003)


if __name__ == "__main__":
    break_blocks(tk)
