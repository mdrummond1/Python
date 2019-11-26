def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

num = int(input("How high do you want to go?")) + 1

for i in range(num):
    print("fact " + str(i) + ": " + str(fact(i)))