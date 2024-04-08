import cv2
imgPath = 'D:\\Programing\\Python_Workspace\\ROS_Project\\Carmera\\Color\\Color.jpg'
img = cv2.imread(imgPath)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)\

cv2.imshow("Origin", img)
cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)

cv2.waitKey(0)
cv2.destroyAllWindows()