letter = ['A', 'B', 'C', 'D', 'E', 'F']
print(letter[0])
print(letter[1])
print(letter[-1])
print(letter[-6])



# 슬라이싱 중요
# 라이다 결과 값을 출력할 때 슬라이싱을 하면 편하게 값을 확인할 수 있다.
# 파마리터[180:][1:180]
print(letter[0:3])



# 배열의 범위를 지정할 때 인텍스를 생략할 수 있다.
print("letter[:3] = %s" % (letter[:3]))
print("letter[3:] = %s" % (letter[3:]))
print("letter[:] = {}".format(letter[:]))