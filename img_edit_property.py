import numpy as np
import cv2

img = cv2.imread('messi5.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))
img1 = cv2.imread('opencv-logo.png')

# cv2.imshow('r', r)
# cv2.imshow('b', b)
# cv2.imshow('g', g)

img = cv2.resize(img, (512, 512))
img1 = cv2.resize(img1, (512, 512))

# dst = cv2.add(img, img1)
dst = cv2.addWeighted(img, .5, img1, .5, 0) 

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()