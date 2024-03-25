import cv2
import numpy as np

capture = cv2.VideoCapture(1)



while True:
    ret, frame = capture.read()

    

    if ret:
        cv2.imshow('frame', frame)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        lower_white = np.array([0,0,150])
        upper_white = np.array([179, 255, 255])
        
        mask = cv2.inRange(hsv, lower_white, upper_white)

        cv2.imshow('mask', mask)        
        cv2.imshow('gray', gray)

        if cv2.waitKey(1) > 0:
            break

capture.release()
cv2.destroyAllWindows()