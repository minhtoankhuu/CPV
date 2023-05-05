#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv
import numpy as np

def Function1():
    background = np.zeros((455, 455))
    background += 455
    cv.imshow("While BackGround", background)
    cv.waitKey(0)
    cv.destroyAllWindows()

Function1()


# In[ ]:




