"""
This algorithm sort the elements by the size
of the elements (units, tens, etc.) and 
sorting it using the counting sort

Complexity:
    O(d(n + k))
    Radix sort is high space inefficient.

"""
import random

def countingSort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    
    for i in range(0, size):
        #count of the elements
        index = arr[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        #acumulative count
        count[i] += count[i - 1]

    # sort the elements
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index%10] - 1] = arr[i]
        count[index%10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

def radixSort(arr):
    maxElement = max(arr)

    place = 1
    while maxElement // place > 0:
        # perform counting sort for each place of the elements
        countingSort(arr, place)
        place *= 10

elements = [random.randint(0,99999) for i in range(10000)]

#print(elements)

#print("--------------------------")

radixSort(elements)

#print(elements)

print("Elements have been sorted... (radix sort, 10 000 elements)")
