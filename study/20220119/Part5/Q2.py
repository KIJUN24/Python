class MaxLimitCalculator:
    def __init__(self):
        self.value = 0


    def add(self, val):
        self.value += val
        if(self.value > 100):
            print(100)
        else:
            print(self.value)

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)