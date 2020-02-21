import math
import sys
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

'''
    MERGE-SORT(A, P, r)
        if p >= r
            return
        q = floor((p  + r) / 2)
        MERGE-SORT(A, p, q)
        MERGE-SORT(A, q+1, r)
        Merge(A, p, q, r)
'''
def merge_sort(arr, l, r):
    if l >= r:
        return
    
    mid = math.floor((l + r) / 2)
    
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    
    merge(arr, l, mid, r)

    return arr
'''    
    MERGE(A, p, q, r)
        n1 = q - p + 1
        n2 = r - q
        let L[1..n1 + 1] and R[1..n2 + 1] be new arrays
        for i = 1 to n1
            L[i] = A[p + i - 1]
        for j = 1 to n2
            R[j] = A[q + j]
        L[n1 + 1] = inf.
        R[n2 + 1] = inf.
        i = 1
        j = 1
        for k = p to r
            if L[i] <= R[j]
                A[k] = L[i]
                i++
            else if  A[k] = R[j]
                j++
'''

def merge(arr, l, mid, r):

    num1 = mid - l + 1
    num2 = r - mid 

    #L = [arr[l + i - 1] for i in range(num1)]
    #R = [arr[mid + j] for j in range(num2)]
    L = [0] * (num1)
    R = [0] * (num2)

    for i in range(0, num1):
        L[i] = arr[l + i]

    for j in range(0, num2):
        R[j] = arr[mid + 1 + j]

    i = j = 0
    k = l

    while i < num1 and j < num2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < num1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < num2:
        arr[k] = R[j]
        j += 1
        k += 1
         
a = [7, 89, 10, 2, 6, 3, 9, 6, 20, 21, 43]

print("before sort a is " + str(a))

#a = insertion_sort(a)
#a = select_sort(a)
a = merge_sort(a, 0, len(a) - 1)

print("after sort a is " + str(a))

