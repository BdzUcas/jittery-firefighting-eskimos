import tkinter as tk
from PIL import Image, ImageTk
import time
root = tk.Tk()
root.title("IDK MAN")


root.configure(background="light blue")
root.minsize(2600,1200)
root.maxsize(2600,1200)

#Images
itemframe = Image.open("jittery-firefighting-eskimos-Jaxon/Images/ItemFrame.png.png")
itemframe = ImageTk.PhotoImage(itemframe)

Testimage1 = Image.open("jittery-firefighting-eskimos-Jaxon/Images/Test1background.png.png")
Testimage1 = ImageTk.PhotoImage(Testimage1)

Testimage2 = Image.open("jittery-firefighting-eskimos-Jaxon/Images/Test2Background.png.png")
Testimage2 = ImageTk.PhotoImage(Testimage2)
#button.pack(pady=20)

#The main part
#itemframe_btn = tk.Button(root, image=itemframe)
#itemframe_btn.place(relx=.5, rely=0.90, anchor="n")
def SceneButtons(SceneData):
    if SceneData == 1:
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(Testimage2,2))
        root.FrsButton.place(relx=.02, rely=0.5,anchor="n")
    if SceneData == 2:
        root.FrsButton.place_forget()
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(Testimage1,1))
        root.FrsButton.place(relx=.8, rely=0.5,anchor="n")
        #root.frsButton.place(relx=.02, rely=0.5,anchor="n")
def scene(background,SceneData):
    root.backgroundlabel = tk.Label(root, image=background)
    root.backgroundlabel.place(relx=.5, rely=0.0, anchor="n")
    SceneButtons(SceneData)


#Test scene Data
scene(Testimage1,1)
root.mainloop()