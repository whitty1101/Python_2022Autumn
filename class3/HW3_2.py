class computer:
    def __init__(self, kinds, color):
        self.kinds=kinds
        self.color=color
    def printComputer(self):
        print('The computer is a' +str(self.kinds)'and it is in' +str(self.color) )
mac=computer('laptop', 'black')
mac.printComputer