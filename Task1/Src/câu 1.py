#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 as cv
import numpy as np


def square(n, m):
    global background
    try:
        n = int(n)
        m = int(m)
        
        if n != 0 and n != 1:
            print("Value of n in range[0,1]")
            return
        if n == 1:
            background = np.ones((m, m, 3))
            cv.imshow('White window', background)
            
        else:
            background = np.zeros((m, m, 3))
            cv.imshow('Black window', background)
        
        cv.waitKey(0)
        cv.destroyAllWindows()
        return background
    except ValueError:
        
        print("Values of n are interger")
        
def square_show():
    n = (input('enter n: '))
    m = (input('enter weight and height of square: '))
    square(n,m)

    
square_show()

