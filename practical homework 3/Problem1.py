import cv2 as cv
import numpy as np

pic1 = cv.imread('pic1.jpg') 
cv.imshow('Pic1', pic1)


rgb = cv.cvtColor(pic1, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

lab = cv.cvtColor(pic1, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 


gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


hsv = cv.cvtColor(pic1, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)


























cv.waitKey(0)