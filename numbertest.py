'''
Created on Nov 5, 2016

@author: kripa
'''
hours = 30
minute = hours *30
#hours * 60 = minutes # SyntaxError

print(120+130) # + , - , /, *
print(4.5*4)
print(7.8/2)

# Use of math built-in
import math
print(math)
print(math.sqrt(4))

# convert degree into radian
degree = 90
radian = degree/360.0*2*math.pi
print(math.sin(radian))

#print(math.sqrt(-4)) #RuntimeError




import cmath
print(cmath.sqrt(-4))

#Random built-in
import random
print(random)
print(int(10*random.random()))
print(random.__all__)



