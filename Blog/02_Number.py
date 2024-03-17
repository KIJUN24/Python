# 양수
IntNumber1 = 123
print("양수", IntNumber1)

# 음수
IntNumber2 = -111
print("음수", IntNumber2)

# 0
IntNumber3 = 0
print("영(제로)", IntNumber3)

# 양의(플러스) 소수점
Floating_Point_Number1 = 3.14
print("양의(플러스) 소수점", Floating_Point_Number1)

# 음의(마이너스) 소수점
Floating_Point_Number2 = -3.14
print("음의(마이너스) 소수점", Floating_Point_Number2)


# 2진수를 10진수로 변환하는 프로그램

# 2진수 정의
binary_number = "1010"

# 10진수로 변환
decimal_number = int(binary_number, 2)

# 결과 출력
print("2진수", binary_number, "는 10진수로", decimal_number, "입니다.")



# 8진수를 10진수로 변환하는 프로그램

# 8진수 문자열 정의
octal_number = "52"

# 10진수로 변환
decimal_number = int(octal_number, 8)

# 결과 출력
print("8진수", octal_number, "는 10진수로", decimal_number, "입니다.")



# 16진수를 10진수로 변환하는 프로그램

# 16진수 문자열 정의
hexadecimal_number = "2F"

# 10진수로 변환
decimal_number = int(hexadecimal_number, 16)

# 결과 출력
print("16진수", hexadecimal_number, "는 10진수로", decimal_number, "입니다.")