# Factorial Calculator

fact_res_one = [0, 1]

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x in fact_res_one:
        return 1
    else:
        return (x * factorial(x-1))

if __name__ == "__main__": print("The main module.")
