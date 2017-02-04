'''
Created on Jan 10, 2017

@author: kripa
'''
class Point:
    pass
print(Point)

p =Point()
print(p)

p.x = 3.0
p.y = 4.0
print("x axis is "+str(p.x))
print("y axis is "+str(p.y))

import math
distance = math.sqrt(p.x**2+p.y**2)
print(distance)


class Circle():
    pass
cr1 = Circle()
cr1.point = Point()
cr1.radius = 5.8
cr1.point.x = 3.0
cr1.point.y = 4.0
print("circle point is",cr1.point.x,cr1.point.y)
print("circle radius is ",cr1.radius)



















