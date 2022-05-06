# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:23:00 2022

@author: Alex Camilleri
"""

import numpy
# simplified radar file, where 1 = ice
#11100000000000011110000000111100
#11100000000110011110000000000000
rows = [numpy.asarray([1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0]),numpy.asarray([1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])]

locations = [] # list to store location of each position of ice
for r in rows:
  positions = numpy.where(r > 0) # stores xy indexes of all values above 0 (so 1, ice) in a 2d array
  #print(r,positions)

  flag = 0 # For marking a disconuity (start of a new iceberg)
  x_coordinates = [] # list to store x coordinates
  for i in range(len(positions[0])-1): # iterating through the x array in the positions array, -1 is to avoid reaching the last position
    if positions[0][i+1]-positions[0][i] != 1: # if two adjacent values are not "1" apart from eachother, this shows a discontinuity in the iceberg
      temporary_list = [x for x in range(flag,i+1)] # all values between last flag and identified discontinuity
      x_coordinates.append([positions[0][x] for x in temporary_list]) # to store all values between edge and last flag point
      flag = i+1 # the value after the current i is the start of the discontinuity
     
    if i+1 == (len(positions[0])-1): # if i is the penultimate value in positions[0]
      temporary_list = [x for x in range(flag,i+2)] # store the last flag, up to the "next position along", taking advantage of the fact that range doesn't extend to the final value
      x_coordinates.append([positions[0][x] for x in temporary_list]) # temporary list stores places, now looking for positions of those places
  locations.append(x_coordinates)

#For each corner that initiates an iceberg, need to store its length (how many rows the iceberg exists for) - [row, corner position in row, width, length]
corners = []
info = []
for rowcount in range(len(locations)): # Go through every row in locations
  for berg in locations[rowcount]: # each value in locations list is a berg
    if berg[0] not in corners: # locating corners - this whole code assumes rectangular icebergs, everything is in reference to top left corner
      corners.append(berg[0]) # if not in the corner list, add it
      info.append([rowcount,berg[0],len(berg),0]) # storing the row of the berg, the corner, the length and the height (0 because it's the start of the iceberg)
    else: # if the berg[0] IS in corners, then not at the top left of the iceberg anymore
      ping = numpy.where(corners == berg[0])[0][0] # finding where in the the corners list berg[0] exists
      #print(numpy.where(corners==berg[0]) # this will return the position encased in two layers of brackets, so need to add [0][0] to access position directly
      info[ping][3] = info[ping][3] + 1 # accessing the height and adding 1 to it
      #find where it is in corners which is the same place in info
#print(corners)

berg_coordinates_final = [] # this stores the coordinates of each iceberg separately
for i in info:
  #print(i) # checking how it looks
  temp = []
  for j in [y for y in range(i[0],i[0]+i[3]+1)]: # i[0] is the start row, i[0]+i[3] is the height, need to +1 because range doesn't go to the last one
    temp.append([[j,x] for x in range(i[1],i[1]+i[2])]) # [j,x] is an xy coordinate pair. j iterates through the y dimension (height) and x takes the range of the length of the iceberg
  berg_coordinates_final.append(temp) # appending coordinates to the final list

# printing results, printing all the coordinates for individual icebergs wrapped up in layers of lists. Now not enough time to separate them out and integrate this code with the white_star_line.py
print("there are "+str(len(berg_coordinates_final))+" rectangular icebergs")
for i in range(len(berg_coordinates_final)):
  print("Iceberg "+str(i)+" extends over coordinates:",berg_coordinates_final[i])
  print("------")
  
# this code took ages to cobble together, ran out of time, head hurts, need a long break