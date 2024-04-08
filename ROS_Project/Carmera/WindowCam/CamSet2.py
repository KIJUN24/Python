import cv2

capture = cv2.VideoCapture(1)

while True:
    ret, frame = capture.read()

    if ret:
        cv2.imshow("frame", frame)

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', gray)
        
        if cv2.waitKey(1) > 0:
            break

capture.release()
cv2.destroyAllWindows()