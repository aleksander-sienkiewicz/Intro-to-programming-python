"""
-------------------------------------------------------
t04
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-11"
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
from functions import generate_integer_list
n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))
values = generate_integer_list(n, low, high)
print(values)