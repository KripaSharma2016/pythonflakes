'''
Created on 21-Dec-2016

@author: kripa
'''
# looping concept with all build in types
# use of while loop with numbers
# suppose you want to print numbers from 1 to 1000
x =1
while x <=1000:
    print(x)
    x +=1

# while loop with string

name = "rohan sharma"
i = 0
while i < len(name):
    print(name[i])
    i +=1
    
# while loop with list
fruits = ['banana','apple','mango']
i = 0
while i < len(fruits):
    print(fruits[i]) 
    i+=1
# while loop with tuples

fruits = ('banana','apple','mango')
i =0
while i < len(fruits):
    print(fruits[i])
    i +=1
# while loop with dictionary
'''data = {'username': 'rohan',
        'password': 'bsr@123'}
uname = raw_input("enter user name :")
pwd = raw_input("enter password :")

while uname != data['username'] or pwd != data['password']:
    print("Incorrect")
    uname = raw_input("enter user name :")
    pwd = raw_input("enter password :")
print("Welcome to your account")
exit()   ''' 
# for loop
# suppose you want to print numbers from 1 to 10
for i in range(10):
    print(i)
for i in range(1,11):
    print(i) 
    
# print odd numbers till 10
for i in range(1,11,2):
    print(i) 
print(range(1,10,2)) 
# print even numbers till 10 
for i in range(1,11,2):
    print(i+1)     

# for loop with string
name = "rohan sharma"
print(range(len(name)))
for i in range(len(name)):
    print(name[i])      
   
# for loop with list
fruits = ['banana','apple','mango']
for i in range(len(fruits)):
    print(fruits[i])
# for loop with tuples
fruits = ('banana','apple','mango')
for i in range(len(fruits)):
    print(fruits[i])
# nested loop and matrix examples
i =1
while i<= 4:
    j=1
    while j <= i:
        print j,
        j +=1
    print("")
    i +=1  
result = []     
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result) 

result1 = [(x,y) for x in range(3) for y in range(3)] 
print(result1)      
                       
# use break, continue, pass control statement
for i in range(10):
    print(i)
    if i == 4:
        print("before break")
        break
        print("after break")
        
for i in range(10):
    print(i)
    if i == 4:
        print("before continue")
        continue
        print("after continue")

option = raw_input("enter your choice")

if option == "ON_FAN":
    print("on fan")
elif option == "ON_TV":
    print("on tv")
elif option == "OPEN_DOOR":
    pass
else:
    print("Invalid choice") 
           

    