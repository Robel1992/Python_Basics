'''#----------------Making a window---------------------------
#Import tkinter 
import tkinter as tk


#initialize tk/ initialize window (Create Instance)
win = tk.Tk()


#Give the window a title (Creat a title to GUI)
win.title("Out First GUI")


#Make a loop for things to start - the event loop
win.mainloop()


#---------------------------Making a button---------------------------

#Import tkinter 
import tkinter as tk
master = tk.Tk()

def closewindow():
    exit()

#Make win have a button
button = tk.Button(master, text="Close Window", command=closewindow)

button.pack()

master.mainloop()

#-----------------------------Creating a frame within screen --------------------
#Import tkinter 
import tkinter as tk
master = tk.Tk()

def closewindow():
    exit()

#Make win have a button
button = tk.Button(master, text="Close Window", command=closewindow)

button.pack()

master.mainloop()

#-----------------------------Creating an entry for two people --------------------
from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

mainloop()

#-----------------------------Creating an entry for two people --------------------
from tkinter import *
import tkinter.messagebox

root = Tk()

root.title("Username & Passowrd")

#the label of the box
label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")

#The entry boxes to get the information
entry_1 = Entry(root)
entry_2 = Entry(root)

#placeing the elements we created ABOVE!
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, stick=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

#keep me logged in

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

#Pick a color
color = root.colormapwindows(root)

mainloop()

#----------------------------example code ----------------------
from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print(e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)

#------------------My do nothing app ----------------S
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()


#=---------------------=-=-=-=-=-=-=-=
from tkinter import *


def check_expression():
    #Your code that checks the expression
    varContent = inputentry.get() # get what's written in the inputentry entry widget
    outputtext.delete('0', 'end-1c') # clear the outputtext text widget
    outputtext.insert(varContent)

root = Tk()
root.title("Post-fix solver")
root.geometry("500x500")

mainframe = Frame(root)
mainframe.grid(column=0, row=0)

inputentry = Entry(mainframe)
inputentry.grid(column=1, row=1)

executebutton = Button(mainframe, text="Run", command=check_expression)
executebutton.grid(column=1, row=5)              

outputtext = Text(mainframe)
outputtext.grid(column=1, row=5)

root.mainloop()

#-------------Example for Printing a Value -------------------
from tkinter import *
import time

def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "Hey whatsup bro, i am doing something very interresting.")
    #this creates a new label to the GUI
    label.pack() 
    button.destroy()


root = Tk()

button = Button(root, text="Print Me", command=printSomething) 
button.pack()


root.mainloop()'''

#---------------------Simple Calculator ---------------------------------
from tkinter import *

master = Tk()
master.title("Shitty Calculator")

#framework

#Print Answer
def function_class(string_var):
    label = Label(master, text= string_var)
    label.grid(row=0, column = 1)


def add():
    sum = int(first_number.get())+int(second_number.get())
    print(type(sum))
    function_class("+")
    label = Label(master, text= sum)
    label.grid(row=0, column = 4)

def sub():
    diff = int(first_number.get())-int(second_number.get())
    print(type(diff))
    function_class("-")
    label = Label(master, text= diff)
    label.grid(row=0, column = 4)

def mul():
    
    prod = int(first_number.get())*int(second_number.get())
    print(type(prod))
    function_class("x")
    label = Label(master, text= prod)
    label.grid(row=0, column = 4)

def div():
    if second_number.get() == "0":
        function_class("÷")
        label=Label(master, text="ERROR: DIVISION BY ZERO")
        label.grid(row=0, column = 4)

    quot = int(first_number.get())/int(second_number.get())
    print(type(quot))
    function_class("÷")
    label = Label(master, text= quot)
    label.grid(row=0, column = 4)

def clear_table():
    label=Label(master, text="                                                ")
    label.grid(row=0, column = 4)

#Turn first number and second number into a string
#first_number_val = StringVar()
#second_number_val = StringVar()

#the label of the box
label_1 = Label(master, text = "First Number")
label_2 = Label(master, text = "Second Number")
label_answer = Label(master, text = "The answer")
first_number = Entry(master, width=5)
second_number = Entry(master, width=5)



#placeing the elements we created ABOVE!
label_1.grid(row=1, column=0)
label_2.grid(row=1, column=2)
label_answer.grid(row=1, column = 4)

first_number.grid(row=0, column=0)
second_number.grid(row=0, column=2)


#Buttons
Button_add = Button(master, text="+", width=2, command = add) 
Button_add.grid(row=2, column=0)

Button_sub = Button(master, text="-", width=2, command = sub)
Button_sub.grid(row=2, column=1)

Button_mul = Button(master, text="x", width=2, command = mul)
Button_mul.grid(row=3, column=0)


Button_div = Button(master, text="÷", width=2, command = div)
Button_div.grid(row=3, column=1)

Button_equals = Button(master, text="=", width=3)
Button_equals.grid(row = 0, column=3)

Button_clear = Button(master, text="c", width =3, command=clear_table)
Button_clear.grid(row = 2 , column=2)


#master.geometry("500x500")

master.mainloop() 