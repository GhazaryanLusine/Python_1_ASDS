import numpy as np
import cv2 as cv

pic2= cv.imread("pic2.jpg")
cv.imshow("pic2" ,pic2)

cv.rectangle(pic2, (80,80), (400,400), (18, 255, 255), thickness = 2)
cv.imshow('Rectangle', pic2)

cv.waitKey(0) 