#string formatting
numbers = [12, 5, 2017]
string = "Date:{0}/{1}/{2}".format(numbers[0], numbers[1], numbers[2])
print("string: {}".format(string))
a = "{x}/{y}".format(x = 100, y = 200)
print(a)

#string functions
print("hiya ".join(["Apple", "Banana", "Mango"]))
print("hello there".replace("l", "WORLSD", 1))
newStr = "This is a new string"
print(newStr.startswith("This"))
print(newStr.endswith("ing"))
print(newStr.endswith("ung"))
print(newStr.lower())
print(newStr.upper())

