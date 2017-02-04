'''
Created on Jan 8, 2017

@author: kripa
'''
class First():
    def __init__(self,name):
        self.fname=name
        print("this is init method "+name+ " " +self.fname)
#ins = First()
#print(ins)
First("rohan")
obj = First('jerin')

class Fruits(object):
    def __init__(self,name):
        self.fruit_name = name
        print("your fruit in cart is "+self.fruit_name)
        
banana = Fruits('banana')
apple = Fruits('apple') 

class Person():
    pass
p1 = Person()
p1.name = "jerin"
p1.age = 24

p2 = Person()
p2.name = "Ginu"
p2.age = 45
print(p1)
print(p2)
print(p1.name,p2.age)

print("{0} is {1} years old".format(p1.name,p1.age))
print("{0} is {1} years old".format(p2.name,p2.age))














     











