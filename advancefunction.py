'''
Created on Jan 6, 2017

@author: kripa
'''
def printer(msg):
    print(msg)

printer("hello world")   # direct call
x = printer  
x("rohan") # indirect

def indirectcall(func,msg): # Argument call
    func(msg)
indirectcall(printer, "bye bye")        

y = x
y("jerin")
print(y.__name__)

# lambda
def func(x,y,z): return x+y+z
print(func(1,2,3))
var = (lambda x,y,z : x+y+z)
print(var(1,2,3))
print(var('aa','bb','cc'))
def f1(x): return x**2
def f2(x): return x**3
def f3(x): return x**4
l = [f1,f2,f3]
for i in l:
    print(i(2))

l = [lambda x:x**2,
     lambda x:x**3,
     lambda x:x**4]
for i in l:
    print(i(2))
dictFuvtion = { 'add':lambda x,y:x+y,
               'sub':lambda x,y: x-y
               }  
print(dictFuvtion['add'](2,4))  
  
    


















