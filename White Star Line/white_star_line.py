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
import numpy

lidar_file = 'white1.lidar'
radar_file = 'white1.radar'

def explore_data(input_file):
    raw_data = open(input_file, 'r')
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
    #result = numpy.where(data_array >= 0)
    #print("x values:",result[0])
    #print("y values:",result[1])
    list_of_coords = list(zip(result[0], result[1]))
    print(list_of_coords)
    
    
    return list_of_coords

    # get a specific element [row, column]
    #print(data_array[137,150])
    # get a specific row
    #print(data_array[0, ])
    # get a specific column
    #print(data_array[:, 2])
    #[startindex:endindex:stepsize]

#lidar_data = explore_data(lidar_file)
iceberg_coords = explore_data(radar_file)
#print(lidar_data)
#print(iceberg_coords[0])
#print(iceberg_coords[0][0])

def height_check(input_file):
    with open(input_file, 'r'):
        data_array = numpy.loadtxt(input_file, delimiter = ",")
        data_array = data_array.astype('int32')
        return data_array

iceberg_heights = height_check(lidar_file)
print(iceberg_heights[135])



for x in iceberg_coords:
    for y in x:
        print(iceberg_heights[x,y])
    
"""
    for x in lidar_data:
        print(radar_data[x])
        for y in lidar_data:
            print(radar_data[y])
"""
            
"""            
    x_loc = lidar_data[0][0]
    y_loc = lidar_data[0][1]
    print(radar_data[x_loc,y_loc])
"""
        

#matplotlib.pyplot.ylim(0, 300) # the following is to plot the agents each "frame" of the animation
#matplotlib.pyplot.xlim(0, 300) # set graph limits
#matplotlib.pyplot.imshow(lidar_data)
#matplotlib.pyplot.imshow(radar_data)
    
    
    
    
    
    
    
    
"""
for row in lidar_data:
    for value in row:
        if value >= 100:
            print(value)
            #print(type(value))
"""            
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