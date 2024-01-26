import cv2 as cv
import numpy as np


hsv = 0
lower_blue1 = 0
upper_bule1 = 0
lower_blue2 = 0
upper_bule2 = 0
lower_blue3 = 0
upper_bule3 = 0


def nothing(x):
    pass


def mouse_callback(event, x, y, flags, param):
    global hsv, lower_blue1, upper_bule1, lower_blue2, upper_bule2, lower_blue3, upper_bule3, threshold

    # 마우스 왼쪽 버튼 누를 시 위치에 있는 픽셀값을 읽어와서 HSV로 변환합니다.
    if event == cv.EVENT_LBUTTONDOWN:
        print(img_color[y, x])
        color = img_color[y, x]

        one_pixel = np.uint8([[color]])
        hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)
        hsv = hsv[0][0]

        threshold = cv.getTrackvarPos('threshold', 'img_result')

        # HSV 색공간에서 마우스 클릭으로 얻은 픽셀값과 유사한 픽셀값의 범위를 정합니다.
        if hsv[0] < 10:
            print("case1")
            lower_blue1 = np.array([hsv[0]-10+180, threshold, threshold])
            upper_bule1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, threshold, threshold])
            upper_bule2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0], threshold, threshold])
            upper_bule3 = np.array([hsv[0]+10, 255, 255])

        elif hsv[0] > 170:
            print("case2")
            lower_blue1 = np.array([hsv[0], threshold, threshold])
            upper_bule1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, threshold, threshold])
            upper_bule2 = np.array([hsv[0]+10, 255, 255])
            lower_blue3 = np.array([hsv[0]-10, threshold, threshold])
            upper_bule3 = np.array([hsv[0], 255, 255])


        else:
            print("case3")
            lower_blue1 = np.array([hsv[0], threshold, threshold])
            upper_bule1 = np.array([hsv[0]+10, 255, 255])
            lower_blue2 = np.array([hsv[0]-10, threshold, threshold])
            upper_bule2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0]-10, threshold, threshold])
            upper_bule3 = np.array([hsv[0], 255, 255])

        
        print(hsv[0])
        print("@1", lower_blue1, "~", upper_bule1)
        print("@1", lower_blue2, "~", upper_bule2)
        print("@1", lower_blue3, "~", upper_bule3)


cv.namedWindow('img_color')
cv.setMouseCallback('img_color', mouse_callback)

cv.namedWindow('img_result')
cv.createTrackbar('threshold', 'img_result', 0, 255, nothing)
# 트랙바 : 0~255 범위. S와 V 값 수정.
cv.setTrackbarPos('threshold', 'img_result', 30)
cap = cv.VideoCapture(0)


while(True):
    # img_color = cv.imread('2.jpg')
    ret, img_color = cap.read()
    height, width = img_color.shape[:2]
    img_color = cv.resize(img_color, (width, height), interpolation = cv.INTER_AREA)

    # 원본 영상을 HSV 영상으로 변환합니다.
    img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

    # 범위 값으로 HSV 이미지에서 마스크를 생성합니다.
    img_mask1 = cv.inRange(img_hsv, lower_blue1, upper_bule1)
    img_mask2 = cv.inRange(img_hsv, lower_blue2, upper_bule2)
    img_mask3 = cv.inRange(img_hsv, lower_blue3, upper_bule3)
    img_mask = img_mask1 | img_mask2 | img_mask3

    kernel = np.ones((11, 11), np.unit8)
    img_mask = cv.morphologyEx(img_mask, cv.MORPH_OPEN, kernel)
    img_mask = cv.morphologyEx(img_mask, cv.MORPH_CLOSE, kernel)


    # 마스크 이미지로 원본 이미지에서 범위 값에 해당되는 영상 부분을 획득한다.
    img_result = cv.bitwise_and(img_color, img_color, mask = img_mask)

    numOfLabels, img_label, stats, centroids = cv.connectedComponentsWithStats(img_mask)

    for idx, centroid in enumerate(centroids):
        if stats[idx][0] == 0 and stats[idx][1] == 0:
            continue

        if np.any(np.isnan(centroid)):
            continue

        x, y, width, height, area = stats[idx]
        centerX, centerY = int(centroid[0]), int(centroid[1])

        if area > 50:
            cv.circle(img_color, (centerX, centerY), 10, (0, 0, 255), 10)
            cv.rectangle(img_color, (x, y), (x+width, y+height), (0, 0, 255))

    cv.imshow('img_color', img_color)
    cv.imshow('img_mask', img_mask)
    cv.imshow('img_result', img_result)

    # ESC 키 누르면 종료
    if cv.waitKey(1) & 0xFF == 27:
        break


cv.destroyAllWindows()