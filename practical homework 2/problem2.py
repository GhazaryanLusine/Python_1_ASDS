import cv2 as cv

pic1 = cv.imread('pic1.jpg') 
cv.imshow('Pic1', pic1)
                 
                 
blur_3 = cv.GaussianBlur(pic1, (3, 3), cv.BORDER_DEFAULT) 
blur_11 = cv.GaussianBlur(pic1, (11, 11), cv.BORDER_DEFAULT) 
cv.imshow('Blur_3', blur_3)
cv.imshow('Blur_11', blur_11)
                 
                 
                 
                 
                 
cv.waitKey(0)