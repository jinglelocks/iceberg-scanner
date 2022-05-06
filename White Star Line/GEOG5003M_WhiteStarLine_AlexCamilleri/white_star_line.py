# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:51:49 2022

@author: Alex Camilleri
"""

"""
SETUP
"""
import csv # library to read/write text files
import numpy # numpy arrays used in place of lists in this code for efficiency
import matplotlib # library for plotting the radar and lidar data
import time # used for timing the code to make it more efficient
import tkinter as tk # used to create the GUI (must enable Tkinter backend graphic display in IDE)

root = tk.Tk() # initialise a Tk GUI "frame" window
root.title("White Star Line - Iceberg Scanner") # title in the top bar of the GUI
root.geometry('900x200') # set dimensions of the GUI window, found by playing with widget size and layout during development

radar_file = 'white1.radar' # define radar and lidar input files
lidar_file = 'white1.lidar'

"""
FUNCTIONS
"""
def scan_iceberg(radar_file, lidar_file): # function to scan the iceberg, takes two arguments: the white1.radar and white1.lidar files
    start = time.time() # getting the start time to time the code
    with open(lidar_file, 'r'): # using 'with open' removes the need to file.close when done
        lidar_array = numpy.loadtxt(lidar_file, delimiter = ",")  # numpy.loadtxt to read lidar file as a numpy array
    with open(radar_file, 'r'):
        radar_array = numpy.loadtxt(radar_file, delimiter = ",") # numpy.loadtxt to load radar file as a numpy array
        #radar_array = radar_array.astype('int32') # converted to int to avoid float errors, cut to try and increase efficiency
        ice_positions = numpy.where(radar_array >= 100) # stores the coordinates of values >= 100 in a 2d array, where [0] is array of "x values" and [1] is array of "y values"
        #print(numpy.shape(radar_array)) # checking dimensions of radar_array
        
    if numpy.shape(lidar_array) != numpy.shape(radar_array): # adding an error check to make sure the two files are of the same dimension
        result_report.config(text="Error, the two data files are not of identical dimension.") # tested this by using == instead of != since I know the files are of same dimension
    else: # if the files are of the same dimension, the iceberg will be assessed
    
        volume = 0 # beginning the volume variable at 0, ready to store sum of volumes gathered during the following loop
        for i in range(len(ice_positions[0])): # iterate through all positions in the x array of the result 2d array (same dimensionality as y)
            x = ice_positions[0][i] # variable for ith position in the x array
            y = ice_positions[1][i] # ith position in the y array
            height_metres = lidar_array[x][y]/10 # height value at [x][y] of lidar array is in units of 10cm, /10 converts to metres
            #print(height_metres)
            volume = volume + height_metres#*1*1 # converting to volume by doing HxWxL (pixels are 1x1), removed 1x1 operation to increase efficiency
        
        mass_above_water = volume*900 # mass = volume*density
        total_mass = 10*mass_above_water # 10% of the mass is above water, so total is 10* that value
        #print("mass above water =",mass_above_water)
        #print("total mass =",total_mass)
        total_volume = 10*volume
        #print("total volume =", total_volume)
        end = time.time()
        print(end-start) # this version = 0.17 s
        
        result_mass.config(text="Total mass= "+str(total_mass)+" kg") # sending results to empty labels in the GUI
        result_vol.config(text="Total volume= "+str(total_volume)+" m3")
        if total_mass > 36000000: # updating the empty result_pull label with a conditional tow-ability report 
            result = "Iceberg mass exceeds limit, tow not possible."
            result_pull.config(text=result)
        else:
            result = "Iceberg mass within acceptable limit, tow possible."
            result_pull.config(text=result) 
    
        with open('iceberg_report.txt', 'w', newline='') as report_file: # creating/opening the iceber_report.txt in write mode save the iceberg assessment (overwrites previous info)
            report = ("Total mass = ", total_mass, "Total volume = ", total_volume, result)
            writer = csv.writer(report_file, delimiter=',')
            writer.writerow(report)
        result_report.config(text="Report saved to source code directory.")
        #return ["Total mass = ", total_mass, "Total volume = ", total_volume, result]
        
def show_radar(radar_file): # function to read and display the white1.radar data
    matplotlib.pyplot.ylim(0, 300) #
    matplotlib.pyplot.xlim(0, 300) # set graph limits
    with open(radar_file, 'r'): # read lidar data
        radar_array = numpy.loadtxt(lidar_file, delimiter = ",")
        matplotlib.pyplot.imshow(radar_array)

def show_lidar(lidar_file): # function to read and display the white1.lidar data
    matplotlib.pyplot.ylim(0, 300) # set graph limits
    matplotlib.pyplot.xlim(0, 300) # 
    with open(lidar_file, 'r'): # read lidar data
        lidar_array = numpy.loadtxt(lidar_file, delimiter = ",")
        matplotlib.pyplot.imshow(lidar_array)

def quit_scanner():
    root.quit()     # stops mainloop
    root.destroy()  # "destroys" the tkinter frame and widgets
                    
"""
TK WIDGETS
"""         
# setting up buttons, could have made a subclass of the Button class   
button_scan = tk.Button(root, text="Scan Iceberg", height=5, width=31, command=lambda: scan_iceberg(radar_file, lidar_file)) # have to use a lambda command to pass arguments in function 
button_radar = tk.Button(root, text="Show radar image", height=5, width=31, command=lambda: show_radar(radar_file))
button_lidar = tk.Button(root, text="Show lidar image", height=5, width=31, command=lambda: show_lidar(lidar_file))
button_quit = tk.Button(root, text="Quit", height=5, width=31, command=quit_scanner)
#button_save = tk.Button(root, text="Save result", height=5, width=30, command=save_file) # removed save button feature

# placing buttons on interface grid, some trial and error was required to get the placement right
button_scan.grid(row=0,column=0) # two options for widget placement with tkinter
button_radar.grid(row=0,column=1) # .pack throws the widget in wherever it will fit
button_lidar.grid(row=0,column=2) # .grid allows definition of placement via relative rows/columns
button_quit.grid(row=0,column=3)

# definining empty labels to populate with information once the function runs using Label.config(text="")
result_mass = tk.Label(root,text="")
result_vol = tk.Label(root,text="")
result_pull = tk.Label(root,text="")
result_report = tk.Label(root,text="")

# placing the labels on the grid
result_mass.grid(row=1,column=0,columnspan=4)
result_vol.grid(row=2,column=0,columnspan=4)
result_pull.grid(row=3,column=0,columnspan=4)
result_report.grid(row=4,column=0,columnspan=4)

root.mainloop() # tkinter mainloop keeps the program running to wait for user input

"""
END OF PROGRAM
"""

"""
Test blocks and cut features
"""

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

    #print(ice_positions) # visualising the coordinates array
    #ice_positions = numpy.where(radar_array >= 0) # testing to see if all radar_array value positions can be found
    #print("x values:",ice_positions[0]) # visualising the x values (the [0] array in the ice_positions 2d array)
    #print("y values:",ice_positions[1]) # visualising the y values (the [1] array in the ice_positions 2d array)
    #list_of_coords = list(zip(ice_positions[0], ice_positions[1])) # zipping the x and y values in tuples, unnecessary really but helped me to check everything was looking ok
    #print(list_of_coords)
    #return list_of_coords

    #print(radar_array) # checking out the radar_array to see if appropriate
    #print(type(radar_array)) # checking the type to be sure what I'm dealing with
    #print("dimensions of radar array:",radar_array.ndim) # checking dimensions
    #print("shape of radar array:",radar_array.shape) # could use this to make a check that the input files are the same shape, raise an exception if not
    #rows, columns = radar_array.shape # since the radar_array is 2d, can put the x and y values in their own variables
    #print("# of rows:",rows)
    #print("# of columns:",columns)
    #print(radar_array[radar_array >= 100]) # testing if I could pull specific values

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