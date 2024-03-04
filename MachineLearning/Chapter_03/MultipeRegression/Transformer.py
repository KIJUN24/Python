from Perch_data import *
from DataFrame_Pandas import *
from sklearn.preprocessing import PolynomialFeatures

# degree(제곱항을 만들어줌)(PolynomialReatures의 매개변수) = 2(기본값)
poly = PolynomialFeatures()
poly.fit([[2,3]])
# print(poly.transform([[2,3]]))

poly = PolynomialFeatures(include_bias=False)
# 1의 값을 빼기 위해 False를 해준다.
poly.fit([[2,3]])
# print(poly.transform([[2,3]]))

poly = PolynomialFeatures(include_bias=False)
poly.fit(trian_input)
train_poly = poly.transform(trian_input)
# print(train_poly.shape)
# 결과값 : (42, 9) : 42개의 샘플과 9개의 특성이 있음.
# print(poly.get_feature_names_out())

test_poly = poly.transform(test_input)