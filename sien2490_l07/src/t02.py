"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-01"
-------------------------------------------------------
"""
# Imports
from _pydecimal import _dpower

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """
from functions import power_of_two
target = int(input("Enter target number: "))
total = power_of_two(target)
print(f"The closest power of 2 greater than equal to {target} is {total}")