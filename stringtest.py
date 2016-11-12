'''
Created on Nov 6, 2016

@author: kripa
'''
#first_name = input("enter your first name")
#first_name = raw_input("enter your first name")
#print("hello"+ " " +first_name)

print("hello world")
print('hello world')
#print('let's play) 
print("let's play") 
print('let\'s play')

print(len("vipul"))

name = "rahul"
print(name[0])

# r  a  h  u  l
# 0  1  2  3  4
# -5 -4 -3 -2 -1
print(name[-2])
print(name[-5])


print(name[len(name)-1])

# slicing
city = "bengaluru"
print(city[3:6]) # city[m:n] m - is starting piont and n - end piont
print(city[:])
print(city[:4])
mini_city = city[3:5]
print(mini_city)

# Concatenation
print("vipul" " " " khatiyan")
first_name = 'vipul'
last_name = 'khatiyan'
#print(first_name " " last_name) #Syntax error 
print(first_name + " " + last_name)

# string is immutable (unchangeable)
name = 'rahul'
#name[2] = 't'  # Runtime error (str' object does not support item assignment)
changed_name = name[:2] + 't' + name[3:]
print(changed_name)
print(name)

# string built-in methods
name = 'vipul'
print(name)
print(name.capitalize())
print(name.upper())
print(name.find('pu'))

word = 'he . is . running '
print(word.split('.'))
print(word.split('.')[0])

# Long string
para = """hjsh djdhgHDkjdhnGD dbDGYkudhioUNGVDHAI SGFYGAFIJAHFGAHSFJKA JFJAGHFGASFHAHFJHAKGHDFGadak  hjsahfgahfk"""
print(para)

import re
match = re.match("HELLO[ \t ] *(.*)world","HELLO python world")
print(match.group(1))

print(dir("vipul"))







