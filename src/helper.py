# This is a library of helpful functions made by BDZ.
# Anyone is welcome to use any of them for any purpose.
# Here's a quick overview of all of them:
# Hit alt+z to wrap text and make this actually readable
# btw if you are making a terminal-based program please read f(), choice_input(), int_input(), and list_choice() because they are UNBELIEVABLY useful. I use them all the time. Please do yourself a favor and read them.
# and if you are using tkinter check out gui() as it is pretty useful

# f() takes two arguments, one for a format and the second for text. It returns the text with the given format, and defaults to an empty string if no text is provided. Formats can be colors like "gray" or "blue" or a couple special ones like "clear" to clear the screen or "###" to print a gray triple #

# uinput() takes a user input in a pretty way, strips it, and converts it to lowercase.

# stringify() takes any list and converts it entirely to strings. Somewhat useful for generating lists of number strings with range. It also lowers all items.

# chance() takes a float between 0 and 1 and returns true x percent of the time. so 0.25 would be a 25% chance to return true

# choice_input() is probably the most useful. It takes a list of strings as the first argument and a prompt as the second (optional), and an error message as the third input (optional). It takes a user inputs until the input matches one of the items in the list. So if you wanted the user to pick a number from 1-4, you could say choice_input([1,2,3,4],"Pick a number from 1-4: "). It automatically lowers the input, so don't put in options with uppercase letters, and stringifies the list (so numbers are okay in the list, as they'll be converted to strings). The optional third argument is an error message to be displayed if the input does not match something from the list.

# int_input() is similar to choice input, but doesn't take the first argument. Instead, it only accepts inputs that can be converted to a float (ie 1, 7.6, -12 would all be valid). It automatically converts it to a float for you. It also accepts an optional max and min argument.(min defaults to 0). Arguments in order are: prompt, error, max, min. All are optional

# csv_to_dictionary accepts the file path to a csv file and returns a list of dictionaries with the content of the csv. Pretty self explanatory.

# save_csv() is the opposite of csv_to_dictionary(), it takes a dictionary as the first argument and a file path as the second.

# uniprint accepts anything. ANYTHING. and it pretty prints it. You could nest tuples in sets in dictionaries in dictionaries full of floats, integers, whatever. It will print it with coloring and indentation.

# search() takes a list of dictionaries (such as from csv_to_dictionary()) and asks the user for a prompt. Then it returns a list of all the dictionaries that contain that prompt in any of their values.

# list_choice() is incredibly useful. It accepts a list and prompt and prints the prompt, then each item in the list with a number assigned. Then it asks the user for a choice, which can be a number assigned to a choice or one of the choices. It returns what they chose. Super useful for making menus, to make a menu where the user picks between search, add, or quit you would use just this one line of code: choice = list_input(['search','add','quit'],'What would you like to do?')

# gui() texts a list of strings to display as lines of text and a list of strings to display as buttons. It will create a gui with a width and height that perfectly fits the displayed text and buttons. It returns the text on whichever button the user clicks.

import random
import csv
from tkinter import *

#text formatting function
def f(format, text = ''):
    formatters = { 
        'gray': "\033[30m",
        'grey': "\033[30m",
        'green': "\033[32m",
        'clear': "\033c",
        'blue': "\033[34m",
        'white': "\033[0m",
        '###': "\033[30m###\033[0m",
        'red': "\033[31m",
        'magenta': "\033[31m",
        'cyan': "\033[36m",
        'lime': "\033[92m",
        'yellow': "\033[93m",
        'light blue': "\033[94m",
        "bright red": "\033[91m"
    }
    try:
        return formatters[format] + text + "\033[0m"
    except:
        return text
    
#user input
def uinput(prompt = '> '):
    uinput = input(prompt + '\033[34m').lower().strip()
    print(f("white"),end='')
    return uinput

def stringify(list):
    #turn every item in the given list into a string
    return [str(i).lower() for i in list]

#random chance based on chance given
def chance(chance):
    if random.random() <= chance:
        return True
    return False

#input from choices
def choice_input(choices,prompt = '> ',error = 'Please select a valid choice!'):
    #loop forever
    while True:
        #take user input
        choice = uinput(prompt)
        #if it is a valid choice
        if choice in stringify(choices):
            #return it
            return choice
        #otherwise
        else:
            #tell the user to select a valid choice
            print(error)


#number input
def int_input(prompt='> ',error = 'Input is not a number',max = 100000,min = 0):
    #loop fovever
    while True:
        #get user input
        num = uinput(prompt)
        try:
            num = float(num)
        #if it is not a number
        except:
            #tell user
            print(error)
            continue
        #if it is within range
        if num <= max and num >= min:
            #return it
            return num
        else:
            print('Input is out of range!')


    
#search dictionary function
def search(dictionaries):
    #query = take user input "search"
    query = uinput("Search: ")
    #create list for potential matches
    potential = []
    #loop over list
    for dic in dictionaries:
        #loop through keys of current dictionary:
        for feild in dic.keys():
            #if potentials already contains current dictionary:
            if dic in potential:
                #break loop
                break
            #if current feild of current dictionary contains query:
            if query in dic[feild].lower():
                #add current dictionary to potential dictionaries
                potential.append(dic)
    #return potentials
    return potential


#print anything function
def uniprint(to_print, indentation = ''):
    #get type of thing to print
    method = type(to_print)
    #if it is an integer, float, or string
    if method is int or method is str or method is float:
        #print it
        print(indentation + to_print)
    #if it is a list, tuple, or set
    elif method is list or method is tuple or method is set:
        #loop through it
        for item in to_print:
            #uniprint item
            uniprint(item, indentation)
            #print new line
            print()
    #if it is a dictionary:
    elif method is dict:
        #loop through the keys
        for key in to_print.keys():
            #get type of value
            nest_method = type(to_print[key])
            #if value is a string, float, or integer:
            if nest_method is int or nest_method is str or nest_method is float:
                #print the key and a colon followed by the value
                print(f'{indentation}{key}: \033[34m{to_print[key]}\033[0m')
            #otherwise:
            else:
                #print the key and a colon
                print(f'{indentation}{key}:')
                #uniprint value
                uniprint(to_print[key],indentation + ' ')

#choice from a list
def list_choice(choices,prompt = 'Choose an option:'):
    choices = stringify(choices)
    #print prompt
    print(prompt)
    #create a list with a number for each choice
    choice_ints = list(range(1,len(choices) + 1))
    #loop through that list
    for i in choice_ints:
        #print each item with its number (ie 1. Thing 1)
        print(f'{i}. {f('gray',choices[i-1].title())}')
    #get an input that is either a number assigned to an item or one of the items
    chosen = choice_input(choice_ints + choices)
    #if it was a number assigned to an item
    if chosen in stringify(choice_ints):
        #return the item that number was assigned to
        return choices[int(chosen) - 1]
    #otherwise
    else:
        #return what they chose
        return chosen
    


#result class, used for passing information locally to globally
class Result():
    def __init__(self):
        self.result = ''

#gui function, for creating a menu with the given text and buttons
def gui(text=['No text provided'],options=['continue'],fontsize=10,font='Helvetica',title_text='Menu',width=0,height=0):
    #finds the longest bit of text out of the text and all the buttons
    #find longest text
    longest = 0
    for line in text:
        length = len(line)*fontsize*0.6
        if length > longest:
            longest = length
    for i in options:
        length = len(i)*fontsize*0.6
        if length > longest:
            longest = length
    #if height is 0 (unset)
    if height == 0:
        #calculate height by amount of buttons and size of title and buttons
        height = int(len(text)*fontsize*3 + len(options) * fontsize * 5)
    #if width is 0 (unset)
    if width == 0:
        #calculate width based on longest text
        width = int(longest) + 100
    #create a screen
    root = Tk()
    root.title(title_text)
    root.geometry(f'{width}x{height}')

    #loop through the text
    for line in text:
        #create a label with the line of text, and place it on the screen
        label = Label(root,text=line,font=(font,fontsize))
        label.pack(pady=fontsize/2)
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
    #loop through options
    for option in options:
        #make a button with given font and size that runs the button push function
        button = Button(root,text=option,command = lambda option=option: button_push(result,option),font=(font,fontsize))
        #add it to the buttons list
        buttons.append(button)
        #put it on the screen
        button.pack(pady=fontsize/2)
    #run the screen
    root.mainloop()
    #return the result property of the Result object
    return result.result