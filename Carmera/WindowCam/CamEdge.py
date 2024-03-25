import cv2
import numpy as np

capture = cv2.VideoCapture(1)

while True:
    ret, frame = capture.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur_gray = cv2.GaussianBlur(gray, (5,5), 0)
        edge = cv2.Canny(np.uint8(blur_gray), 60, 70)

        cv2.imshow("original", frame)
        cv2.imshow("gray", gray)
        cv2.imshow("blur", blur_gray)
        cv2.imshow("canny", edge)
        

        if cv2.waitKey(1) > 0:
            break

capture.release()
cv2.destroyAllWindows()