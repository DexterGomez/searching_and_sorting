"""
Uses binary trees to perform the sorting.
Heapify is the process to adjust the positions of the
elements by their position with their root.

Complexity:
    For all cases heap sort is O(n*log(n))
"""
import random

def heapify(arr, arrLength, i):

    # define the father element and their child
    largestElement = i
    left = 2*i + 1
    right = 2*i + 2

    # check if the child are greater than the father
    if left < arrLength and arr[i] < arr[left]:
        largestElement = left

    if right < arrLength and arr[largestElement] < arr[right]:
        largestElement = right

    # if father is not the lagerst element then swap position with it
    # then heapify the tree again
    if largestElement != i:
        arr[i], arr[largestElement] = arr[largestElement], arr[i]
        heapify(arr, arrLength, largestElement)

def heapSort(arr):
    length = len(arr)

    # built the heap
    for i in range(length//2, -1, -1):
        heapify(arr, length, i)
    
    # swap and heapify the root
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)



elements = [random.randint(0,999) for i in range(10000)]

#print(elements)
#print("--------------------")

heapSort(elements)

#print(elements)
print("Elements have been sorted...")
