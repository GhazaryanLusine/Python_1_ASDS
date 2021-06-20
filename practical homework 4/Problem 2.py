import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


pic1 = cv.imread('pic1.jpg') 
colors = ('r', 'b', 'g')

for i, col in enumerate(colors):
    hist = cv.calcHist([pic1], [i], None, [220], [0,220]) 
    mpl.use('tkagg') 
    x = np.arange(220)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')


plt.show()
cv.waitKey(0)





