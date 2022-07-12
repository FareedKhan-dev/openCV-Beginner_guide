import cv2 as cv

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")

gray = cv.cvtColor(my_image, cv.COLOR_BGR2GRAY)


# Simple thresholding
threshold, thresh = cv.threshold(gray, 100, 225, cv.THRESH_BINARY)

# inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 100, 225, cv.THRESH_BINARY_INV)

# Adapted thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)

cv.imshow('Cat', thresh)
cv.imshow('Cat2', thresh_inv)
cv.imshow('Cat3', adaptive_thresh)



cv.waitKey(0)