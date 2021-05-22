import cv2 as cv

pic1 = cv.imread('pic1.jpg')
cv.imshow('Pic1', pic1)

gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)


























cv.waitKey(0)