# 과대적합을 줄 일 수 있는 법 : 규제
# 가중치(기울기)를 작게 만든다.

from sklearn.preprocessing import StandardScaler
from MultipeRegression_Train import *

ss = StandardScaler()
ss.fit(train_poly)

train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)
