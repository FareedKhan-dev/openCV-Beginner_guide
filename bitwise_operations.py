import cv2 as cv
from cv2 import bitwise_and
import numpy as np


blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)


circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# Bitwise and operator
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_end', bitwise_and)

# Bitwise pr operator
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

# Bitwise xor  without intersect operator
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

# Bitwise pr operator
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise_not', bitwise_not)


cv.waitKey(0)