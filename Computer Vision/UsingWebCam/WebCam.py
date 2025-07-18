import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()

    cv.imshow('frame',frame)

    if cv.waitKey(5) == ord('x'):
        break
camera.release()
cv.destroyAllWindows()