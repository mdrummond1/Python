'''
	INSERTION-SORT(A):
		1 for j = 2 to A.length
		2       key = A[j]
		3       // Insert A[j] into the sorted sequence A[1.. J - 1]
		4       i = j - 1
		5       while I > 0 and A[i] > key
		6             A[I + 1] = A[i]
		7             i = i - 1
        8       A[I + 1] = key
'''

def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1

        array[i + 1] = key

    return array
    
'''
    SELECT-SORT(A)
        for i = 1 to n - 1 do
            //find smallest key in  A[1..n]
            //exchange it with A[i]
            for j = i + 1 to n do
                if A[j] < smallest
                    loc = j
            //A[i] <-> A[loc]
            A[loc] = A[i]
            A[i] = smallest
'''

def select_sort(array):
    for i in range(0, len(array) - 1):
        smallest = array[i]
        loc = i
        for j in range(i + 1, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                loc = j
        array[loc] = array[i]
        array[i] = smallest
    return array

a = [9, 12, 3, 6, 112, 98, 34, 75, 7]

print("before sort a is " + str(a))

#a = insertion_sort(a)
a = select_sort(a)

print("after sort a is " + str(a))

