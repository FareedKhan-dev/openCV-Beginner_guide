import cv2 as cv

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")


# averaging
average = cv.blur(my_image, (5,5))
# cv.imshow('Cat1', average)


# Gaussian Blur (Weighted blur) less blur than average
gaussian = cv.GaussianBlur(my_image, (5,5), 0)
# cv.imshow('Cat', gaussian)


# Medium Blur finds median
median_blur = cv.medianBlur(my_image, 5)
cv.imshow('Cat3', median_blur)

# bilateral Blur most effective bluring but retains edges
bilateral = cv.bilateralFilter(my_image, 10, 35, 25)
cv.imshow('Cat4', bilateral)

cv.waitKey(0)