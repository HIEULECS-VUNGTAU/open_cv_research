import numpy as np
import cv2
# import matplotlib

img = cv2.imread('data/gradient.png', 0)
img2 = cv2.imread('data/sudoku.png', 0)
_, th1 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)
th3 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)

cv2.imshow('res', img2)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()