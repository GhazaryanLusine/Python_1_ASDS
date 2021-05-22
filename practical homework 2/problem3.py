import cv2 as cv

pic2 = cv.imread('Pic2.jpg')
cv.imshow('Pic2',pic2)


canny = cv.Canny(pic2, 125, 175)
cv.imshow('Pic2_Edges', canny)


blur_5 = cv.GaussianBlur(pic2, (5, 5), cv.BORDER_DEFAULT) 
canny_blur = cv.Canny(blur_5, 125, 175)
cv.imshow('Edges_blured', canny_blur)








cv.waitKey(0)