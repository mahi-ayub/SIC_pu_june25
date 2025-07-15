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

def exit_program():
    print("Exiting program.")
    exit()

def invalid():
    print("Invalid choice!\n")

menu = {
    '1': push,
    '2': pop,
    '3': display,
    '4': exit_program
}

while True:
    print("Menu:\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter your choice: ")
    menu.get(choice, invalid)()
