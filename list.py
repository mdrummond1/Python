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