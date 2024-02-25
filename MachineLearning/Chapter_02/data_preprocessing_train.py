# P.102

import SklearnSetDiv as sd
import data_preprocessing as dpp
import matplotlib.pyplot as plt
import numpy as np

plt.scatter(dpp.train_scaled[:,0], dpp.train_scaled[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

new = ([25, 150] - dpp.mean) / dpp.std
plt.scatter(dpp.train_scaled[:,0], dpp.train_scaled[:,1])
# plt.scatter(new[0], new[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

sd.kn.fit(dpp.train_scaled, sd.train_target)

test_scaled = (sd.test_input - dpp.mean) - dpp.std

print(sd.kn.score(test_scaled, sd.test_target))
print(sd.kn.predict([new]))

distances, indexes = sd.kn.kneighbors([new])
plt.scatter(dpp.train_scaled[:,0], dpp.train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(dpp.train_scaled[indexes,0], dpp.train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()