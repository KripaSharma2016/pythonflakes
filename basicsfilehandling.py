'''
Created on Jan 8, 2017

@author: kripa
'''
fhandle = open('abc.txt','w')
line1 = "he is running.\n"
fhandle.write(line1)
line2 = "he is playing.\n"
fhandle.write(line2)
name = "rohan"
age = 20
CGPA = 7.82
fhandle.write(name+'\n')
fhandle.write(str(age)+'\n')
fhandle.write(str(CGPA)+'\n')










fhandle.close
fhandle = open('abc.txt','r')
data =fhandle.read()
print(len(data))