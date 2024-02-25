# 함수(Function)
# 재사용 가능한 코드 블록을 정의하는 방법.
# 특정 작업을 수행하는 코드를 묶어서 호출할 수 있다.
# 코드 중복을 줄이고 프로그램의 구조를 개선할 수 있다.

# 함수 기초
def add_number(a, b):
    result = a + b
    return result

sum_result = add_number(3, 5)
# print("두 숫자의 합", sum_result)



# f기본값 설정하기, f-string
def greet(name="Guest"):
    print(f"안녕하세요, {name}님!")

# greet()
# greet("John")



# 임의의 개수의 위치 인자 처리하기(가변 인자 개수 처리)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

add_result = sum_all(1,2,3,4)
# print(f"합계 : {add_result}")

add_result = sum_all()
# print(f"합계 : {add_result}")
# 인자(파라미터가 여러 개 있든 아무것도 없든 상관없다.)

# print("\n")

# 임의의 개수의 키워드 인자 처리하기
def print_info1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# print_info1(name="John", age=30, city="New York")

# print("\n")

# 위치, 키워드 인자 동시 출력
def print_info2(*args, **kwargs):
    print("Positional Arguments:")
    for arg in args:
        print(arg)
    
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# print_info2(1, 2, 3, name="John", age=30, city="New York")



# 위 함수들의 특성을 이용하여 평균 계산하기
def calculate_average(*args, **kwargs):
    total = sum(args)

    for key, value in kwargs.items():
        total += value

    count = len(args) + len(kwargs)
    average = total / count
    return average

result = calculate_average(1,2,3, a=4, b=5, c=6)
# print(f"평균 : {result}")



# 제곱한 수를 더하기
def calculate_squared_sum(*args):
    squared_sum = sum(x**2 for x in args)
    return squared_sum

result = calculate_squared_sum(1,2,3,4,5)
print(f"제곱의 합 : {result}")