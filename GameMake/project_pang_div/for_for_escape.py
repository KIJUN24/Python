balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print("ball : ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapon : ", weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print('공과 무기가 충돌')
            break
    else:   # for문도 else을 사용할 수 있다.
        continue
    print("바깥 for 문 break")
    break
