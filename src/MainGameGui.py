import tkinter as tk
from PIL import Image, ImageTk
import time
root = tk.Tk()
root.title("IDK MAN")


root.configure(background="light blue")
root.minsize(2600,1400)
root.maxsize(2600,1400)

#Images
itemframe = Image.open("Images/ItemFrame.png.png")
itemframe = ImageTk.PhotoImage(itemframe)

Testimage1 = Image.open("Images/Test1background.png.png")
Testimage1 = ImageTk.PhotoImage(Testimage1)

Testimage2 = Image.open("Images/Test2Background.png.png")
Testimage2 = ImageTk.PhotoImage(Testimage2)

Testitem1 = Image.open("Images/Test_Item.png.png")
Testitem1 = ImageTk.PhotoImage(Testitem1)
#button.pack(pady=20)

root.Temporary_Items = []
root.testItemBool = 0
root.Item_Selected = "None"

#The main part
#itemframe_btn = tk.Button(root, image=itemframe)
#itemframe_btn.place(relx=.5, rely=0.90, anchor="n")
def itemframe_Deletion(Item_type):
    for x in root.Temporary_Items:
        if x[1] == Item_type:
            root.Temporary_Items.pop(x)
            Inventoryframes(root.Temporary_Items)
def item_selection(item_Type):
    if item_Type == "None":
        root.Item_Selected = item_Type
    elif item_Type == "Test":
        root.Item_Selected = item_Type
        itemframe_Deletion(item_Type)

def Inventoryframes(Inventory):
    pass
    root.empty = tk.Button(root,image=itemframe, command=lambda:item_selection("None"))
    root.empty.place(relx=0.1, rely=0.85,anchor="n")
    root.InventoryCount = 0.1
    for x in Inventory:
        root.InventoryCount += 0.1
        button = tk.Button(root,image=x[1],command=lambda:item_selection(x[0]))
        button.place(relx=root.InventoryCount, rely=0.85,anchor="n")
def item(ItemName):
    if ItemName == "Test":
        root.item.place_forget()
        #Hey I Do Not know what we are really doing for the item logic so just replace this with the function for item storage
        root.Temporary_Items.append(["Test",Testitem1])
        print(root.Temporary_Items)
        Inventoryframes(root.Temporary_Items)

def SceneButtons(SceneData):
    if SceneData == 1:
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(Testimage2,2))
        root.FrsButton.place(relx=.02, rely=0.5,anchor="n")
    if SceneData == 2:
        root.FrsButton.place_forget()
        root.FrsButton = tk.Button(root, image=itemframe, command=lambda:scene(Testimage1,1))
        root.FrsButton.place(relx=.8, rely=0.5,anchor="n")
        #root.frsButton.place(relx=.02, rely=0.5,anchor="n")
def SceneItems(SceneData):
    if SceneData == 1:
        if root.testItemBool < 4:
            root.testItemBool += 1
            root.item = tk.Button(root, image=Testitem1, command=lambda: item("Test"))
            root.item.place(relx=.5, rely=0.1,anchor="n")
        
def scene(background,SceneData):
    root.backgroundlabel = tk.Label(root, image=background)
    root.backgroundlabel.place(relx=.5, rely=0.0, anchor="n")
    SceneButtons(SceneData)
    SceneItems(SceneData)


#Test scene Data
scene(Testimage1,1)
root.mainloop()