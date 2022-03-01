from random import *

def random_pop(data):
    number = randint(0, len(data)-1)
    return data.pop(number)

if(__name__ == "__main__"):
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))