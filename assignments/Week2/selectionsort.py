# Selection Sort Implementation
def selection_sort(arr):
    N = len(arr)
    for i in range(1, N):  
        element = arr[i - 1]
        position = i - 1
        for j in range(i - 1, N):  
            if arr[j] < element:
                element = arr[j]
                position = j
        arr[position], arr[i - 1] = arr[i - 1], arr[position]
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)