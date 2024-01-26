# # 오류 처리
# 4 / 0

# a = [1,2,3]
# a[4]

# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)


# try:
#     a = [1,2,3]
#     a[4]
# except IndexError as e:
#     print(e)



# # 여러 개의 오류 처리
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱할 수 없습니다.")



# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)



# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)



# try:
#     f = open("나 없는 파일", 'r')
# except FileNotFoundError:
#     pass



class Bird:
    def fly(self):
        raise NotImplementedError



# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()


class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()