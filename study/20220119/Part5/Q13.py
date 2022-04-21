from random import *

result = []
while(len(result) < 6):
    i = randint(1, 45)
    if i not in result:
        result.append(i)


print(result)