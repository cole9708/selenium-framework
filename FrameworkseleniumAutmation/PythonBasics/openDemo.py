class Calculator:
    num = 100 #class variable

    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print('object created')

    def getData(selfs):
        print('i am executing method in class')

    def summation(self):
        return self.firstNumber + self.secondNumber


obj = Calculator(2,3)
obj1= Calculator(4,5)
obj2 = Calculator(4,9)
print(obj.summation())
print(obj1.summation())
print(obj2.summation())
obj.getData()
print(obj.num)

