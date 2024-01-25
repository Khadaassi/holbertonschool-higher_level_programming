#!/usr/bin/python3
def print_last_digit(number):

    last_digit = abs(number)
    while last_digit >= 10:
        last_digit //= 10
    
    # Print the last digit
    print(last_digit, end="")
    
    # Return the value of the last digit
    return last_digit
