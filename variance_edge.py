from math import comb
import cv2 as cv
import numpy as np

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")

gray = cv.cvtColor(my_image, cv.COLOR_BGR2GRAY)

# Laplacian 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))


# Sabel 
sabelx = cv.Sobel(gray, cv.CV_64F,1 , 0)
sabely = cv.Sobel(gray, cv.CV_64F, 0 ,1)
combined_sabel = cv.bitwise_or(sabelx, sabely)

cv.imshow('SobelX', sabelx)
cv.imshow('SobelY', sabely)
cv.imshow('combined sabel', combined_sabel)


canny = cv.Canny(gray, 150, 175)
cv.imshow('canny ', canny)




cv.waitKey(0)