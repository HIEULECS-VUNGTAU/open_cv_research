import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)
# time.sleep()

background = 0

for i in range(30):
    ret, background = cap.read()

# Laterally invert the image / flip the image.
background = np.flip(background, 1)

# Capturing the live frame
ret, img = cap.read()

# Laterally invert the image / flip the image
img = np.flip(img, 1)

# converting from BGR to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Range for lower red
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask1 = cv.inRange(hsv, lower_red, upper_red)

# Range for upper range
lower_red = np.array([170, 120, 70])
upper_red = np.array([180, 255, 255])
mask2 = cv.inRange(hsv, lower_red, upper_red)

# Generating the final mask to detect red color
mask = mask1 + mask2

mask1 = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3, 3), np.uint8))
mask1 = cv.morphologyEx(mask, cv.MORPH_DILATE, np.ones((3, 3), np.uint8))

# creating an inverted mask to segment out the cloth from the frame
mask2 = cv.bitwise_not(mask1)

# Segmenting the cloth out of the frame using bitwise and with the inverted mask
res1 = cv.bitwise_and(img, img, mask, mask2)
# creating image showing static background frame pixels only for the masked region
res2 = cv.bitwise_and(background, background, mask, mask1)

# Generating the final output
final_output = cv.addWeighted(res1, 1, res2, 1, 0)
cv.imshow("magic", final_output)
cv.waitKey(0)
cv.destroyAllWindows()