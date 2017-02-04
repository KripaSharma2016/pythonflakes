'''
Created on Jan 22, 2017

@author: kripa
'''
class Person:
    
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name =name
    @property
    def show_details(self):
        return "{}{}".format(self.name, " you are smart")    
        
if __name__ == "__main__":
    p1 = Person('jerin')  
    print(p1.name)
    print(p1.show_details)  
    p2 = Person("Ginu")
    print(p2.show_details)        