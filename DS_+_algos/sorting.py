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
SELECT-SORT-HELP(A)
    for i = 1 to n - 1 do
        j = findLargest(A, n - i + 1)
        A[j] = A[n - i + 1]
        A[n- i + 1] = A[j]
'''

'''
SEL-SORT-HELPER(A, k)
    index = 1;
    for m = 1 to k do
        if A[m] > A[index]
            index = m
    return index
'''

'''
REC-SEL-SORT(A, n)
    if n <= 1 return
    
'''

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
         
'''
    HEAPIFY(A, i)
    //Guaranteed: subtree rooted at left(i) & right(i) are heaps
    //make the subtree rooted at i into a heap
    l = left(i)
    r = right(i)
    largest = i
    
    if (l <= A.heapsize) ^ (A[l] > A[largest])
        largest = l
    if (r <= A.heapsize ^ (A[r] > A[largest])
        largest = r
    if (largest != i)
        A[largest] <-> A[i]
        Heapify (A, largest)

    NOTE:   parent(i) = floor(i/2)
            left(i)   = 2i
            right(i)  = 2i + 1

'''
def heapify(Arr, iter):
    left = 2 * iter + 1
    right = 2 * iter + 2
    n = len(Arr)
    largest = iter

    if left < n and Arr[left] > Arr[largest]:
        largest = left
    if right < n and Arr[right] > Arr[largest]:
        largest = right
    if largest != iter:    
        Arr[largest], Arr[iter] = Arr[iter], Arr[largest]
        heapify(Arr, largest)
     
'''
    BUILDHEAP(A) //Make A[1..n] into heap
        A.heapsize = n;
        //nodes floor(n/2) + 1, floor(n/2) + 2, ..., n are leaves
        for i = floor(n/2) down to 1 do
            Heapify(A, i)
'''

def buildHeap(Arr):
    for i in range(math.floor(len(Arr) / 2) - 1, -1, -1):
        heapify(Arr, i)
a = [7, 89, 10, 2, 6, 3, 9, 6, 20, 21, 43]

print("before sort a is " + str(a))

#a = insertion_sort(a)
#a = select_sort(a)
a = merge_sort(a, 0, len(a) - 1)
print("after sort a is " + str(a))
b = buildHeap(a)
print("after sort a is " + str(a))
print("b is " + str(b))

