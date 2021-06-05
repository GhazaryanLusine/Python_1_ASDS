import cv2 as cv
import numpy as np

pic1 = cv.imread('pic1.jpg') 

cv.imshow('Pic1', pic1) 

blue, green, red = cv.split(pic1)


cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)















cv.waitKey(0)