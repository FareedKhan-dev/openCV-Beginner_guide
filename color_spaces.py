import cv2 as cv

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")


# BGR to greyscale
gray = cv.cvtColor(my_image, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat', gray)
# BGR to HSV
hsv = cv.cvtColor(my_image, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)
# BGR to L*a*b
lab = cv.cvtColor(my_image, cv.COLOR_BGR2Lab)
# cv.imshow('lab', lab)


import matplotlib.pyplot as plt
# show rgb not bgr
plt.imshow(my_image)
# plt.show()

# BGR to RGB
# same as matplotlib default
rgb = cv.cvtColor(my_image, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

cv.waitKey(0)