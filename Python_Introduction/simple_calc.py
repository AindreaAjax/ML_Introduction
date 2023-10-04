# add x and y
def add(x: int, y: int):
    # it is to say that we want values for x and y to be integer but even if it's float no problem, the computation will go through
    return x + y


# subtract y from x
def subtract(x, y):
    return x - y


# multiply x and y
def multiply(x, y):
    return x * y


# divide x by y
def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return x / y


if __name__ == "__main__":
    print("3 divided by 2 is: \t", division(3, 2))
