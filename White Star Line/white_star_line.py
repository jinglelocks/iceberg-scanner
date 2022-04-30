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

raw_lidar = open(lidar_file, 'r')
lidar_data = numpy.loadtxt(raw_lidar, delimiter = ",")
raw_lidar.close
lidar_data = lidar_data.astype('int32')

print(lidar_data)
print(type(lidar_data))
print("dimensions of lidar_data array:",lidar_data.ndim)
print("shape of lidar data:",lidar_data.shape) # make a check to see if they are the same shape
rows, columns = lidar_data.shape
print("# of rows:",rows)
print("# of columns:",columns)
print(lidar_data[lidar_data >= 100])
result = numpy.where(lidar_data >= 100)
print(result)

# get a specific element [row, column]
#print(lidar_data[137,150])
# get a specific row
#print(lidar_data[0, ])
# get a specific column
#print(lidar_data[:, 2])
#[startindex:endindex:stepsize]
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


matplotlib.pyplot.ylim(0, 300) # the following is to plot the agents each "frame" of the animation
matplotlib.pyplot.xlim(0, 300) # set graph limits
matplotlib.pyplot.imshow(lidar_data)