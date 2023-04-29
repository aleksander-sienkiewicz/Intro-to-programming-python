"""
-------------------------------------------------------
task 1 from lab 6
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-28"
-------------------------------------------------------
"""
# Imports

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
from functions import sum_even
n = int(input(f'Enter a number: '))
total = sum_even(n)
print(f'The sum of all even numbers from 2 to {n} is: {total}')