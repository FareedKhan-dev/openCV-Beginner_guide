import cv2 as cv

# Reading Images
my_image = cv.imread("introduction_photoes videos/images/pexels-george-desipris-792381.jpg")
cv.imshow('Cat', my_image)


# Reading Videos

# Webcam or camera connected to laptop
# capture = cv.VideoCapture(0)

capture = cv.VideoCapture("introduction_photoes/ videos/production ID_4781762.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()