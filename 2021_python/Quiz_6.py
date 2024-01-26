# 함수 : std_weight
# 전달 : 키(height), 성별(gender)

# def std_weight(height, gender):
#     if gender == "여자":
#         std_weight = height * height * 21
#         print("키 : {0}cm\t성별 : {1}".format(height*100, gender), end = " ")
#         return std_weight
#     else:
#         std_weight = height * height * 22
#         print("키 : {0}cm\t성별 : {1}".format(height*100, gender), end = " ")
#         return std_weight

# print(std_weight(1.72, "남자"))
# print(std_weight(1.53, "여자"))
# print(std_weight(1.80, "남자"))


#//////////////////////////////////////////////////////////// 


def std_weight(height, gender): # 키는 m단위(실수), gender "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))