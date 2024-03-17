import cv2
import numpy as np

imgpath = 'D:\\Programing\\Python_Workspace\\Carmera\\Roi\\LineImage2.jpg'
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
img = cv2.rectangle(img, (450,180), (600,280), (0,255,0), 3)

print(len(img), len(img[0]))

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()