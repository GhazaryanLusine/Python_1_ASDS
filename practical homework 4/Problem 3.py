import cv2 as cv

pic1 = cv.imread('pic1.jpg') 
gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)

cv.imshow('gray', gray) 

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) 

cv.imshow('simple threshold', thresh) 


adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive threshold', adaptive_thresh) 

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive threshold gaussian', adaptive_thresh_gaussian) 


cv.waitKey(0)

