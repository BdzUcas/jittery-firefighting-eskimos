from tkinter import *
from time import sleep
import random

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


#class for making instruction menu in front
class instruction_base:
    def __init__(self, root, instructions):
        self.root = root
        self.start_frame = Frame(root, bg="white", width=300, height=400)
        self.start_frame.pack(padx=20, pady=20)
        self.start_frame.lift()
        self.inst_desc = Label(self.start_frame, text=instructions, fg="black", width=15, height=20)
        self.inst_desc.pack(pady=20)
        self.start_btn = Button(self.start_frame, text="Start Game", command=self.start_game, bg="lightgray", fg="black", padx=5, pady=5, width=10)
        self.start_btn.pack()
        self.quit_btn = Button(self.start_frame, text="Exit Game", command=root.destroy, bg="lightgray")
        self.quit_btn.pack()

    def start_game(self):
        self.start_frame.destroy()


class Ball:
    def __init__(self, canvas, color, radius):
        self.canvas = canvas
        self.window_height = self.canvas.winfo_height()
        self.window_width = self.canvas.winfo_width()
        #speed
        self.dx = 1.5
        self.dy = -1.5
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
            horizontal_touch = ball_right >= paddle_left and ball_left <= paddle_right
            vertical_touch = ball_bottom >= paddle_top and ball_top < paddle_top
            return horizontal_touch and vertical_touch
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
    bricks_pos = [(75, 100), (175, 100), (275, 100), (375, 100), (475, 100), (575, 100), (675, 100), (775, 100), (875, 100), #row 1
    (75, 150), (175, 150), (275, 150), (375, 150), (475, 150), (575, 150), (675, 150), (775, 150), (875, 150), #row 2
    (75, 200), (175, 200), (275, 200), (375, 200), (475, 200), (575, 200), (675, 200), (775, 200), (875, 200), #row 3
    (75, 250), (175, 250), (275, 250), (375, 250), (475, 250), (575, 250), (675, 250), (775, 250), (875, 250), #row 4
    (75, 300), (175, 300), (275, 300), (375, 300), (475, 300), (575, 300), (675, 300), (775, 300), (875, 300)] #row 5

    for x, y in bricks_pos:
        bricks.append(Brick(canvas, x, y, 80, 20, "white"))

    instruction_menu = instruction_base(root, "In this game, you have to use the paddle on the bottom of the screen to bounce the ball so it hits the blocks above. Hit all blocks to win!\nYou only have one life per round.\nUse the left and right arrow keys to control your paddle.")
    while True:
        #lose condition
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

        #win condition
        count_brick = 0
        for brick in bricks:
            if brick.active:
                count_brick += 1
        if count_brick == 0:
            canvas.create_text(500, 400, text="YOU WIN!", fill="white", font=("Helvetica", 32))
            root.update()
            break

        sleep(0.003)
    root.mainloop()

block_break(tk)


#matching cards
class Card:
    def __init__(self, canvas, x, y, width, height, face_value, on_click):
        self.canvas = canvas
        self.face_value = face_value
        self.face_up = False
        self.matched = False
        self.rect_id = canvas.create_rectangle(x, y, x+width, y+height, fill="gray", outline="black", width=2)
        self.text_id = None
        self.canvas.tag_bind(self.rect_id, "<Button-1>", lambda event: on_click(self))

    #make card show other side
    def flip(self):
        if self.face_up or self.matched:
            return
        self.canvas.itemconfig(self.rect_id, fill="white")
        coords = self.canvas.coords(self.rect_id)
        center_x = (coords[0] + coords[2]) / 2
        center_y = (coords[1] + coords[3]) / 2
        self.text_id = self.canvas.create_text(center_x, center_y, text=str(self.face_value), font=("Arial", 24))
        self.face_up = True

    #make card show back
    def hide(self):
        if not self.face_up or self.matched:
            return
        self.canvas.itemconfig(self.rect_id, fill="gray")
        if self.text_id:
            self.canvas.delete(self.text_id)
            self.text_id = None
        self.face_up = False

    def set_matched(self):
        self.matched = True
        self.canvas.itemconfig(self.rect_id, fill="light green")
        if self.text_id:
            self.canvas.itemconfig(self.text_id, fill="black")


def match_cards(root):
    root.title("Matching Cards")
    root.configure(background="blue")
    root.resizable(0, 0)
    root.geometry("1000x800")
    root.attributes("-topmost", True)
    canvas = Canvas(root, bg="blue", width=1000, height=800, highlightthickness=4)
    canvas.pack()
    root.update()

    #need values twice since there needs to be pairs
    values = list(range(1, 9))
    deck = values + values
    #shuffle to get random positions
    random.shuffle(deck)

    #set up cards
    card_width = 200
    card_height = 150
    margin = 25
    cards = []
    states = {
        "cards faceup": [],
        "accept_clicks": True
    }

    def click_card(card):
        if not states["accept_clicks"] or card.face_up or card.matched:
            return
        card.flip()
        states["cards faceup"].append(card)
        if len(states["cards faceup"]) == 2:
            states["accept_clicks"] = False
            root.after(800, check_match)

    #check for a match
    def check_match():
        if len(states["cards faceup"]) != 2:
            states["accept_clicks"] = True
            return

        #check if they're matching. if they're not, flip them back over.
        first, second = states["cards faceup"]
        if first.face_value == second.face_value:
            first.set_matched()
            second.set_matched()
        else:
            first.hide()
            second.hide()

        states["cards faceup"].clear()
        states["accept_clicks"] = True

        #check if all cards are facing up for the win conditions
        if all(card.matched for card in cards):
            canvas.create_text(500, 400, text="YOU WIN!", fill="white", font=("Arial", 48))

    #set up the card objects and their values
    for row in range(4):
        for col in range(4):
            x = margin + col * (card_width + margin)
            y = margin + row * (card_height + margin)
            face_value = deck.pop()
            card = Card(canvas, x, y, card_width, card_height, face_value, click_card)
            cards.append(card)

    #use mainloop in order to keep window open.
    root.mainloop()