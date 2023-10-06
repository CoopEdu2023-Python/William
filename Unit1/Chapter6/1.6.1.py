def add(x, y):
    print("Addition result:", x+y)
    return x+y


def subtract(x, y):
    print("Subtraction result:", x-y)
    return x-y


def multiply(x, y):
    print("Multiplication result:", x*y)
    return x*y


def divide(a, b):
    if b != 0:
        result = a / b
        print("Division result:", result)
    else:
        print("Division by zero error.")


add(5, 10)
subtract(20, 10)
multiply(10, 5)
divide(100, 0)

