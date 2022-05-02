# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:56:48 2022

@author: alexa
"""

from tkinter import *

# first thing to do is create a frame
root = Tk() # set the root widget (the frame to work within)

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()

my_button1 = Button(root, text="Click me!", state=DISABLED) # disable or enable
my_button2= Button(root, text="Click me!", padx=50) # change size with padx and pady
my_button3= Button(root, text="Click me!", padx=50, pady=50)
my_button4 = Button(root, text="Click me!", command=myClick) # button that runs a function
my_button5 = Button(root, text="Click me!", fg="blue", bg="red") # colouring text and button

my_button1.pack()
my_button2.pack()
my_button3.pack()
my_button4.pack()
my_button5.pack()

# last thing to do is create an event loop
root.mainloop()

