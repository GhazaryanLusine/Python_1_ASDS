import cv2 as cv
import numpy as np

img = cv.imread('pic2.jpg') 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray) 


sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('combined sobel', combined_sobel) 



cv.waitKey(0)