import numpy as np
import cv2 as cv

pic2= cv.imread("pic2.jpg")
cv.imshow("pic2" ,pic2)

cv.circle(pic2, (300, 300), 100, (0, 0, 255), thickness = 3)
cv.imshow('Circle', pic2)

cv.waitKey(0) 