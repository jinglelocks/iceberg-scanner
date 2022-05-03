# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:51:49 2022

@author: alexa
"""
import csv
import rasterio
from rasterio.plot import show
import matplotlib
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy
import time
import tkinter as tk

root = tk.Tk()
root.title("White Star Line Iceberg Scanner")
root.geometry('900x200')

def iceberg_scan(radar_file, lidar_file):
    start = time.time()
    raw_data = open(radar_file, 'r')
    data_array = numpy.loadtxt(raw_data, delimiter = ",")
    raw_data.close
    data_array = data_array.astype('int32')
    #print(data_array)
    #print(type(data_array))
    print("start of array check")
    print("dimensions of data array:",data_array.ndim)
    print("shape of data array:",data_array.shape) # make a check to see if they are the same shape
    #rows, columns = data_array.shape
    #print("# of rows:",rows)
    #print("# of columns:",columns)
    #print(data_array[data_array >= 100])
    result = numpy.where(data_array >= 100)
    #print(result)
    #result = numpy.where(data_array >= 0)
    #print("x values:",result[0])
    #print("y values:",result[1])
    #list_of_coords = list(zip(result[0], result[1]))
    #print(list_of_coords)
    #return list_of_coords
    volume = 0
    for i in range(len(result[0])): # iterate through all positions within the x array of the result 2d array (same dimensionality as y)
        x = result[0][i] # ith value in the x array
        y = result[1][i] # ith value in the y array
        with open(lidar_file, 'r'): # read lidar data
            lidar_array = numpy.loadtxt(lidar_file, delimiter = ",")
            lidar_array = lidar_array.astype('int32')  
        height_metres = lidar_array[x][y]/10 # height value at xy of lidar array is in units of 10cm, /10 converts to metres
        #print(height_metres)
        volume = volume + height_metres*1*1 # converting to volume by doing HxWxL
    mass_above_water = volume*900 # mass = volume*density
    mass_total = 10*mass_above_water # 10% of the mass is above water, so total is 10* that value
    print("mass above water =",mass_above_water)
    print("total mass =",mass_total)
    total_volume = volume*10
    print("total volume =", total_volume)
    end = time.time()
    print(end-start) # This version: 76.65096712112427
    result_mass.config(text="Total mass= "+str(mass_total))
    result_vol.config(text="Total mass= "+str(total_volume))
    if mass_total > 36000000:
        result_pull.config(text="Iceberg mass exceeds limit, tow not possible.")
    else:
        result_pull.config(text="Iceberg mass under limit, tow possible.")
        
def show_radar(radar_file):
    matplotlib.pyplot.ylim(0, 300) #
    matplotlib.pyplot.xlim(0, 300) # set graph limits
    with open(radar_file, 'r'): # read lidar data
        radar_array = numpy.loadtxt(lidar_file, delimiter = ",")
        radar_array = radar_array.astype('int32')  
        matplotlib.pyplot.imshow(radar_array)

def show_lidar(lidar_file):
    matplotlib.pyplot.ylim(0, 300) #
    matplotlib.pyplot.xlim(0, 300) # set graph limits
    with open(lidar_file, 'r'): # read lidar data
        lidar_array = numpy.loadtxt(lidar_file, delimiter = ",")
        lidar_array = lidar_array.astype('int32')  
        matplotlib.pyplot.imshow(lidar_array) 
        
def quit_scanner():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
                    
# define radar and lidar input files
radar_file = 'white1.radar'
lidar_file = 'white1.lidar'
                    
# setting button and label widgets                    
button_scan = tk.Button(root, text="Scan Iceberg", height=5, width=30, command=lambda: iceberg_scan(radar_file,lidar_file))
button_radar = tk.Button(root, text="Show radar image", height=5, width=30, command=lambda: show_radar(radar_file))
button_lidar = tk.Button(root, text="Show lidar image", height=5, width=30, command=lambda: show_lidar(lidar_file))
button_quit = tk.Button(root, text="Quit", height=5, width=30, command=quit_scanner)

button_scan.grid(row=0,column=0)
button_radar.grid(row=0,column=1)
button_lidar.grid(row=0,column=2)
button_quit.grid(row=0,column=3)

result_mass = tk.Label(root,text="")
result_vol = tk.Label(root,text="")
result_pull = tk.Label(root,text="")

result_mass.grid(row=1,column=0,columnspan=4)
result_vol.grid(row=2,column=0,columnspan=4)
result_pull.grid(row=3,column=0,columnspan=4)


root.mainloop()





"""
fig = matplotlib.pyplot.figure(figsize=(5, 4), dpi=100)
t = numpy.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * numpy.sin(2 * numpy.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid(row=0,column=1)
"""

#iceberg_scan(radar_file, lidar_file)
#show_lidar(lidar_file)
#show_radar(radar_file)


# get a specific element [row, column]
#print(data_array[137,150])
# get a specific row
#print(data_array[0, ])
# get a specific column
#print(data_array[:, 2])
#[startindex:endindex:stepsize]
    
# print(lidar_data > 100) # returns false or true
#print(numpy.any(lidar_data>=  100, axis =0))
# you can index with a list in numpy
#a = numpy.array([1,2,3,4,5,6,7,8,9])
#print(a[[1,2,8]])

#coordinates = list(zip(result[0], result[1]))
#for coord in coordinates:
    #print(coord)

"""
with open('white1.radar', 'r') as lidar_data:
    csv_reader = csv.reader(lidar_data)
    
    for line in lidar_data:
        for value in line:
            print(value)
"""