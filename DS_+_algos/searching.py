'''
    LINEAR-SEARCH
        for i = 1 to n do
            if A[i] = v
                print(i)
                return
        print(0)
'''
def linearSearch(array, x):
    for i in range(0, len(array)):
        if array[i] == x:
            return i
            print("found!")

array = [2, 5, 4, 7, 9, 8]

print(linearSearch(array, 10))