import cv2 as cv


pic1= cv.imread("pic1.jpg")

cv.imshow("pic1", pic1)

cv.line(pic1, (0,400), (1024,0), (255, 255, 180), thickness = 2)
cv.imshow('Line', pic1)

cv.waitKey(0)