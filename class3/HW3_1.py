class People:
    def __init__(self,height,weight,age):
        self.height=height
        self.weight=weight
        self.age=age
    def printAttribute(self):
        print(self.height,self.weight,self.age)


mom=People('163','45','18')
dad=People('179','70','???')
me=People('161','44','13')
mom.printAttribute()
dad.printAttribute()
me.printAttribute()

