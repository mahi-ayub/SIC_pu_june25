num = input("Enter a number: ")
prime_digits = [2, 3, 5, 7]
count = 0

for digit in num:
    if int(digit) in prime_digits:
        count += 1

print("Number of prime digits:", count)