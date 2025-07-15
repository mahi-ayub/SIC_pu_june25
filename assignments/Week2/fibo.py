n = int(input("Enter the value of n: "))
a, b = 1, 2  
if n == 1:
    print("Hemachandra term:", a)
elif n == 2:
    print("Hemachandra term:", b)
else:
    for i in range(3, n + 1):
        a, b = b, a + b
    print("Hemachandra term:", b)
