import cv2

def Capture_Video():
    # 첫 번째 카메라
    cap1 = cv2.VideoCapture(0)
    if not cap1.isOpened():
        print("Failed to open camera 1")
        return
    
    # 두 번째 카메라
    cap2 = cv2.VideoCapture(1)
    if not cap2.isOpened():
        print("Failed to open camera 2")
        return
    

    while True:
        # 카메라에서 프레임 읽기
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("Failed to capture frame")
            break

        # 영상 처리 작업
        #...

        # 프레임 출력
        cv2.imshow("CAM1", frame1)
        cv2.imshow("CAM2", frame2)

        # 종료 키
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # 카메라 헤제
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()


# 메인 함수 실행
if __name__ == "__main__":
    Capture_Video()