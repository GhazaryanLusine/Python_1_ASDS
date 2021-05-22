import cv2 as cv


pic2= cv.imread('Pic2.jpg')
cv.imshow('Pic2',pic2)

resize_big = cv.resize(pic2, (pic2.shape[1]*2, pic2.shape[0]), interpolation = cv.INTER_AREA) 
cv.imshow('Resize_big', resize_big)

resize_small = cv.resize(pic2, (pic2.shape[1], pic2.shape[0]//2), interpolation = cv.INTER_CUBIC) 
cv.imshow('Resize_small', resize_small)



cv.waitKey(0)