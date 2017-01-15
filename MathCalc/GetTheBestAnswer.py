

class GetAnswer:
    minValue = 0
    maxValue = 0
    currentName = 212
    resultString = ""
    def GetTestResult(self):

        return GetAnswer.currentName
    def __init__(self,minValue,maxValue):
        self.minValue = minValue
        self.maxValue = maxValue
        pass
    def GetAll(self):

        for currentValue in range(self.minValue,self.maxValue):
            self.resultString += self.GetSingle(currentValue)
        return self.resultString


    def GetSingle(self,firstValue):
        if not ( self.minValue < firstValue < self.maxValue):
            return ""
        for i in range(self.minValue,self.maxValue):
            if firstValue - i == 2:
                return "%d,%d"%(firstValue,i) +"\r\n"
        return ""
