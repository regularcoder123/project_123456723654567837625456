class square:
    def __init__(self,side):
        self.side = side
    def area(self):
        print("Area of the shape is:",self.side)
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area_circ = 3.14 * self.radius**2
        print("Area of the shape is:",area_circ)

obsquare = square(23)
obcircle = circle(123)
obsquare.area()
obcircle.area()
