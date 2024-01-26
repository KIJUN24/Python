#! /usr/bin/env python

# 셔뱅 : 파이썬을 사용하겠다._인터프리팅 정보를 줌.

from email.mime import image        
# email.mime로부터 image 사용
import rospy        
# 노드 작성시 필요(python을 사용할 경우)
import cv2      
#cv2 사용 : openCV
import numpy as np      
# numpy를 사용하는데 np로 축약하여 사용.
from sensor_msgs.msg import Image, CompressedImage      
# senor_msgs.msg(메시지 형태)에 Image, CompressedImage 사용.
from cv_bridge import CvBridge,CvBridgeError        
# cv_bridge에 있는 cvBridege, CvBridgeError 사용.
# CvBridge : ROS와 openCV와 연결해주는 역할(ROS Image와 openCV Image와 Format 다름.)


class camera_sim():     # camera_sim 클래스 생성.

    def __init__(self): 
        rospy.init_node('image_to_receiver', anonymous=False)       
        # node의 이름을 image_to_receiver로 하고 통신은 하나만 하겠다.
        self.pubcam = rospy.Publisher("/pub_image", Image, queue_size=10)       
        # rospy를 사용해 publish 하겠다.(토픽을 보내겠다)     
        # /pub_image 이 토픽으로부터 Image형태로 보내겠다. 
        # (사이즈 queus_size = 10으로 보내겠다.)(메시지 큐 크기)
        # 메시지를 얼마나 가지고 있을지에 관련된 변수 --> 오래된 데이터부터 삭제
        self.subcam = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)        
        # rospy를 사용해 subscribe 하겠다.(토픽을 받겠다)
        # /image_jpeg/compressed 이 토픽으로부터 CompressedImage형태의 메시지를 받겠다.
        # callback 하겠다.
        self.bridge = CvBridge()
        # CvBridge 함수를 가져와 선언.
        rospy.on_shutdown(self.cam_shutdown)
        # rospy.on_shutdown을 사용해 노드를 종료할 수 있음.
        # cam_shutdown callback을 요청해 노드를 종료할 수 있음.
        rospy.spin()        
        # 노드가 셧다운 되기 전까지 종료하지 않게 해줌.
        # 콜백만 처리하다가 죽음.
        # 쓰는 이유 : publish 메시지 큐를 비우는데 사용.

###############################  초기화시켜주는 함수  ###############################


    def callback(self, data):
        # simulation cam -> cv2
        try:
            cv_image = self.bridge.compressed_imgmsg_to_cv2(data)
        except CvBridgeError as e:
            # CvBridgeError : 발생 오류 / e : 오류 메시지 변수
            print("converting error")
            print(e)
            # CvBridgeError가 발생하여 except가 실행 -> 변수 e에 담긴 오류 메시지 출력
        height, width, channel = cv_image.shape
        # shape : 크기
        #print(cv_image.shape)


        # cv2_bgr -> convert color
        cvt_img=cv2.cvtColor(cv_image,cv2.COLOR_RGB2HLS)
        # 사진의 색상변환 -> RGB -> HLS (H : 색상, S : 채도, L : 밝기)
        h, s, v = cv2.split(255-cvt_img)
        # h, s로 색상 조절, v : 밝기 조절
        # split 채널 분리.(색상을 3가지로 분리)
        lower = (0,0,0) 
        # 가장 낮은 값
        upper = (255,255,255)
        # 가장 높은 값
        filtered_img = cv2.inRange(cvt_img, lower, upper)
        # 특정 색상 영역을 추출.
        # cvt_img : 입력 행렬, lower : 하한 값 행렬 또는 스칼라, upper : 상한 값 행렬 또는 스칼라
        img_result = cv2.bitwise_and(cv_image, cv_image, mask = filtered_img)
        # bitwise_and : mask영역에서 서로 공통으로 겹치는 부분 출력
        # (img_result와 region_mask 사진 중 mask영역에서 겹치는 부분 출력)


        # ROI(region of Interest) 
        region = np.array([[(0, height), (0, height*60/100), (width/2, height*40/100),(width, height*60/100), (width, height)]], dtype = np.int32)
        # 범위 설정, type : int형 32채널
        zero_img = np.zeros_like(cv_image)
        # cv_image와 같은 크기의 zeros array를 구하고자 함.
        # zeros array : 0으로 되어있는 array
        region_mask=cv2.fillPoly(zero_img, region, (255,255,255))
        # 다각형 그리기(이미지 파일, 포인트, 색)


        # Covered ROI Mask
        masked_img = cv2.bitwise_and(img_result, region_mask)
        # bitwise_and : mask영역에서 서로 공통으로 겹치는 부분 출력
        # (img_result와 region_mask 사진 중 mask영역에서 겹치는 부분 출력)


        # Warped Image
        src=np.float32([[0,height],[width,height], [width*25/100, height*70/100],[width*75/100, height*70/100]])
        # numpy 데이터 형태 지정(float32 형태)
        dst=np.float32([[width*15/100,height],[width*85/100,height],[width*15/100,0],[width*85/100,0]])
        # numpy 데이터 형태 지정(float32 형태)
        M = cv2.getPerspectiveTransform(src, dst)
        # 사진을 기하학적으로 변환(src : 4개의 원본 좌표, dst : 4개의 결과 좌표)
        Minv = cv2.getPerspectiveTransform(dst, src)
        # src와 dst 자리바꿈.
        warped_img = cv2.warpPerspective(masked_img, M, (width, height))
        # 원근 변환 함수 : 원근 맵 행렬에 대한 기하학적 변환을 수행함.
        # warpPerspective(입력 이미지, 원근법 맵 행렬, 출력 이미지 크기)
        # 입력 이미지에 원근 맵 행렬을 적용하고 출력 이미지 크기로 변형해서 출력 이미지(warped_img)를 반환.


        # Calculate Curved
        try :
            self.pubcam.publish(self.bridge.cv2_to_imgmsg(warped_img,"rgb8"))
            # opencv와 ros에서 사용하는 이미지 포맷이 달라 cv2_to_imgmsg을 통해 변환해줌.
            # pubcom을 publish한다. bridge에 있는 cv2_to_imgmsg을 통해 warped_img을 변환한다.
            # "rgb8" : RGB 8bit
        except CvBridgeError as e:
            # CvBridgeError : 발생 오류 / e : 오류 메시지 변수
            print("publish error")
            print(e)
            # CvBridgeError가 발생하여 except가 실행 -> 변수 e에 담긴 오류 메시지 출력


    def cam_shutdown(self):
        print("I'm dead!")
    # cam_shutdown이라는 함수 정의, I'm dead!를 print함.


if __name__=="__main__":
# 직접 호출 : 기능 수행 / 다른 모듈에서 사용 : 필요한 함수만 사용 가능.
    cs = camera_sim()
    # cs를 camera_sim()으로 선언