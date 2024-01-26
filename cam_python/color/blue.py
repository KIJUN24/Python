import cv2

img_color = cv2.imread('RGB_text.png')
height, width = img_color.shape[:2]
# img_color에서 높이와 너비 값을 가져옴

img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

lower_blue = (120-10, 30, 30)
# 30 : 너무 어두워서 검은색에 가까운 값과 너무 밝아 흰색에 가까운 색은 제외
upper_blue = (120+10, 255, 255)
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
# 범위 내에 있는 색들은 흰색이 됨. 나머지 검은색.

img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask)
# 원본 이미지에서 범위 내에 있는 부분을 획득.

cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destoryAllwindows()