import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

pic1 = cv.imread('pic1.jpg') 

gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [180], [0,180]) 
gray_hist = [i[0] for i in gray_hist]

mpl.use('tkagg')
x = np.arange(180)
plt.plot(x,gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

plt.show()


cv.waitKey(0)





