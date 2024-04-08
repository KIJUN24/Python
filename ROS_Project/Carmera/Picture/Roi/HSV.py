import cv2
import numpy as np
from ImagePath import *

img = cv2.imread(ImagePath)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,190])
upper_white = np.array([179,255,255])

mask = cv2.inRange(hsv, lower_white, upper_white)

cv2.imshow('원본', img)
cv2.imshow('line', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()