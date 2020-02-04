from student import Student

stu1 = Student("Bret", "Business", 3.5, False)
stu2 = Student("Frieda", "Art", 2.8, True)

print(stu2.on_honor_roll())
print(stu1.on_honor_roll())

num = {1, 2, 3, 4, 5, 6}
print(num)
num.add(7)
print(num)
num.remove(3)

num2 = {2, 3, 4, 7, 8}

#res = num.union(num2)
print(num | num2)

#res = num.intersection(num2)
print(num & num2)

#num.difference(num2)
print(num - num2)


