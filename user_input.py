'''
Created on Jan 8, 2017

@author: kripa
'''
'''fhandle = open('userdata.txt','a')
name = raw_input("enter your name:")
age = input("enter your age:")
phone = input("enter your mobile number:")
address = raw_input("enter your address:")
fhandle.write("User name is %s \n"%name)
fhandle.write("%s's age is %d \n"%(name,age))
fhandle.write("%s's phone number is %d \n"%(name,phone))
fhandle.write("%s's address is %s \n"%(name,address))
fhandle.close()
'''
import os
path = os.getcwd()
print(path)
abspath = os.path.abspath('usrdata.txt')
print(abspath)
temp = "C:\kripa\user"
print(os.path.exists(temp))
print(os.path.isfile('userdata.txt'))
print(os.path.isfile(temp))
print(os.path.isdir(temp))
print(os.listdir(path))






