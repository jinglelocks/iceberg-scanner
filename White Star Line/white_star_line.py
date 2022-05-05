# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:51:49 2022

@author: alexa
"""
import csv
import numpy # numpy arrays used in place of lists in this code for efficiency
import matplotlib # library for plotting the radar and lidar data
import time # used for timing the code to make it more efficient
import tkinter as tk # used to create the GUI (must enable Tkinter backend graphic display in IDE)

root = tk.Tk() # initialise a Tk GUI "frame" window
root.title("White Star Line - Iceberg Scanner") # title in the top bar of the GUI
root.geometry('900x200') # set dimensions of the GUI window, found by playing with widget size and layout during development

def scan_iceberg(radar_file, lidar_file): # function to scan the iceberg, takes two arguments: the white1.radar and white1.lidar files
    start = time.time() # getting the start time of the run for testing purposes
    with open(radar_file, 'r'): # using with open removes the need to file.close when done
        radar_array = numpy.loadtxt(radar_file, delimiter = ",") # using numpy library numpy.loadtxt to load radar file csv
        radar_array = radar_array.astype('int32')
    #print(data_array)
    #print(type(data_array))
    #print("dimensions of data array:",data_array.ndim) #
    #print("shape of data array:",data_array.shape) # make a check to see if they are the same shape
    #rows, columns = data_array.shape
    #print("# of rows:",rows)
    #print("# of columns:",columns)
    #print(data_array[data_array >= 100])
    ice_positions = numpy.where(radar_array >= 100) # stores the coordinates of values >= 100 in a 2d array, where [0] is array of "x values" and [1] is array of "y values"
    #print(ice_positions) # visualising the coordinates array
    #ice_positions = numpy.where(data_array >= 0)
    #print("x values:",ice_positions[0])
    #print("y values:",ice_positions[1])
    #list_of_coords = list(zip(ice_positions[0], ice_positions[1]))
    #print(list_of_coords)
    #return list_of_coords
    volume = 0
    for i in range(len(ice_positions[0])): # iterate through all positions within the x array of the result 2d array (same dimensionality as y)
        x = ice_positions[0][i] # ith value in the x array
        y = ice_positions[1][i] # ith value in the y array
        with open(lidar_file, 'r'): # read lidar data
            lidar_array = numpy.loadtxt(lidar_file, delimiter = ",")
            lidar_array = lidar_array.astype('int32')  
        height_metres = lidar_array[x][y]/10 # height value at xy of lidar array is in units of 10cm, /10 converts to metres
        #print(height_metres)
        volume = volume + height_metres*1*1 # converting to volume by doing HxWxL
    mass_above_water = volume*900 # mass = volume*density
    total_mass = mass_above_water*10 # 10% of the mass is above water, so total is 10* that value
    #print("mass above water =",mass_above_water)
    #print("total mass =",total_mass)
    total_volume = volume*10
    #print("total volume =", total_volume)
    end = time.time()
    print(end-start) # This version: 74.85s
    result_mass.config(text="Total mass= "+str(total_mass)+" kg")
    result_vol.config(text="Total volume= "+str(total_volume)+" m3")
    if total_mass > 36000000:
        result = "Iceberg mass exceeds limit, tow not possible."
        result_pull.config(text=result)
    else:
        result = "Iceberg mass within acceptable limit, tow possible."
        result_pull.config(text=result)
    #return ["Total mass = ", total_mass, "Total volume = ", total_volume, result]
    #button_save.grid(row=1, column=3) # placing the save file button on interface after the calculation has run
    #global report
    report = ("Total mass = ", total_mass, "Total volume = ", total_volume, result)
    with open('iceberg_report.txt', 'w', newline='') as report_file:
        writer = csv.writer(report_file, delimiter=',')
        writer.writerow(report)
    result_report.config(text="Report saved to source code directory.")
        
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
    root.destroy()  # "destroys" the tkinter widgets and frame
                    
# define radar and lidar input files
radar_file = 'white1.radar'
lidar_file = 'white1.lidar'
            
# setting button and label widgets                    
button_scan = tk.Button(root, text="Scan Iceberg", height=5, width=30, command=lambda: scan_iceberg(radar_file, lidar_file))
button_radar = tk.Button(root, text="Show radar image", height=5, width=30, command=lambda: show_radar(radar_file))
button_lidar = tk.Button(root, text="Show lidar image", height=5, width=30, command=lambda: show_lidar(lidar_file))
button_quit = tk.Button(root, text="Quit", height=5, width=30, command=quit_scanner)
button_save = tk.Button(root, text="Save result", height=5, width=30, command=quit_scanner)

# placing buttons on interface grid
button_scan.grid(row=0,column=0)
button_radar.grid(row=0,column=1)
button_lidar.grid(row=0,column=2)
button_quit.grid(row=0,column=3)

result_mass = tk.Label(root,text="")
result_vol = tk.Label(root,text="")
result_pull = tk.Label(root,text="")
result_report = tk.Label(root,text="")

result_mass.grid(row=1,column=0,columnspan=4)
result_vol.grid(row=2,column=0,columnspan=4)
result_pull.grid(row=3,column=0,columnspan=4)
result_report.grid(row=4,column=0,columnspan=4)

root.mainloop()



"""    
def save_file(): # unused, couldn't get the report variable out of the scan_iceberg function without using a global variable
    report = scan_iceberg(radar_file, lidar_file) # idea was to show the "Save file" button at the end of the scan_iceberg run.
    with open('report.txt', 'w', newline='') as report_file:
        writer = csv.writer(report_file, delimiter=',')
        writer.writerow(report)
"""

"""
fig = matplotlib.pyplot.figure(figsize=(5, 4), dpi=100)
t = numpy.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * numpy.sin(2 * numpy.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid(row=0,column=1)
"""

#scan_iceberg(radar_file, lidar_file)
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