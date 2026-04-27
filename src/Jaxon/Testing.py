import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load and display an image 
timage = Image.open('P:\Castro,jaxon\JC_CP2\Fnaf Cameras\Images\download.png')
timage = ImageTk.PhotoImage(timage)
caveimage = Image.open('P:\Castro,jaxon\JC_CP2\Fnaf Cameras\Images\Cave.png')
caveimage = ImageTk.PhotoImage(caveimage)
#Making the image switching function
parent.count = 1
def update():
    parent.count += 1
    if parent.count == 3:
        parent.count = 1
    if parent.count == 1:
        button.config(image=timage)
    if parent.count == 2:
        button.config(image=caveimage)
# Create a label to display the image
button = tk.Button(parent, image=timage, command=update)
button.pack(pady=20)

# Start the Tkinter event loop
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