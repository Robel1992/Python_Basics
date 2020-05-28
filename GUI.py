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

mainloop()'''

#-----------------------------Creating an entry for two people --------------------
from tkinter import *

root = Tk()

#the label of the box
label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")

#The entry boxes to get the information
entry_1 = Entry(root)
entry_2 = Entry(root)

#placeing the elements we created ABOVE!