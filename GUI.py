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

master.mainloop()'''

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