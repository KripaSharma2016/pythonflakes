'''
Created on Jan 29, 2017

@author: kripa
'''
#f = open("myfile.txt")
'''try:
    f = open("myfile.txt")
except Exception as ex:
    print(str(ex))
else:
    print(f.read())
    f.close()  
finally:
    print("end of the program")    

try:
    f = open("virus.bat")
    if f.name == 'virus.bat':
        raise Exception
except Exception:
    print("not valid file")

try:
    num=90
    if num==90:
        raise Exception
        print("this is if clause after raise")
    print("this is after exception")
except Exception:
    print("this is and error")
'''
class MyError(RuntimeError): 
    def __init__(self,msg):
        self.msg=msg
try:
    raise MyError("this is created my own error")     
except MyError as ex:
    print(ex.msg)      









