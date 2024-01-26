import random
import time

algha_max = 10
p1 = 0

while True:
    time.sleep(1)
    p1 += random.randrange(-algha_max, algha_max)
    print(p1)