def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr1 = [23, 1, 45, 90, 33, 12, 88, 76, 2, 11, 99, 7]       
arr2 = [1, 2, 3, 4, 6, 5, 7, 8]                             
arr3 = [100, 90, 80, 70, 60, 50]                           

for arr in [arr1[:], arr2[:], arr3[:]]:
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted:", arr)