#find sum of array elements using recursion

def sum_array(arr, n):
    if n <= 0:
        return 0
    else:
        return arr[n - 1] + sum_array(arr, n - 1)

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    if len(arr) != n:
        print("Error: The number of elements does not match the specified size.")
    else:
        print("The sum of the array elements is:", sum_array(arr, n))
