# 가중치의 절댓값을 벌칙으로 준다.
# L1규제

from sklearn.linear_model import Lasso
import Regularization as re
from Ridge import *

lasso = Lasso()
lasso.fit(re.train_scaled, train_target)

print(lasso.score(re.train_scaled, train_target))
print(lasso.score(re.test_scaled, test_target))

train_score_lasso = []
test_score_lasso = []
alpha_list_lasso = [0.001, 0.01, 0.1, 1, 10, 100]

for alpha in alpha_list_lasso:
    lasso = Lasso(alpha=alpha)
    lasso.fit(re.train_scaled, train_target)
    train_score_lasso.append(lasso.score(re.train_scaled, train_target))
    test_score_lasso.append(lasso.score(re.test_scaled, test_target))


import matplotlib.pyplot as plt

plt.plot(np.log10(alpha_list_lasso), train_score_lasso)
plt.plot(np.log10(alpha_list_lasso), test_score_lasso)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()