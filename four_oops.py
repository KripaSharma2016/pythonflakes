'''
Created on Jan 14, 2017

@author: kripa
'''
class Fruits:
    cost = '60'
    def __init__(self,name):
        self.name = name
        print("fruits is "+self.name)
banana = Fruits('banana') 
apple = Fruits('apple')  
print("cost of banana is "+banana.cost)
print("cost of apple is "+apple.cost)  
print(Fruits.cost)
#print(Fruits.name)
print(banana.name)