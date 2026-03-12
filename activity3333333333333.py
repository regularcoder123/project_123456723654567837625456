#ENCAPSULATIONNNNNNNN
class square:
    def __init__(self):
        self.__side = 10
    def area(self):
        print("Side Length:",self.__side)
        print("Area:",self.__side**2)

obsquare = square()
obsquare.area()
