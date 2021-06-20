import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


pic1 = cv.imread('pic1.jpg') 
colors = ('r', 'b', 'g')

for i, col in enumerate(colors):
    hist = cv.calcHist([pic1], [i], None, [256], [0,256]) 
    plt.plot(hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('N of pixels')
    axes = plt.gca()
    axes.set_ylim([0,800])


plt.show()
cv.waitKey(0)





