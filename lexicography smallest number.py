# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:57:27 2024

@author: Nicholas
"""

def smallest_number(num):
    # Convert the number to a string and handle negative numbers
    is_negative = num < 0
    num_str = str(abs(num))
    
    # Sort the digits
    sorted_digits = sorted(num_str)
    
    # Find the first non-zero digit
    first_non_zero = next(i for i, digit in enumerate(sorted_digits) if digit != '0')
    
    # Construct the result
    if first_non_zero == 0:
        # If there are no leading zeros, just join the sorted digits
        result = ''.join(sorted_digits)
    else:
        # Place the first non-zero digit at the beginning
        result = sorted_digits[first_non_zero] + ''.join(sorted_digits[:first_non_zero] + sorted_digits[first_non_zero+1:])
    
    # Add the negative sign back if the original number was negative
    if is_negative:
        result = '-' + result
    
    return int(result)

# Test cases
print(smallest_number(310))  # Output: 103
print(smallest_number(-310))  # Output: -103
print(smallest_number(1000))  # Output: 1000
print(smallest_number(-1000))  # Output: -1000
print(smallest_number(10400))  # Output: 10004
print(smallest_number(-10400))  # Output: -10004
