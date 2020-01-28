def addBinInt(a, b):
    if len(a) != len(b):
        print("arrays must me the same size")
        return [-1]
    
    n = len(a) - 1
    print("n: " + str(n))
    c = [0 for i in range(len(a) + 1)]
    
    while n >= 0:
        sum = a[n] + b[n] + c[n+1]
        if sum == 2:
            c[n] += 1
            sum = 0
        elif sum == 3:
            c[n] += 1
            sum = 1
        c[n+1] = sum
        print(c)
        n -= 1
    return c

arr1 = [1, 1, 1, 0] #13
arr2 = [0, 1, 1, 1] #27
#arr3 = [1, 0, 1, 0, 0, 0] 40
arr3 = addBinInt(arr1, arr2)
print(arr3)