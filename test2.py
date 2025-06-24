def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

try:
    num = int(input("Enter a number: "))
    print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")
except ValueError:
    print("Invalid input.")
