'''
Created on Feb 2, 2017

@author: kripa
'''

import re

'''if re.search('was', 'this is a dog'):
    print("data is available!")
else:
    print("not available")    
    
para = "While anonymous access grants one way to enter into systems, attackers alsohave been quite successful with using stolen credentials to gain access to legiti mate FTP servers. FTP Client programs, such as FileZilla, often store passwords" 
data = re.findall('.a...', para)  
print(data)
for i in data:
    print(i) '''


f = file("ipconfig.txt")
f1 = file('mydata','w')
for line in f:
    if re.match(r'(.*)IPv6 Address(.*?)', line):
        print(line)
        newline = line.split(':',1)[1].strip()
        f1.write("ipv6 is= :"+newline)
        f1.write("\n")
        print(newline)
        print("\n")
    if re.match(r'(.*)IPv4 Address(.*?)', line):
        print(line)
        newline = line.split(':',1)[1].strip()
        f1.write("ipv4 is= :"+newline)
        f1.write("\n")
        print(newline)
        print("\n")
    if re.match(r'(.*)Subnet Mask(.*?)', line):
        print(line)
        newline = line.split(':',1)[1].strip()
        f1.write("Subnet Mask is= :"+newline)
        
        print(newline)
        f1.write("\n")
        print("\n")
    if re.match(r'(.*)Default Gateway(.*?)', line):
        print(line)
        newline = line.split(':',1)[1].strip()
        f1.write("Default Gateway is= :"+newline)
        print(newline)            
f.close()
f1.close()            