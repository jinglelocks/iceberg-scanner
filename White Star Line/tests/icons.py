# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:42:03 2022

@author: alexa
"""
import tkinter
# only supports 2 image types, need to import another module
from PIL import ImageTk,Image

root = tkinter.Tk()
root.title('Learn to code')
#root.iconbitmap('{file/path}')
button_quit = tkinter.Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

# define the thing
# put the image in something else
# put that something else on the screen
# images can be added to almost every widget
img = Image.open("placeholder.png")
my_img = ImageTk.PhotoImage(img)
my_label = tkinter.Label(root, image=my_img)
my_label.pack()



root.mainloop()