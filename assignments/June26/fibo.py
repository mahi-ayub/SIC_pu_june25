n = int(input("Enter the value of n: "))
a, b = 1, 2  

if n == 1:
    print("Fibonacci term:", a)
elif n == 2:
    print("Fibonacci term:", b)
else:
    for i in range(3, n + 1):
        a, b = b, a + b
    print("Fibonacci term:", b)