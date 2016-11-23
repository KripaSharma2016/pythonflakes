'''
Created on 21-Nov-2016

@author: ks016399
'''
''' write a program which will display personal information of employee Like
phonenumber, dpt, and address. demand on request
 exp :
 enter employee name : vipul
 phonenumeber(p) , dpt(d), or address (a) ? p
 vipul phone number is 1234 '''
 
 # Solution
emp_info = {'vipul' : {'phone':'1234',
                        'dpt' : 'r&d',
                        'address' : 'delhi'
                        },
             'jerin' : {
                        'phone' : '456',
                        'dpt' : 'testing',
                        'address' : 'blr'
                        }
             }
name = raw_input("enter employee name")
request = raw_input("phonenumeber(p) , dpt(d), or address (a) ?")

key = "None"

if request == 'p':
    key = 'phone'
elif request == 'd':
    key = 'dpt'
elif request == 'a':
    key = 'address'
else :
    print("sorry there is no option like you entered")      

if name in emp_info:
    print(name+"'s"+" " +key+" " +' is '+emp_info[name][key])    
                
    
    




