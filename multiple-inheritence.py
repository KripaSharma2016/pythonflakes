'''
Created on Jan 26, 2017

@author: kripa
'''
class Batsman:
    def __init__(self,name):
        self.__batsMan=name
    def getBatsManName(self):
        return self.__batsMan
    def setBatsManName(self,name):
        self.__batsMan=name  
class Boller:
    def __init__(self,name):
        self.__bolerName=name
    def getBollerName(self):
        return self.__bolerName
    def setBollerName(self,name):
        self.__bolerName=name  
class Keeper:
    def __init__(self,name):
        self.__keeperName=name
    def getKeeperName(self):
        return self.__keeperName
    def setKeeperName(self,name):
        self.__keeperName=name        
class Player(Batsman,Boller,Keeper):
    def __init__(self,name):
        Batsman.__init__(self, name)
        Boller.__init__(self, name)
        Keeper.__init__(self, name)
p1 = Player("M S Dhoni")
print(p1.getBatsManName()) 
print(p1.getKeeperName())    



class A(object):
    def m(self):
        print("this is from A")
class B(A):
    def m(self):
        print("this is from B")
class C(A):
    def m(self):
        print("this is from C")
class D(C,B):
    def m(self):
        print("this is from D")
        '''C.m(self)
        B.m(self)
        A.m(self)'''
d1 = D()
d1.m()
C.m(d1)  

print("--------using MRO--------")
'''
MRO
'''
class A(object):
    def m(self):
        print("this is from A")
class B(A):
    def m(self):
        print("this is from B")
        super(B,self).m()
class C(A):
    def m(self):
        print("this is from C")
        super(C, self).m()
class D(C,B):
    def m(self):
        print("this is from D")
        super(D, self).m()
d2 = D()
d2.m()        
        
      
               
       
                  