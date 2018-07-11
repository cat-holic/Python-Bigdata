class Caculator:
    def __init__(self,num):
        self.num = num

    def sum(self):
        print(sum(self.num))
    def avg(self):
        print(sum(self.num)/len(self.num))


cal1= Caculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Caculator([6,7,8,9,10])
cal2.sum()
cal2.avg()