import cv2 as cv

video = cv.VideoCapture("vid1.mp4")

while True:
    isTrue, frame = video.read()
    
    
    if frame is not None:
        cv.imshow("Video",frame)
    else:
        print("The end")
        exit(1)
    
    if cv.waitKey(15) & 0xFF == ord("C"):
        break

video.release()
cv.destroyAllWindows()
cv.waitKey(0)