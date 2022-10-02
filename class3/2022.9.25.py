'''
class Cars:#創立類別
    pass
audi=Cars()#創立物件
'''
'''
class Cars:
    pass
class Motorcycle:
    pass
audi=Cars()
print(isinstance(audi,Cars))#判斷類別和物件的關系
print(isinstance(audi,Motorcycle))
'''
'''
class Cars:
    pass
audi=Cars()
#建立屬性
audi.color='blue'
audi.seats=4
#呼叫屬性
print(audi.color)
'''
'''
class Cars:
    #建構式
    def __init__(self, color, seat):
        self.color=color
        self.seat=seat
        #方法
    def move(self,meter):
        print('my car moves'+str(meter)+'meter')
audi=Cars('blue',4)
audi.move(5) #呼叫方法
'''
'''
class Cars:
    #建構式
    def __init__(self, color, seat):
        self.color=color
        self.seat=seat
        #方法
    def printAttribute(self):
        print('My car color is'+str(self.color))
        print('My car has'+str(self.seat),'seats')
audi=Cars('blue',4)
audi.printAttribute()
'''


class FullName:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printMyName(self):
        print('My name is',self.firstname+','+self.lastname )
        
name1=FullName('Andy','Wang')
name2=FullName('Lulu','Cheng')
name1.printMyName()
name2.printMyName()

