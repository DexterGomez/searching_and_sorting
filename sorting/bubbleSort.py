"""
This method iterate the elements and check if n element is greater than n+1
if it is true then it swap the elements. The algorithm repeats the action
until the array is complete ordened.

Time complexity:
    Worst case O(n^2)
    Best case O(n)
    Average case O(n^2)
"""
import random


def bubbleSort(arr):
    """
    Gets an array and sort their elements
    """
    m = len(arr)

    # goes through the elements of the array
    for u in range(m):

        # goes through the array from the 0th element to the m-u-1 element
        for v in range(0, m-u-1):

            # swap the elements if it is greater than the next
            if arr[v] > arr[v+1] :
                aux = arr[v]
                arr[v] = arr[v+1]
                arr[v+1] = aux

    return arr

elements = [random.randint(0,100) for i in range(10000)]

#print(elements)

#print("------------------------------------")

r = bubbleSort(elements)
#print(r)

print('Elements have been sorted...')