x = 10  # Global variable

def function():
    y = 20  # Local variable
    print(x, y)

function()
# print(y)  # This will cause an error because y is local to function()
