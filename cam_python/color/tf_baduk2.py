import cv2
import numpy as np

img = cv2.imread('baduk2.jpg', cv2.IMREAD_GRAYSCALE)

img = cv2.medianBlur(img, 1)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,
                1, 
                20,
                param1 = 200,
                param2 = 20,
                minRadius = 0,
                maxRadius = 15)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('img', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()