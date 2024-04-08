import cv2

# 1번 포트에 연결되어 있는 카메라 연결
capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()

    dst = frame[100:200, 200:300]
    

    cv2.imshow("VideoRoi", frame)
    cv2.imshow("VideoRoi", dst)

capture.release()
cv2.destroyAllWindows()