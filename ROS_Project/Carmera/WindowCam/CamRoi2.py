import cv2

capture = cv2.VideoCapture(1)

while True:
    ret, frame = capture.read()

    if ret:
        cv2.imshow("frame", frame)
        # cv2.imshow("Roi", frame[100:300, 200:400])
        if cv2.waitKey(1) > 0:
            break

capture.release()
cv2.destroyAllWindows()