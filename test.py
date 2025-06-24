import tkinter as tk

count = 0

def increment():
    global count
    count += 1
    label.config(text=f"Clicked: {count} times")

root = tk.Tk()
root.title("Click Counter")

label = tk.Label(root, text="Clicked: 0 times", font=("Arial", 72))
label.pack(pady=10)

button = tk.Button(root, text="Click Me!", command=increment, font=("Arial", 14))
button.pack(pady=10)

root.mainloop()
