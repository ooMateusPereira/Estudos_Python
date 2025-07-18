import cv2 as cv

video = cv.VideoCapture('people.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(250, 150)

while True:

    ret, frame = video.read()

    if ret:
        maks = subtractor.apply(frame)
        cv.imshow('frame',maks)

        if cv.waitKey(1) & 0xFF == ord('x'):
            break
    else:
        video = cv.VideoCapture('people.mp4')

cv.destroyAllWindows()
video.release()