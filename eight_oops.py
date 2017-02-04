'''
Created on Jan 22, 2017

@author: kripa
'''
class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def getName(self):
        return "{} {}".format(self.first_name,self.last_name)  
p1 = Person("Jerin",'james')
print(p1.getName())   

class Employee(Person):
    def __init__(self,first_name, last_name,emp_id,dpt):
        super().__init__(first_name, last_name)
        self.emp_id = emp_id
        self.dpt = dpt
    def getDetails(self):
        return "emp_id {} for {} is from {}".format(self.emp_id,self.getName(),self.dpt) 
emp1 = Employee("rohan","sharma","102",'R&D')
print(emp1.getDetails())   
p2 = Person('GINU','ALAN')
print(p2.getName())