import cv2 as cv
import numpy as np

pic2= cv.imread('pic2.jpg')
cv.imshow('Pic2',pic2)


def translate(img, x, y): 
    
    transMat = np.float32([[1, 0, x], [0, 1, y]]) 
    dimentions = (img.shape[1], img.shape[0]) 
    
    return cv.warpAffine(img, transMat, dimentions)



pic2_translated=translate(pic2, 50, 50)# I changed x=200 to 50,because when i did translate with x=200 , i see only black screen, no pic :)
cv.imshow('Translated', pic2_translated)

def rotate(img, angle, rotPoint = None): 
    
    (height, width) = (img.shape[0], img.shape[1])
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) 
    dimentions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimentions)


rotated_pic2_tr=rotate(pic2_translated,50)
cv.imshow('Rotated', rotated_pic2_tr)

fliped_pic2 = cv.flip(rotated_pic2_tr, -1)
cv.imshow('Fliped', fliped_pic2)
















cv.waitKey(0)