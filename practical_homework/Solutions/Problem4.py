import cv2 as cv

def rescaleFrame(frame, scale =0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

video = cv.VideoCapture("vid1.mp4")

while True:
    isTrue, frame = video.read()
       
    if frame is not None:
        frame_rescaled = rescaleFrame(frame,0.5)
        cv.imshow("Video",frame)
        cv.imshow("Video_rescaled",frame_rescaled)
    else:
        print("The end")
        exit(1)
    
    if cv.waitKey(15) & 0xFF == ord("C"):
        break

video.release()
cv.destroyAllWindows()
cv.waitKey(0)