import cv2 as cv
import numpy as np

pic3 = cv.imread('Pic3.jpg')
cv.imshow('Pic3', pic3)

pic3_canny = cv.Canny(pic3, 125, 175)


contours, hierarchies = cv.findContours(pic3_canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 
pic3 = cv.imread('Pic3.jpg')
cv.drawContours(pic3 , contours, -1, (0, 0, 255), 1)
cv.imshow('Contours_canny', pic3)


pic3_gray = cv.cvtColor(pic3, cv.COLOR_BGR2GRAY)
blur_7 = cv.GaussianBlur(pic3_gray, (7, 7), cv.BORDER_DEFAULT)
contours, hierarchies = cv.findContours(blur_7, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 
pic3 = cv.imread('Pic3.jpg')
cv.drawContours(pic3 , contours, -1, (0, 0, 255), 1)
cv.imshow('Contours_blur', pic3)




cv.waitKey(0)