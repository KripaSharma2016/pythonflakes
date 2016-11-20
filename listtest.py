'''
Created on Nov 20, 2016

@author: kripa
'''
num = [1,2,4,5,5]
emp_name = ['john','james','rahul']
merged_list = [1,2,'rahul',False,[1,2,3,4]]

# ['john','james','rahul']
#    0       1       2
#   -3       -2       -1

print(emp_name[1])
print(emp_name[-2])

''' [1,2,'rahul',False,[1,2,3,4]]
     0 1    2      3       4
    -5 -4  -3     -2         -1 
    '''
print(merged_list[4][3])    

# blank list 
#fruits = list()
fruits = []
print(fruits)

fruits = ['apple','orange','banana']
fruits[1] = 'grapes'
print(fruits) # list is mutable (changeable)

print('apple' in fruits)
print('orange' in fruits) # membership

for fruit in fruits:
    print(fruit)
    
print(len(fruits))    
print(range(8)) # n -1

for i in range(len(fruits)):
    print("at index ", i , " element is ", fruits[i])
    
list_one = [1,2,3,4,5]
list_two = ['kapil','rahul']
list_three = list_one + list_two
print(list_three)    

# list slicing

print(list_one[1:4]) # [m:n] m -s fist end or n-1 will be last end
print(list_one[:])

list_one[1:3] = [8,9,5] 
print(list_one)

# matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][2])

# build in methods
fruits = ['apple','orange','banana']
fruits.append('grapes')
print(fruits)

list_alpha = ['e','t','a','c','d']
list_alpha.sort(cmp=None, key=None, reverse=True)
print(list_alpha)

fruits.sort(cmp=None, key=None, reverse=False)
print(fruits)

print(fruits.index('banana'))
print(fruits.count('apple'))
fruits.append('apple')
print(fruits.count('apple'))

# delete elements from list
print(fruits)
print(fruits.pop())
print(fruits)
fruits.pop(1)
print(fruits)

fruits.remove('grapes')
print(fruits)

# find min max
num = [1,2,3,4,5,6,7]
print(max(num))
print(min(num))

# string and list
sentence = "he is running"
list_sen = list(sentence)
print(list_sen)
list_sen = sentence.split(' ')
print(list_sen)

path = "C:/Python27/DLLs"
delemeter_1 = '/'
path = path.split(delemeter_1)
print(path)
delemeter_2 = '.'
path = delemeter_2.join(path[1:])
print(path)






