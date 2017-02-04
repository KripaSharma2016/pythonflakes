'''
Created on Jan 6, 2017

@author: kripa
'''
'''
what is recursion?
----> function that call themselves either directly or indirectly in
order to loop. '''
numbers = [1,2,3,4,5,6,7]
result = 0
for i in range(len(numbers)):
    result +=numbers[i]
print(result)  

def addall(l):
    print(l)
    if not l:
        return 0
    else:
        print(l[0])
        return l[0]+addall(l[1:])
print(addall(numbers))   

def addall1(l):
    return 0 if not l else l[0]+addall1(l[1:])
print(addall1(numbers))

    


  