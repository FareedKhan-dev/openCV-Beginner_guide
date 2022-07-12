import cv2 as cv

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/daf.jpg")
# cv.imshow('gray', my_image)



# Converting images to gresycale (intensity distribution)
gray = cv.cvtColor(my_image, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Blur the images (remove noise from image, extra elements)
blur = cv.GaussianBlur(my_image, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Cat', blur)

# Edge cascade ( to find edges of images)
canny = cv.Canny(blur, 60, 105)
# blur_images to reduce edges
# cv.imshow('canny', canny)

# dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
# cv.imshow('dilated', dilated)

# Eroding this diluted image
eroded = cv.erode(dilated,  (3,3), iterations=3)
# cv.imshow('eroded', eroded)

# Resize and crop an image
resized = cv.resize(my_image, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

# Crop image
croped = my_image[50:200, 200:400]
cv.imshow('croped', croped)


cv.waitKey(0)