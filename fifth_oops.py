'''
Created on Jan 14, 2017

@author: kripa
'''
class C(object):
    
    count = 0
    def __init__(self):
        type(self).count +=1
    def __del__(self):
        type(self).count -=1
    def printer(self,msg):
        self.msg = msg 
        print("your msg is = "+self.msg)   
c1 = C()
c2 = C()
c3 = C()
del c2
print("number of instances =",C.count) 
c1.printer("hello delhi")  


class Cal:
    def add(self,x,y):
        self.x = x
        self.y = y
        return x+y
    def sub(self,x,y):
        self.x = x
        self.y = y
        return x-y
    def mul(self,x,y):
        self.x = x
        self.y = y
        return x*y
obj = Cal()
print(obj.add(5, 6))    
print(Cal.mul(obj,4, 7))  


class Book(object):
    __writername = "rohan sharma"
    __readername  = "jemes alen"
    
    @classmethod
    def writer(cls):
        return Book.__writername
    @staticmethod
    def reader():
        return Book.__readername
    def printer(self):
        return "this is printer"
print(Book.reader())
print(Book.writer())
#print(Book.printer())
b1 = Book()
print(b1.reader())
print(b1.writer())
print(b1.printer())
print(Book.printer(b1))



  