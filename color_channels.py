import cv2 as cv
import numpy as np

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")


# Split image into rgb color
b,g,r = cv.split(my_image)

# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red',  r)

print(my_image.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge color channels
merged = cv.merge([b,g,r])
# cv.imshow('merged',  merged)


# blank image
blank = np.zeros(my_image.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('blue',  blue)
cv.imshow('green',  green)
cv.imshow('red',  red)



cv.waitKey(0)