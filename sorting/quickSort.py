"""
This algorithm is known as divide an conquer

Time complexity:
    Worst case O(n^2)
    Best case O(n*log(n))
    Average case O(log(n))
"""
import random

def pivot(arr, leftIndex, rightIndex):
    
    pivotIndex = arr[rightIndex]

    i = leftIndex - 1

    for j in range(leftIndex, rightIndex):
        if arr[j] <= pivotIndex:
            i += 1
            
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[rightIndex] = arr[rightIndex], arr[i+1]

    return i + 1

def quickSort(arr, leftIndex, rightIndex):
    if leftIndex < rightIndex:

        #gets the pivot position
        pivIndex = pivot(arr, leftIndex, rightIndex)

        quickSort(arr, leftIndex, pivIndex - 1)
        quickSort(arr, pivIndex, rightIndex)


elements = [random.randint(0,100) for i in range(10000)]

#print(elements)

#print("---------------------------------")

quickSort(elements, 0, len(elements)-1)
#print(elements)

print('Elements have been sorted...')