from tkinter import *

#result class, used for passing information locally to globally
class Result():
    def __init__(self):
        self.result = ''

#This is the gui function that does GUI.
#Here is a quick explanation of how to use it!
#The first argument is a list of dictionaries. 
#Each dictionary represents a widget in the gui
#Here are the different widgets and how you do them:

#text widgets are written with just a string like this
text_widget = "This is some text!"

#buttons are written with a square bracket like this
button_widget = "[This is a button"

#images are written with an exclamation mark like this
image_widget = "!Images\\Test1.png"

#if you want to start your text with an exclamation mark or square bracket, manually input a widget like this:
manual_widget = {
    "type": "text", #replace with "button" or "image" for other widgets
    "text": "[This is the text i want" #replace with a "source" field for images
    }

#then the entire function would look like
#gui([text_widget,button_widget,image_widget,manual_widget])
#you can also change the fontsize, the font, and the title_text
#you can change the width and height but i would NOT recommend it
#because the function adapts the gui size to the widgets provided so it always fits them perfectly
#i probably put too much effort into this lol
#here are a few more examples of widget lists you could do
main_menu_widgets = ["MAIN MENU","Choose an option","[Start Game","[Settings","[quit"] #using this in a gui function would return "Start Game", "Settigns", or "Quit" depending on which button the user pressed.


#gui function, for creating a menu with the given widgets
def gui(widgets=[{'type':'text','text':'no widgets provided!'}],fontsize=10,font='Helvetica',title_text='Menu',width=0,height=0):
    widgets = widgetify(widgets)
    #create a screen
    root = Tk()
    root.title(title_text)
    #finds the longest bit of text out of the widgets
    #find widest widget
    longest = 0
    for widget in widgets:
        if widget['type'] == 'text' or widget['type'] == 'button':
            try:
                widget['text']
            except:
                print('Text and button widgets must have specified text!')
                return
            length = len(widget['text'])*fontsize*0.6
        elif widget['type'] == 'image':
            try:
                    widget['source']
            except:
                print('Image widgets must have specified source!')
                return
            length = PhotoImage(file=widget['source']).width()
        if length > longest:
            longest = length

    #if height is 0 (unset)
    if height == 0:
        for widget in widgets:
            match widget['type']:
                case 'text':
                    height += fontsize * 3
                case 'button':
                    height += fontsize * 5
                case 'image':
                    height += PhotoImage(file=widget['source']).height()
        height = int(height)
        #calculate height by amount of buttons and size of title and buttons
    #if width is 0 (unset)
    if width == 0:
        #calculate width based on longest text
        width = int(longest) + 100
    
    root.geometry(f'{width}x{height}')
    #create a Result object for storing what the user clicks on
    result = Result()
    #function that runs when a button is pushed
    def button_push(result,text):
        #set the result property of the given Result object to the text of the button
        result.result = text
        #kill the screen
        root.destroy()
    #make an empty list for the buttons
    buttons = []
    #loop through the widgets
    for widget in widgets:
        #make sure widget has a specified type
        try:
            widget['type']
        except:
            print('Widgets must have a specified type!')
            return
        match widget['type']:
            #if it is a text widget
            case 'text':
                
                #create a label with the line of text, and place it on the screen
                label = Label(root,text=widget['text'],font=(font,fontsize))
                label.pack(pady=fontsize/2)
            #if it is a button widget
            case 'button':
                text = widget['text']
                #make a button with given font and size that runs the button push function
                button = Button(root,text=text,command = lambda text=text: button_push(result,text),font=(font,fontsize))
                #add it to the buttons list
                buttons.append(button)
                #put it on the screen
                button.pack(pady=fontsize/2)
            #if it is an image widget
            case 'image':
                #make an image from the specified source
                image = PhotoImage(file=widget['source'])
                #put it in a label
                image_label = Label(root,image=image)
                #put that label on the screen
                image_label.pack(pady=fontsize/2)
    #run the screen
    root.mainloop()
    #return the result property of the Result object
    return result.result

def widgetify(text):
    method = type(text)
    if method is list:
        for i, line in enumerate(text):
            text[i] = widgetify(line)
    elif method is str:
        if text[0] == '[':
            text = {"type":"button","text":text[1:]}
        elif text [0] == '!':
            text = {"type":"image","source":text[1:]}
        else:
            text = {"type":"text","text":text}
            
    elif method is dict:
        pass
    else:
        text = "ERROR: Widgets must be dictionaries or strings!"
    return text
