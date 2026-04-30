import tkinter as tk
from PIL import Image, ImageTk
import time
from ImageLoading import *
root = tk.Tk()
root.title("IDK MAN")


root.configure(background="light blue")
root.minsize(2600,1200)
root.maxsize(2600,1200)

#button.pack(pady=20)


itemframe_btn = tk.Button(root, image=itemframe)
itemframe_btn.place(relx=.5, rely=0.90, anchor="n")
root.mainloop()