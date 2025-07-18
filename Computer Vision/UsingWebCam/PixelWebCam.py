import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()

    cv.imshow('frame',frame)

    laplacian = cv.Laplacian(frame, cv.CV_8U)
    laplacian = cv.convertScaleAbs(laplacian)
    cv.imshow('laplacian',laplacian)

    edges = cv.Canny(laplacian, 100, 100)
    cv.imshow('edges',edges)

    if cv.waitKey(5) == ord('x'):
        break
camera.release()
cv.destroyAllWindows()