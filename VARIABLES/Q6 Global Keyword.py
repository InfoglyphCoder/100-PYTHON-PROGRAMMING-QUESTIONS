# 6. What is the global keyword in Python?

print("The global keyword allows a function to modify a variable,\n that is defined outside of its scope (i.e., in the global scope).")

# Example:
x = 10 # Global variable
def myfunc():
  global x
  x = 5 # Local variable
myfunc()