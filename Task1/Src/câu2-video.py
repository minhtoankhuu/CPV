#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv

cap = cv.VideoCapture(0)

print(cap)

while True:
    ret, frame = cap.read()
    #ret: true or false.
    if ret == True:
        print("image")
    
    cv.imshow("Webcam", frame)

    if cv.waitKey(1) & 0xff == ord('q'):
       break
cap.release()
cv.destroyAllWindows()


# In[ ]:




