# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 09:05:23 2022

@author: alexa
"""
import numpy as np
test = [1,2,3,4,5,6]
test = np.asarray(test).reshape([2,3])
print(test)
print(test[0,0])
print(test[0,2])


test2 = [[1, 2],[3, 4]]
x = 0
y = 1
print(test2[x,y])