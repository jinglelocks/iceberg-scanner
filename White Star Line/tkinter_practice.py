# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:56:48 2022

@author: alexa
"""

from tkinter import *

# first thing to do is create a frame
root = Tk() # set the root widget (the frame to work within)

my_label = Label(root, text="Hello World!") # create label widget, now have to put it into root
# two ways, one is pack, shoves it in there at first available spot
my_label.pack()

# last thing to do is create an event loop
root.mainloop()
