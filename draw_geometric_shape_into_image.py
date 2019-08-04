import cv2
import numpy as np

img = cv2.imread('lena.jpg',1)

img = cv2.line(img, (0,0), (255,255), (0,0,255), 10)  
img = cv2.arrowedLine(img, (0,0), (255,400), (0,0,255), 10)
img = cv2.rectangle(img, (400,400), (500,450), (0,255,0), 10)  
img = cv2.circle(img, (300,300),60,(255,0,0), 10)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'Lena',(10,500), font, 4, (255,255,255), 5, cv2.LINE_AA)

print(img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()