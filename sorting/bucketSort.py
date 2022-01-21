"""
Divide an unsorted array in 'buckets'
Each bucket is sorted by a suitable sorting algorithm recursively

Complexity:
    Average O(n)
    Worst O(n^2)

"""

import random

def bucketSort(arr):

    # create the buckets
    bucket = []
    for i in range(len(arr)):
        bucket.append([])

    # elements insertion on the buckets
    for j in arr:
        index = int(10*j)
        bucket[index].append(j)

    # sorting each bucket using a built-in function
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    # getting the arr sorted
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1

    return arr

elements = [random.randint(0,99)/100 for i in range(10000)]

#print(elements)

#print("----------------------------------")

elementsSorted = bucketSort(elements)

#print(elementsSorted)

print("elements have been sorted (Bucket sort, 10 000 elements)...")
