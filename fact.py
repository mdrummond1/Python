def fact(num):
    if num == 0:
        return 1
    if num < 0:
        print ("ERROR! must be a positive value.")
        return 0
    return num * fact(num - 1)

get = int(input("enter max factorial to find: ")) + 1

for i in range(get):
    result = fact(i)
    print("fact " + str(i) + ": " + str(result))
    print("length: " + str(len(str(result))))