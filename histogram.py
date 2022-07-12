from turtle import color
import cv2 as cv
import matplotlib.pyplot as plt

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/da.jpeg")

gray = cv.cvtColor(my_image, cv.COLOR_BGR2GRAY)

cv.imshow('Cat', gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure('Histogram of grayscale')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.plot(gray_hist)
plt.show()

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([my_image], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)