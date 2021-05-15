import cv2 as cv

def rescaleFrame(frame, scale =0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

pic = cv.imread("pic1.jpg")
pic_rescaled= rescaleFrame(pic, 0.5)

cv.imshow("Pic1",pic)
cv.imshow("Pic1_rescales",pic_rescaled)

cv.waitKey(0)