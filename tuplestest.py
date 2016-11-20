'''
Created on Nov 20, 2016

@author: kripa
'''
t = 1,2,3,'a',True
print(type(t))
print(t)

#blank_tuple = tuple()
blank_tuple = ()
print(blank_tuple)

# don't use tuple as variable name
'''tuple = "hi"
print(tuple) '''

num = (1,2,3,4,5)
''' (1,2,3,4,5)
     0 1 2 3 4 <- index
    -5-4-3 -2-1 '''
print(num[0])
print(num[-2])
print(num[1:4]) # [m:n] m is first end and n-1 is last end of index
print(num[:2])

# use of operators
sum = (12+3)
print(sum)
print(sum*3)

#sum_t = (12,+3)
#print(sum_t)

sum_t = (12+3,)
print(sum_t*3)

print((1,2,3,4)+(7,8,9))

fruits = ('apple','banana','mango')
print(fruits*3)

print(fruits.index('banana'))
#print(fruits.index('orange'))
print('orange' in fruits)
#fruits.append('apple') # tuples are immutable (not changeable)
#fruits[1] = 'orange'

# swap two variables
a = 6
b = 5
a,b = b,a # tuples assg.
print("a is = ",a)
print("b is =", b)

email_id = "kapilsharma@gmail.com"

''' o/p uname = 'kapilsharma'
        domain = 'gmail.com'
        
        '''      

uname, domain = email_id.split("@")
print("uname is =",uname)
print("domain is =",domain)

a,b,c = 1, 'rahul',5.6 # L.H.S == R. H.S.
print(a)
print(b)
print(c)

result= divmod(9, 2)
print(result)
quot,rem = result
print("quot is =",quot)
print("rem is = ",rem)

def min_max(t):
    return min(t),max(t)
t = (1,2,3,4,5,6)
minimum, maximum = min_max(t)
print("minimum value is = ",minimum)
print("maximum value is =", maximum)

# LIST AND TUPLES

str1 = "hello"
list1 = [1,2,3,4]
list2 = ['one','two','three','four','five']
print(zip(str1,list1))
print(zip(list1,list2))

l = (1,2,[3,4,5],6)
print(l[2])
print(l[2][1])

fan = [(1,2.4,'rahul'),(2,4.5,'a')]
for int_value,float_value,string_value in fan:
    print(int_value)
    print(float_value)
    print(string_value)
    
# enumerate

name = 'rohit'
for index,value in enumerate(name):
    print(" at " ,index, " element is", value)    
    
    
    
    
    
    
    
    
    
    
























