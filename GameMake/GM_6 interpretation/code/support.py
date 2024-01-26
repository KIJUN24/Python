# image : https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=2531s
from os import walk         # os로부터 walk만 가져옴. -> for문으로 탐색할 수 있게끔 하기 위해 가져옴.
import pygame

def import_folder(path):        # 이 함수를 사용하려면 path의 정보가 있어야 사용 가능함.
    surface_list = []           # surface_list를 정의하고 (dir)빈 공간으로 놔둠.

    for _,__,img_files in walk(path):       # 필요한 정보만 추출하려고 3번째 img_files만 가져옴. --> path아래에 있는 파일들을 가져옴.
        for image in img_files:
            full_path = path + '\\' + image     # path아래에 있는 파일 + '\\' + 이미지 (~.png) = 사용할 이미지 주소
            # full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()   # 이미지 불러오기
            surface_list.append(image_surf)     # 이미지를 빈 dir공간에 넣기

    return surface_list     #surface_list 값을 사용하기 위해 반환






#     for information in walk(path):
#         print(information)

# import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_6\\graphics\\character\\run')
