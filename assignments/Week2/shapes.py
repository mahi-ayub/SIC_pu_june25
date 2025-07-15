def right_angled_triangle(n):
    print("\nA. Right Angled Triangle")
    for i in range(1, n + 1):
        print('*' * i)

def equilateral_triangle(n):
    print("\nB. Equilateral Triangle")
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

def hollow_square(n):
    print("\nC. Hollow Square")
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

def hollow_rhombus(n):
    print("\nD. Hollow Rhombus")
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def pascals_triangle(n):
    print("\nE. Pascal's Triangle")
    for i in range(n):
        print(' ' * (n - i), end='')
        num = 1
        for j in range(i + 1):
            print(num, end=' ')
            num = num * (i - j) // (j + 1)
        print()

def x_shape(n):
    print("\nF. X Shape")
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def x_in_hollow_square(n):
    print("\nG. X Shape inside Hollow Square")
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or j == i or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def benzene_ring(n):
    print("\nH. Benzene Ring (Hexagon)")
    width = n
    space = n
    print(' ' * space + '/' + '-' * width + '\\')
    for i in range(n):
        print(' ' * (space - i - 1) + '/' + ' ' * (width + 2 * i + 1) + '\\')
    for i in range(n):
        print(' ' * i + '\\' + ' ' * (width + 2 * (n - i - 1) + 1) + '/')
    print(' ' * space + '\\' + '-' * width + '/')

n = int(input("Enter number of lines (min 3 recommended): "))

right_angled_triangle(n)
equilateral_triangle(n)
hollow_square(n)
hollow_rhombus(n)
pascals_triangle(n)
x_shape(n)
x_in_hollow_square(n)
benzene_ring(n)

