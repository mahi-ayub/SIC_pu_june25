#Find biggest digit in a number
num = int(input("Enter a number: "))
max_digit = 0

for digit in str(num):
    if int(digit) > max_digit:
        max_digit = int(digit)
print("Biggest digit:", max_digit)
#Find the 2nd biggest digit in a number
num = input("Enter a number: ")  
digits = []

for digit in num:
    d = int(digit)
    if d not in digits:
        digits.append(d)

digits.sort()

if len(digits) >= 2:
    print("2nd smallest digit:", digits[1])
else:
    print("There is no 2nd smallest digit.")