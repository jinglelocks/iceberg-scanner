# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:30:54 2022

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

def iceberg_scan(radar_file, lidar_file):
    start = time.time()
    with open(radar_file, 'r'):
        radar_array = numpy.loadtxt(radar_file, delimiter = ",")
        radar_array = radar_array.astype('int32')
        #print(radar_array[150][135])
        #print(numpy.where(radar_array[150] >= 100))
        
        locs = []

        for row in radar_array:
            if len(numpy.where(row >= 100)[0]) > 1:  
                positions = numpy.where(row >= 100) # where in the current row is a value >= 100
                print(positions)
            else:
                pass
            

"""
          flag = 0 # For marking end of iceberg
          x_coordinates = []
          for i in range(len(positions[0])-1):
            if positions[0][i+1]-positions[0][i] != 1:
              temporary_list = [x for x in range(flag,i+1)] # all values between last flag and identified discontinuity 
              x_coordinates.append([positions[0][x] for x in temporary_list]) #   Store all values between edge and last flagged point
              flag = i+1
              
            if i+1 == (len(positions[0])-1):
              temporary_list = [x for x in range(flag,i+2)]
              x_coordinates.append([positions[0][x] for x in temporary_list])
          locs.append(x_coordinates)
        
        
        for l in locs:
          print(l)
"""
        
        
        


# define radar and lidar input files
radar_file = 'white1.radar'
lidar_file = 'white1.lidar'

iceberg_scan(radar_file, lidar_file)

