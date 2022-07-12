from turtle import width
import cv2 as cv
from cv2 import rotate
import numpy as np

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")


# Translation (moving image)
def translate(img, x, y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimesnsion = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimesnsion)

translated = translate(my_image, -100, 200)
# cv.imshow('Cat', translated) 

# Rotation image
def rotating(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimesnsion = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, rotMat, dimesnsion)
rotated = rotating(my_image, 90)

# cv.imshow('Cat', rotated) 

# Resizing image
resized = cv.resize(my_image, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Cat', resized)


# Flipping an image
flipped = cv.flip(my_image, 1)
# cv.imshow('Cat', flipped)

# crop an image
cropped = my_image[200:400,:]
cv.imshow('Cat', cropped)


cv.waitKey(0)