"""The Sys module""" 

# The `sys` module has a vast array of functions. But we usually use the `sys.argv`, `sys.exit` and maybe sometimes `sys.stdin`, `sys.stdout` functions too. You can read the documentation at - https://docs.python.org/3/library/sys.html"""

"sys.argv"

# This is mainly useful when we are to execute a script and we know that the user will provide some input in the command line along with the script name before hitting Enter i.e, running the script itself. Thus, we need to store the inputs that the user gives so that we can use them to manipulate our program.

# Actually, when we write a script we expect the user to provide some input along with the script name in order to have access to a specific feature.

# `sys.argv` is the list of command line arguments passed to a Python script. Usually `sys.argv[0]` stores the script name.

import sys

# summing user inputted values
def sum_of_numbers():
    sum_till_now = 0
    for num in sys.argv[1:]:
        sum_till_now += int(num)
    print(sum_till_now)
    
# sum_of_numbers()



"sys.exit"

# say we want to exit the script execution prematurely that is to say, in the middle of the program. 
# For example, if we get a string character that can't be converted to an integer number we would like to exit the execution and ask the user to input only integer numbers. Let's do that -

# redefining the sum_of_numbers() function
def sum_of_numbers():
    sum_till_now = 0
    for num in sys.argv[1:]:
        try:
            sum_till_now += int(num)
        except: 
            sys.exit("Please provide valid inputs (Integers only).")
    
print("Sum =  ", sum_of_numbers())