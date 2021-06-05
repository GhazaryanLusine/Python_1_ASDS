import cv2 as cv
import numpy as np

pic2 = cv.imread('Pic2.jpg') 
cv.imshow('Pic2', pic2)

blank = np.zeros(pic2.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (pic2.shape[1]//2, pic2.shape[0]//2), 50, 255, -1)

masked_image = cv.bitwise_and(pic2,pic2, mask=mask)

cv.imshow('result', masked_image)

 
cv.waitKey(0)