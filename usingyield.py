numbers = [1,2,3,4,5]
def cub(l):
    result=[]
    for i in l:
        result.append(i**3)
    return result
print(cub(numbers))
def cub_g(l):
    for i in l:
        yield i**3
obj = cub_g(numbers)     
print(obj) 
for num in obj:
    print(num)
'''print(next(obj)) 
print(next(obj))  
print(next(obj)) 
print(next(obj)) 
print(next(obj)) 
print(next(obj)) '''

my_num = [x**3 for x in [1,2,3,4,5]] 
print(my_num)
my_num = (x**3 for x in [1,2,3,4,5]) 
print(my_num)
for i in my_num:
    print(i)
   
    
    
    



    