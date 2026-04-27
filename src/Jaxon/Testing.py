import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load and display an image 
timage = Image.open("Images/Test1.png")
timage = ImageTk.PhotoImage(timage)
hover = Image.open("Images/Test2.jpg")
hover = ImageTk.PhotoImage(hover)
caveimage = Image.open("Images/Briggs.jpg")
caveimage = ImageTk.PhotoImage(caveimage)
briggsHover = Image.open("Images/Briggs-Hover.png")
briggsHover = ImageTk.PhotoImage(briggsHover)
#Making the image switching function
parent.count = 1
def switchup():
    parent.count += 1
    if parent.count == 3:
        parent.count = 1
    if parent.count == 1:
        button.config(image=timage)
    if parent.count == 2:
        button.config(image=caveimage)
def update():
    if parent.count == 3:
        parent.count = 1
    if parent.count == 1:
        button.config(image=timage)
    if parent.count == 2:
        button.config(image=caveimage)
def hoverupdate():
    if parent.count == 1:
        button.config(image=hover)
    if parent.count == 2:
        button.config(image=briggsHover)

def changeOnHover(button):

    # adjusting background of the widget
    # background on entering widget
    button.bind("<Enter>", func=hoverupdate)

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=update()))
    

# Create a label to display the image
button = tk.Button(parent, image=timage, command=switchup)
button.pack(pady=20)

# Start the Tkinter event loop
changeOnHover(button)
parent.mainloop()


"""import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()

root.title("test")
root.configure(background="light blue")
root.minsize(900,300)
root.maxsize(1500,500)
root.geometry("1200x400+100+100")

image = PhotoImage(file="Fnaf Cameras/Images/download.png")
btn = tk.Button(root, image=image)
btn.place(relx=.52, rely=0.4, anchor="n")

root.mainloop
"""