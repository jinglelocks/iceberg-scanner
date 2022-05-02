# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:42:03 2022

@author: alexa
"""
from tkinter import * 
# only supports 2 image types, need to import another module
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to code')
#root.iconbitmap('{file/path}')
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

# define the thing
# put the image in something else
# put that something else on the screen
# images can be added to almost every widget

my_img = ImageTk.photoimage(image.open("placeholder.png"))
my_label = Label(image=my_img)
my_label.pack()



root.mainloop()