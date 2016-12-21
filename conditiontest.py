'''
Created on 22-Nov-2016

@author: ks016399
'''
# more about print and import

print 1,23,4
print(1,23,4)

print 'hello',
print 'rohan'

print(1, 'rohan' , 4.5)
print(str(1)+'rohan' +str(4.5))
#print(print('hello'))

# Assignment Logic
x,y,z = 3,4,5
print(x,y,z)
x,y = y,z
print(x,y,z)

numbers = (1,2,3)
x,y,z = numbers
print(x,y,z)

# Augmented Assignments
x =2 
y *=x
print(y)

# for other datatype also
first_name = "kapil"
last_name = "sharma"
first_name +=last_name
print(first_name)

# all values considered as false
# False none 0 "" () [] {}

print(True+40)
print(False+40)

print(bool("hello"))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#if bool(()) == bool({}) == False :
#    print("hi")
   
   
# conditions
# Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated.

name = "peter"
print(name == "peter")
value = 7
print(value > 10)
age = 18 
name = "rahul"
if name=="rahul" and age ==18:
    print("welcome rahul")

if name=="rahul" or age ==19:
    print("welcome rahul")   

fruits = ['orange','mango','apple']
if 'apple' in fruits :
    print("found it")
# share ppt
# is operator
a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(a is b)
a = b
print(a is b)

#Strings are compared according to their order when sorted alphabetically:
print("use string")
print("alpha" < "beta")
'''name = raw_input("Enter your full name")
if name.endswith("sharma"):
    print("hello, sharma")'''
    
    
# elif
'''
num = input("enter any number")
if num>0:
    print("number is positive")
elif num <0:
    print("number is negative")
else :
    print("number is zero")       

# check range of number that user enter     
# exercise_one    
print(5 if 1 else 10)  
print(5 if 0 else 10) '''

# work with dictionary
price = {'apple':'110',
         'mango' : '50',
         'orange' : '80'
         }    
print(price.get('apple','not defined'))
print(price.get('banana','not defined'))

# using if - else clause
if 'banana' in price:
    print(price['apple'])
else:
    print("Bad choice")   
# we can use try catch, we will see it later     
# find the largest number in three numbers
#a,b,c = 8,9,10
#a,b,c = 8,90,10
a,b,c = 80,9,10
if a > b and a >c:
    print("a is largest",a)
elif b>c:
    print("b is largest",b)
else:
    print("c is largest",c)        
     
exit()       

















    























