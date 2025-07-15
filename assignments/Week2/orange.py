def partition_oranges(arr):
    n = len(arr)
    pivot = arr[n - 1]
    k = 0

    for i in range(n - 1):
        if arr[i] <= pivot:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1

    arr[k], arr[n - 1] = arr[n - 1], arr[k]
    return arr

n = int(input())
arr = list(map(int, input().split()))
result = partition_oranges(arr)
print(" ".join(map(str, result)))