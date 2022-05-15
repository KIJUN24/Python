import pygame
from path import *



ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3에 해당하는 값

balls = []

balls.append({
    "pos_x" : 50,   # 공의 x좌표
    "pos_y" : 50,   # 공의 y좌표
    "img_idx" : 0,  # 공의 이미지 인덕스
    "to_x" : 3,     # x축 이동방향, -3이면 왼쪽으로, 3이면 오른쪽으로
    "to_y" : -6,    # y축 이동방향
    "init_spd_y" : ball_speed_y[0]  # y최초 속도
    })

ball_to_remove = -1
