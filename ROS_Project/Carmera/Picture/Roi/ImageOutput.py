import cv2
from ImagePath import *

img = cv2.imread(ImagePath, cv2.IMREAD_COLOR)

# print(img)
cv2.imshow('Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()