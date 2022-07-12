import cv2 as cv

def rescaleFrame(frame, scale=0.25):
    # images, Videos, Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):

    capture.set(3,width)
    capture.set(4,height)



# Reading Videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame)

    cv.imshow('resized Video', resized_frame)


    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()