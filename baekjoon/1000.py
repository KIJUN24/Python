# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 예제 입력
# 1 2 
# 예제 출력
# 3


a, b = map(int, input().split())
if(0<a and b<10):
    print(a+b)