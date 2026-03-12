class Computer:
    def __init__(self):
        self.__maxprice =676767676767776767676776767641414144141441141411141441414141414144141414414141414141441414414676767676767676767676767676767677676767
    
    def sell(self):
        print(f"Selling Price: {self.__maxprice}")
    def setMAXPRICE(self,price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 676767677676
c.sell()

c.setMAXPRICE(2345678923456723456345)
c.sell()