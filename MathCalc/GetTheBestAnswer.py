
import copy

class GetAnswer:
    minValue = 0
    maxValue = 0
    currentName = 212
    resultString = ""

    def GetTestResult(self):
        return GetAnswer.currentName

    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue
        pass

    def GetAll(self):

        for currentValue in range(self.minValue, self.maxValue):
            self.resultString += self.GetSingle(currentValue)
        return self.resultString
    # 满足条件的数字集合
    def GetSingle(self, firstValue):
        if not (self.minValue < firstValue < self.maxValue):
            return ""
        for i in range(self.minValue, self.maxValue):
            if firstValue - i == 2:
                return "%d,%d" % (firstValue, i) + "\r\n"
        return ""

    def GetInitAnswer(self,firstValue):
        rangValue = set(range(1,9))
        li=list(rangValue)
        li2 = copy.copy(li)
        li.remove(firstValue)
        print('2')
        print(li2,type(li2))
        print('1')
        print(li,type(li))
        pass

#TODO 添加
    def AdditionCheck(self,checkedValue1,checkedValue2,targetValue):
        return checkedValue1 + checkedValue2 == targetValue
    def SubtractionCheck(self,checkedValue1,checkedValue2,targetValue):
        return checkedValue1 - checkedValue2 == targetValue

