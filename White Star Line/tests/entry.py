# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:56:48 2022

@author: alexa
"""

from tkinter import *

# first thing to do is create a frame
root = Tk() # set the root widget (the frame to work within)

def myClick():
    #myLabel = Label(root, text="Hello "+entry1.get())
    hello = "Hello " + entry1.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
entry1 = Entry(root)
entry2 = Entry(root, width=50, fg="blue", bg="white", borderwidth=5)
entry1.pack()
#entry2.pack()
entry1.insert(0, "Enter your name")


my_button1 = Button(root, text="Enter your name", command=myClick)
my_button1.pack()


# last thing to do is create an event loop
root.mainloop()

