'''
Created on Jan 22, 2017

@author: kripa
'''
'''class Fruits:
    
    def __init__(self,name):
        #print("fruit is "+name)
        self.name = name
        print("fruit is "+self.name)
obj1 = Fruits("banana")
print(obj1.name)
'''
class Fruits:
    
    def __init__(self,name):
        self.name= name
        pass
    
    def set_name(self,name):
        self.__name=name
    
    def get_name(self):
        return self.__name        
        

obj1 = Fruits("banana")
obj1.set_name("bnana")
print(obj1.get_name())













