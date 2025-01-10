# Write a Python program to assign a default value to a variable and change it if the user inputs a new value.

x = 5  # default value
x = int(input(f"Enter a new value (default is {x}): ") or x)
print(f"Value of x: {x}")