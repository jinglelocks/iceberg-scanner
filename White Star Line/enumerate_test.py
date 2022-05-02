# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 19:59:42 2022

@author: alexa
"""

import matplotlib

data = [[0, 1, 0, 0,],[0, 0, 0, 0,],[0, 2, 1, 0],[1, 1, 1, 1],[0, 1, 1, 0],[0, 0, 0, 0,],[0, 0, 0, 0,]]

#print(data)

matplotlib.pyplot.ylim(0, 7) # the following is to plot the agents each "frame" of the animation
matplotlib.pyplot.xlim(0, 4) # set graph limits
matplotlib.pyplot.imshow(data)

for index1, inner_1 in enumerate(data):
    for index2, item in enumerate(inner_1):
        locations = []
        if data[index1][index2] > 1:
            #print("value",data[index1][index2])
            #print(index1, index2)
            locations.append(index1)
            locations.append(index2)
print(locations)
            

"""
for row in range(len(data)):
    for value in row:
        print(value)
    """
"""
    for value in row:
        if value > 1:
            print(data[value])
            """