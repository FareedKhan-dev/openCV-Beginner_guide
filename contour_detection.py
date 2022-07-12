from tokenize import blank_re
import cv2 as cv
import numpy as np

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")


blur = cv.GaussianBlur(my_image,(5, 5), cv.BORDER_DEFAULT)
gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat', gray)

# from canny finding counteirs
canny = cv.Canny(blur, 50, 50)
cv.imshow('Cat', canny)
cantours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(cantours))


# from threshold
# ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
# cantours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(len(cantours))



# Drawing contours that are found
blank = np.zeros(my_image.shape, dtype='uint8')
cv.imshow('blank', blank)

cv.drawContours(blank, cantours, -1, (0,0,255), thickness=1)
cv.imshow('Countours run', blank)

# cv.imshow('thresh', thresh)

cv.waitKey(0)