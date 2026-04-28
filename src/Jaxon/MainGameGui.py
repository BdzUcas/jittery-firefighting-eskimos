import tkinter as tk
from PIL import Image, ImageTk
import time
root = tk.Tk()
root.title("IDK MAN")


root.configure(background="light blue")
root.minsize(2700,2000)
root.maxsize(2700,2000)

#button.pack(pady=20)
itemframe = Image.open("Images/ItemFrame.png.png")
itemframe = ImageTk.PhotoImage(itemframe)

itemframe_btn = tk.Button(root, image=itemframe)
itemframe_btn.pack(padx=1,pady=95)
root.mainloop()