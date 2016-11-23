#coding=utf-8

'''
Created on 11-Nov-2016

@author: ks016399
'''
'''A dictionary is like a list, but more general. In a list, the indices have to be 
integers; in a
dictionary they can be (almost) any type.'''

''' You can think of a dictionary as a mapping between a set of indices (which are called keys)
and a set of values. Each key maps to a value. The association of a key and a value 
is called
a key-value pair or sometimes an item. ''' 
''' example is suppose you want to create phonebook using list '''
name = ['rahul','vipul','jerin','ginu']
numbers = ['123','09123','0652','3450']
print(numbers[name.index('jerin')])
''' It works, but it’s a bit impractical. What you really would want to do is something like the
following:'''
# phonebook['jerin']
phonebook = {'rahul': '123','vipul': '09123','jerin' : '0652', 'ginu' : '3450'}
print(phonebook['jerin'])

# create a blank dictionary
convertor = dict()
print(convertor)

''' we will build a dictionary which will convert from english to hindi language '''
convertor = { 'banana' : 'केला','lion':'शेर'}
print(convertor['banana'])
verb_convertor = {'running':'दौड़ना','bathing':'नहाना'}
print(verb_convertor['running']) # <------ this operation called lookup
print(verb_convertor)

''' order of key-value pair is unpredictable '''
numbers = {1:'one', 2:'two', 3:'three', 4:'four'}
#print(numbers[0])  # exception key error

# dict() function if you have key value pair like :
details = dict([('name','kripa'),('age',20)])
print(details)

d = dict(name='kripa',age = 20)

print(d)

print(len(numbers))

'''The in operator works on dictionaries; it tells you whether something appears as a key in
the dictionary '''
print(1 in numbers)
print('one' in numbers)

number_values = numbers.values()
print('one' in number_values)

# program 1

# build in functions 
print(numbers)
numbers = numbers.clear()
print(numbers)
''' why this is useful '''
x = {'age':20}
y = x
print(y)
#x = {}
#print("x is=",x)
#print("y is =",y)

# use clear function
x.clear()
print("x is=",x)
print("y is =",y)

# copy function
x = {'name':'pk','phone':['1234','567','980']}
y=x.copy()
print("x is =",x)
print("y is =",y)
y['phone'].remove('567')
print("x is =",x)
print("y is =",y)

# how to avoid this error
from copy import deepcopy
x = {'name':'pk','phone':['1234','567','980']}
y=x.copy()
x = deepcopy(x)
y['phone'].remove('567')
print("x is =",x)
print("y is =",y)

# get
x = {}
#print(x['name']) # return keyerror to avoid or you want to make it user defined 
print(x.get('name'))
print(x.get('name','key not found'))

# has_key()
d = {}
print(d.has_key('name'))
d['name'] = 'kapil'
print(d.has_key('name'))

# items and iteritems
dict = {'name':'kapil','age':22}
print(dict.items())
print(dict.iteritems())
it = dict.iteritems()
it = list(it) # convert iterator to list
print(it)

# keys and iterkeys
dict1 = {'name':'kapil','age':22}
print(dict1.keys())
print(dict1.iterkeys())

# pop and popitem
dict1['phone'] = "1234"
print(dict1)
#dict1.pop()
dict1.pop('age')
print(dict1)
dict1.popitem() # remove from last element
print(dict1)

# update
x = {'name':'kapil','age':22}
y = {'phone': '1234'}
#print(x+y)
x.update(y)
print(x)

''' you are given a string and you want to count how many times each letter appears'''
sentence = 'hi, how are you?'
dict1 = dict()
for i in  dict1 :
    if i not in dict1:
        dict1[i] = 1
    else :
        dict1[i] +=1
print(dict1[' '])
print(dict1['h'])   

# loop in dictionary
for obj in dict1 :
    print(obj,dict1)
value = dict1.values()
print(value)
for obj in dict1.values():
    print(obj,dict1) 
keys = dict1.keys()
print(keys)       

# create reverse look-up
''' if you want to access key using value that process is called reverse lookup '''
def reverse_lookup(d,v):
    for k in d :
        if d[k] == v :
            return k
        
print(reverse_lookup(dict1, 1))     

# dictionary and list 
#found out the list of letters in string who is having frequency 2
def reverse_dict(d):
    rev_dict = dict()
    for key in d :
        val = d[key]
        if val not in rev_dict:
            rev_dict[val] = [key]
        else:
            rev_dict[val].append(key)
    return rev_dict
inverse_dict = reverse_dict(dict1)
print(inverse_dict[1]) 
print(inverse_dict[1][0])

# how many letters are having 1 frequency in same string

print(len(inverse_dict[1]))

# example
movies = {'koi mil gya' : '2002',
          'hm apke h kon' : '2000'
          }
for (key,value) in movies.items():
    print(key + " realesed in " +value)
    
#extra generalised form  
print([key for (key,value) in movies.items() if value == '2000' ])

          
            
        
    
      