# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:49:48 2022

@author: alexa
"""

from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Title')
root.geometry("400x200")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()
    
button1 = Button(root, text="Graph it!", command=graph)
button1.pack()


root.mainloop()