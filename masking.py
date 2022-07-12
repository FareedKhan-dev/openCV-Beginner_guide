import cv2 as cv
import numpy as np

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")

blank = np.zeros(my_image.shape[:2], dtype='uint8')

mask = cv.circle(blank, (my_image.shape[1]//3, my_image.shape[0]//3), 100, 255, -1)

masked = cv.bitwise_and(my_image, my_image, mask=mask)

cv.imshow('Masked', masked) 

cv.waitKey(0)