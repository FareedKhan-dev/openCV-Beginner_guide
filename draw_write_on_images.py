from tokenize import blank_re
import cv2 as cv
import numpy as np

# Creating a blank image
blank = np.zeros((500,500, 3), dtype='uint8')

# Paint image a certain color
blank[:] = 7, 6, 17

# Paint certain portion of image a certain color
blank[:400] = 255, 0, 0 # Red color


# Draw a rectange
cv.rectangle(blank, (0,0), (350,500), color=(0, 0, 255), thickness=7)

# Draw a rectange with filled
cv.rectangle(blank, (0,0), (250,500), color=(0,255,0), thickness=cv.FILLED)


# Draw a circle
cv.circle(blank, (250,350), 40, color=(255,255,0), thickness=3)

# Draw a circle with filled
cv.circle(blank, (150,350), 40, color=(255,255,0), thickness=-1)

# Draw line
cv.line(blank, (100,0), (250,500), color=(7,6,17), thickness=3)


# Write text on image
cv.putText(blank, 'Hello World!', (225,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (130,255,200), 2)

cv.imshow('Blank', blank)

cv.waitKey(0)