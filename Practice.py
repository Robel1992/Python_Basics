print('hello world!')

#function adding two numbers
def add(first, second):
    return first+second

print(add(1,3))

#importing pdb to see where there's a break in your code
#import pdb
#pdb.set_trace()
#add(1, "two")

fruits = [
    {'name' : 'apple', 'price': 20},
    {'name' : 'avacado', 'price': 10},
    {'name' : 'orange', 'price': 5}
]

fruit_names = []
for fruit in fruits:
    fruit_names.append(fruit['name'])
print(fruit_names)

fruit_names_2=[fruit['name'] for fruit in fruits if fruit['name'][0] == 'a']
print(fruit_names_2)

#dict comprehension
dict_comprehension = {fruit['name']: fruit['price'] for fruit in fruits}
print(dict_comprehension)

#The Lambda, basically a funtion with different funtion

#regular function
def mult(x, y):
    return x*y

#lamba

#mult2 = lambda x,y: x*y

print(mult(2,3))
#print(mult2)

#Example of a function
more_than_one_nums = filter(lambda x: x>1, [1,2,3])
print(list(more_than_one_nums))







