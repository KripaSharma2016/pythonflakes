'''
Created on Jan 26, 2017

@author: kripa
'''
class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def __repr__(self):
        return "Person({},{},{})".format(self.name,self.age,self.address)
    def __str__(self):
        return "{} is {} years old".format(self.name,self.age)
    def __add__(self,other):
        return self.age+other.age   
    def __len__(self):
        return len(self.name)
p1 = Person('Jerin',50,'Delhi')
p2 = Person('Ginu',30,'blr')
print(p1+p2)
print(p1.__len__())

class Test(object):
    
    __slots__ = ('x','y')
    def __init__(self,num):
        self.x = num

t1 = Test(60)
t1.x=88
print(t1.x)
t1.y = 90
print(t1.y)
#print(p1) 
#print(p2)
#print(p1.__repr__())  
#print(p2.__str__())     
#print(repr(p1))  
#print(str(p2))     
#print(str.__add__('a','b'))
#print(len('india'))
#print('india'.__len__())
#print(30+78)
#print(int.__add__(30,78))
#print(float.__sub__(45.0,12.2))











