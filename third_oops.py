'''
Created on Jan 14, 2017

@author: kripa
'''
class Point:
    pass
p1 = Point()
print(p1)
p2 = p1
print(p2)
p1.x=9.0
p1.y = 11.0
print(p1.x,p1.y)
print(p2.x,p2.y)
print(p1 == p2)
print(p1 is p2)
import copy
p3 = copy.copy(p1)
print(p1)
print(p3)
print(p1 == p3)
print(p1 is p3)
print(p3.x,p3.y)
p3.x=5.0
p3.y =5.0
print(p3.x,p3.y)
print(p1.x,p1.y)

class Circle():
    pass
cr1 = Circle()
cr1.point = Point()
cr1.radius = 5.8
cr1.point.x = 3.0
cr1.point.y = 4.0
#print("circle cr1 point is",cr1.point.x,cr1.point.y)
print("circle cr1 radius is ",cr1.radius)
cr2  = copy.copy(cr1)
#print("circle cr2 point is",cr2.point.x,cr2.point.y)
#print("circle cr2 radius is ",cr2.radius)
cr2.radius = 8.9
cr2.point.x= 6.8
cr2.point.y = 7.8
print("circle cr1 point is",cr1.point.x,cr1.point.y)
print("circle cr1 radius is ",cr1.radius)
print("circle cr2 point is",cr2.point.x,cr2.point.y)
print("circle cr2 radius is ",cr2.radius)
cr2 = copy.deepcopy(cr1)



















