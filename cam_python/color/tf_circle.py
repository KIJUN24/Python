import cv2
import numpy as np

img = cv2.imread('baduk1.jpg', cv2.IMREAD_GRAYSCALE)
# img 변수선언('baduk1.jpg'사진을 Grayscale로 읽음.)

img = cv2.medianBlur(img, 5)
# 사진을 부드럽게 해줌.
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# 색상을 바꿔줌 -> GRAY에서 BGR

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,
                1, # 이미지와 동일한 해상도로 처리
                20, # 원과 원 사이의  거리
                param1 = 50, # Canny Edge 함수의 상위 임계값 지정
                param2 = 25, # 값이 작으면 더 많은 원이 검출
                minRadius = 0, # 이것보다 작은 원은 검출하지 않는다.
                maxRadius = 0) # 이것보다 큰 원은 검출하지 않는다.
# img : 처리할 이미지 / cv2.HOUGH_GRADIENT : 검출방법
# 1 : 해상도 비율 / 20 : 최소 거리
# param1 : Canny Edge 임계값 / param2 : 중심 임계값
# minRadius : 최소 반지름 / maxRadius : 최대 반지름

circles = np.uint16(np.around(circles))
# 2^16개수 만큼 표현 가능 --> 16픽셀
# 반올림처리

for i in circles[0,:]:  # 검출된 원을 이미지에 그리기
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
# 원 그리기
# i[0], i[1] : 원의 중심좌표 (x, y)
# i[2] : 원의 반지름

cv2.imshow('img', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()