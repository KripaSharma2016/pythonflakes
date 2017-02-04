'''
Created on Jan 8, 2017

@author: kripa
'''
import os

'''fhandle = open('systemdata.txt','w')
def findir(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname,name)
        if os.path.isdir(path):
            findir(path)
        else:
            print(path)
            fhandle.write(path+"\n")    
path = "C:\Program Files (x86)"
findir(path)     
'''
fhandle =open('userdata.txt','r')
#data =fhandle.read()
#print(data)
#print(data[:30])
#print(len(data))
for line in fhandle:
    line = line.rstrip()
    if line.startswith("User"):
        print(line)
cmd = 'notepad'
fp = os.popen(cmd)    
data = fp.read()
fp.close()    