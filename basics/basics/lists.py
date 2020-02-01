num = [4, 16, 7, 9, 13, 12, 14]
friends = ["Brad", "Frank", "Wizard", "Tut", "Da fruitster"]

friends.insert(4, "Willam")
friends.append("Creamy J")

print(friends)
friends.sort()
print(friends)
friends.extend(num)
friends.remove("Tut")
print(friends)

number_grid = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9],
    [0]
]

for row in range(len(number_grid)):
    for column in range(len(number_grid[row])):
        print(number_grid[row][column])

#list slicing
print(num[1:5:2])

#list comprehensions
list1 = [x**2 for x in range(5) if x**2 % 2 == 1]
print("list1: {}".format(list1))