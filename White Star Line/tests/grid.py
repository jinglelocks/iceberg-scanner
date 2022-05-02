# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:56:48 2022

@author: alexa
"""

from tkinter import *

# first thing to do is create a frame
root = Tk() # set the root widget (the frame to work within)

my_label1 = Label(root, text="Hello World!") # create label widget, now have to put it into root
my_label2 = Label(root, text="My name is Alex Camilleri") # create label widget, now have to put it into root
# two ways, one is pack, shoves it in there at first available spot
#my_label1.pack() # pack will keep position central even when window resized
# the other is grid, can define specific areas, relative to eachother
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=1)

my_label3 = Label(root, text="Many paths to similar ends").grid(row=2, column=3)





# last thing to do is create an event loop
root.mainloop()

