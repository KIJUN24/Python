import cv2

ImgPath = 'D:\\Programing\\Python_Workspace\\Carmera\\Roi\\LineImage2.jpg'
img = cv2.imread(ImgPath, cv2.IMREAD_COLOR)

print(img.shape)
# (img, (450,180), (600,280), (0,255,0), 3)
cv2.imshow('원본', img)
cv2.imshow('ROI Cut', img[180:280, 450:600])
cv2.waitKey(0)
cv2.destroyAllWindows()