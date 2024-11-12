# Daily Challenge - Circle

import math

class Circle:
    # color = "red"
    
    def __init__(self, radius = None, diameter = None):
        if diameter is not None:
            self.radius = diameter / 2
        elif radius is not None:
            self.radius = radius
        else:
            raise ValueError('Enter radius or diameter')
        self.area = math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    def __str__(self):
       return f'Diameter:{self.diameter} cm,radius {self.radius} cm, area {self.area} cm**2'

    def c_diameter(self):
        return f"Circle's diameter is {self.diameter} cm"

    def circle_area(self):
        return f"Circle's area is {self.area} cm**2"

    def __add__(self, other):
        if isinstance(other,Circle):
            new_radius = self.radius + other.radius
            return Circle(radius=new_radius)
        raise ValueError

    def __gt__(self,other):
        if isinstance(other,Circle):
            return self.radius>other.radius
        return False
    
    def __lt__(self,other):
        if isinstance(other,Circle):
            return self.radius<other.radius
        return False

    def __eq__(self, other):
        if isinstance(other,Circle):
            return self.radius == other.radius
        return False



circle1 = Circle(20)
circle2 = Circle(10)
circle3 = Circle(20)
print(circle1.radius)
print(circle1.circle_area())
print(str(circle1))
circle4 = circle1 + circle2
print(circle3)
print(circle1 == circle2)
print(circle1 == circle3)
print(circle1<circle2)
print(circle2<circle1)
circle_list = [circle1,circle2,circle3,circle4]
sorting = sorted(circle_list)
for crcl in sorting:
    print(crcl)

import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.circle(circle1.radius)
t.penup()
t.fd(100)
t.pendown()
t.circle(circle2.radius)
t.penup()
t.fd(100)
t.pendown()
t.circle(circle3.radius)
t.penup()
t.fd(100)
t.pendown()
t.circle(circle4.radius)
