from openDemo import Calculator

class ChildImp(Calculator):

    def __init__(self):
        Calculator.__init__(self,2,8)

    num2=200
    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


c=ChildImp()
print(c.getCompleteData())
c1=ChildImp()
print(c.getCompleteData())