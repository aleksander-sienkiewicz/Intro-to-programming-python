"""
-------------------------------------------------------
a05 t01 testing
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-05"
-------------------------------------------------------
"""
# Imports
from functions import factorial

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
num = int(input("Enter your number: "))
factNum = factorial(num)
print(f"{num}! is equivalent to {factNum}")