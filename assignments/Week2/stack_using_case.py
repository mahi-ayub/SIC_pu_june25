stack = []

def push():
    val = input("Enter value to push: ")
    stack.append(val)
    print(f"{val} pushed to stack.\n")

def pop():
    if stack:
        val = stack.pop()
        print(f"Popped: {val}\n")
    else:
        print("Stack is empty.\n")

def display():
    if stack:
        print("Stack (top to bottom):")
        for item in reversed(stack):
            print(item)
        print()
    else:
        print("Stack is empty.\n")

while True:
    print("Menu:\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            push()
        case '2':
            pop()
        case '3':
            display()
        case '4':
            print("Exiting program.")
            break
        case _:
            print("Invalid choice!\n")