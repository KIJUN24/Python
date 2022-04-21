# test_list = ['one','two','three']
# for i in test_list:
#     print(i)


# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first + last)
#     print(first - last)
#     print(first * last)
#     print(first / last)


# # marks1.py
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if(mark >= 60):
#         {
#             print("{0}번 학생은 합격입니다.".format(number))
#         }
#     else:
#         print("{0}번 학생은 불합격입니다.".format(number))



# # marks2.py
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if(mark < 60):
#         continue
#     print("{0}번 학생은 합격입니다.".format(number))




# for__range
'''
a = range(10)
print(a)

b = range(1, 11)
print(b)
'''
# add = 0
# for i in range(1, 11):
#     add = add + i
#     print(add)



# # marks3.py
# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if(marks[number] < 60):
#         continue
#     print("{0}번 학생 축하합니다.".format(number + 1))




# # 1~100더하기
# add = 0
# n_ranges = range(1, 101)

# for i in n_ranges:
#     add = add + i
#     print(add)



# # 구구단
# for i in range(2, 10):
#     for j in range(1, 11):
#         print(i*j, end = " ")
#     print('')




# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num*3)
# print(result)



# a = [1, 2, 3, 4]
# result = [num * 3 for num in a]
# print(result)



# a = [1, 2, 3, 4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)



result = [x*y for x in range(2, 10) \
    for y in range(1, 10)]
print(result)