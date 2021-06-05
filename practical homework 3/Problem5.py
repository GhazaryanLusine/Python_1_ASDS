import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype = 'uint8')


rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (179, 50, 255), -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (179, 50, 255), -1)


bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor) 

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or) 


blank1 = np.zeros((400,400,3), np.uint8)
rectangle_pink = cv.rectangle(blank1.copy(), (30, 30), (370, 370), (255, 153, 255), -1)
circle_pink = cv.circle(blank1.copy(), (200, 200), 200, (255, 153, 255),-1)

bitwise_xor_pink = cv.bitwise_xor(rectangle_pink, circle_pink)

cv.imshow('bitwise_xor_pink', bitwise_xor_pink)

cv.waitKey(0)

