
#Functional programming
print("===============FUNCTIONAL!===============")
def add_ten(x):
    return x + 10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten, 4))

#lambdas
print("==================LAMBDAS======================")

def square(x):
    return x**2
print(twice(square, 2))


result = (lambda x, y: x**y)(2, 3)

print(result)

#map
print("=======================MAP==================")
newList = [10, 9, 7, 4, 11, 6]
list1 = list(map(lambda x: x + 2, newList))
print(list1)


#filter
print("======================FILTER====================")
res = list(map(lambda x: x + 2, filter(lambda x: x % 2 == 0, newList)))
print("res {}".format(res))

#generators
print("=====================GENERATORS===================")
def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

def evens(x):
    for i in range(x + 1):
        if i % 2 == 0:
            yield i


lis = [x for x in function()]

print(lis)
print(list(evens(20)))

#intertools
print("===================ITERTOOLS=================")
from itertools import count
from itertools import accumulate
from itertools import takewhile

for i in count(3):
    print(i)
    if i >= 5000:
        break

numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers), ))
