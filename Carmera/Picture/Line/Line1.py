import cv2

imgpath = 'D:\\Programing\\Python_Workspace\\Carmera\\Line\\LineImage2.jpg'
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)

# print(img)
cv2.imshow('Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()