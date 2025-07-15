#Bubble Sort Implementation
def optimized_bubble_sort(arr):
    N = len(arr)
    for i in range(N - 1):  
        sorted_flag = True
        for j in range(N - 1 - i):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = False
        if sorted_flag:
            break
arr = [64, 34, 25, 12, 22, 11, 90]
optimized_bubble_sort(arr)
print("Sorted array:", arr)