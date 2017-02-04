'''
Created on Jan 26, 2017

@author: kripa
'''
''' module is .py '''
from importmodule import Employee
#from mypackage.fruitsmodules import Fruits
#from mypackage.fruitsmodules import Animal
from mypackage.fruitsmodules import *
from mypackage.othermodule import Person
emp_1 = Employee('Jerin')
print(emp_1.showDetails())
banana = Fruits('banana')
dog = Animal('dog')
p1 = Person()
p1.m()
print(dog.showDetails())
print(banana.showData())
