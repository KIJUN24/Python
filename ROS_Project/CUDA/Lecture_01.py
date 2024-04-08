import cupy as cp
import numpy as np

# x_host = np.array([1, 2, 3])
# print(type(x_host))

# x_device = cp.array([1, 2, 3])
# print(type(x_device))

# np.linalg.norm(x_host)
# cp.linalg.norm(x_device)

# 간단한 배열의 계산에서는 CPU가 더 빠르다.


with cp.cuda.Device(0):
    x_on_device_0 = cp.array([1, 2, 3, 4, 5])



x_host = np.random.randint(0, 255, (2000, 2000))
# 2,000 X 2,000 배열을 CPU로 만듦
x_device = cp.asarray(x_host)
# 같은 배열을 만드는 데 CUP를 사용하는 것보다 GPU를 사용하는 것이 더 빠르다.

x_host_1 = x_device.get()
# 값을 다시 가져올 수 있다

from scipy.fft import fftn

# fftn(x_host)

import cupyx

cupyx.scipy.fft.fftn(x_device)