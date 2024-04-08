import cv2

def Cap_Video():
    cap1 = cv2.VideoCapture(0)
    if not cap1.isOpened():
        print("Failed to open Cam1")
        return
    
    cap2 = cv2.VideoCapture(1)
    if not cap2.isOpened():
        print("Filed to open cam2")
        return
    
    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("Failed to cap frame")
            break

        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        cv2.imshow("cam1 gray", gray1)
        cv2.imshow("cam2 gray", gray2)

        if cv2.waitKey(1) > 0:
            break

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    Cap_Video()