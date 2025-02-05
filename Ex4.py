def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


print(add(5, 3))  
print(subtract(5, 3))  
print(multiply(5, 3))  
print(divide(5, 3))  
