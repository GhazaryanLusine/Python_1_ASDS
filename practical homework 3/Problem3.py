import cv2 as cv
import numpy as np

pic2 = cv.imread('pic2.jpg') 

cv.imshow('Pic2', pic2)


average = cv.blur(pic2, (5,5)) # even using small values we can see difference very well

cv.imshow('average blur', average)


bilateral1 = cv.bilateralFilter(pic2,15, 100, 50) # in this case we must use large values in order to see difference, but for example in this picture eyas didnt get blured even if i choose large values.
cv.imshow('bilateral', bilateral1)























cv.waitKey(0)