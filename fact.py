def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)

get = int(input("enter max factorial to find: ")) + 1

for i in range(get):
    print("fact " + str(i) + ": " + str(fact(i)))