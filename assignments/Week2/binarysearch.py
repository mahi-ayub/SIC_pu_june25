# Binary Search Implementation using Recursion
def binary_search(arr, target, low, high):
    if low>high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = [78,74,85,96,12,45,67,89,90,100]
arr.sort()
target = 1
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Found at index:", result)
else:
    print("Not found in the array") 

#Binary Search Implementation using Iteration
def binary_search_iterative(arr1, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1 

arr1 = [100,41,12,63,74,91,15,9,8,7]
arr1.sort()
target = 36
result1 = binary_search_iterative(arr1, target)
if result1 != -1:
    print("Found at index:", result)
else:
    print("Not found in the array") 