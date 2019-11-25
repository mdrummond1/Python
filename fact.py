def fact(num):
    return num * fact(num - 1)

print("fact 4: " + str(fact(4)))