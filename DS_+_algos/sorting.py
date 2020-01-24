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
    
a = [12, 9, 5, 2, 11, 98, 34, 76, 10]

print("before sort a is " + str(a))

a = insertion_sort(a)

print("after sort a is " + str(a))