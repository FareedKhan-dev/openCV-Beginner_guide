from turtle import width
import cv2 as cv

# # Reading Images
# my_image = cv.imread("introduction_photoes videos/images/pexels-george-desipris-792381.jpg")


def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# resized_image = rescaleFrame(my_image)
# cv.imshow('old', my_image)
# cv.imshow('Cat', resized_image)

# cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture("introduction_photoes videos/videos/production ID_4781762.mp4")

while True:
    isTrue, frame = capture.read()

    resized_video = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('resized Video', resized_video)


    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()