import cv2
# cv2(openCV) 사용.(import함)

image = cv2.imread("green.jpg")
# image 변수에 "green.jpg"라는 사진을 읽음.
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# hsv 변수에 image사진의 칼라를 BGR에서 HSV로 변환한다.
h, s, v = cv2.split(hsv)
# hsv(image사진이 칼라가 HSV로 바뀐 사진)을 h, s, v 각각 칼라를 분리함.

cv2.imshow("h", h)
# h(색상)성분의 이미지로 "h"라는 이름으로 사진을 보여줌(출력).
cv2.imshow("s", s)
# s(채도)성분의 이미지로 "s"라는 이름으로 사진을 보여줌(출력).
cv2.imshow("v", v)
# v(명도)성분의 이미지로 "v"라는 이름으로 사진을 보여줌(출력).
cv2.waitKey(0)
# 무한대로 대기

cv2.destroyAllWindows()
# 창을 닫음.

# h : Hue(색상) / s : Saturation(채도) / v : Value(진하기)