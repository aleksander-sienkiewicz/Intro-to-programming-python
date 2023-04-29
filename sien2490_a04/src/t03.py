"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-24"
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
from functions import product_largest
v1 = int(input("Enter the first number: "))
v2 = int(input("Enter the second number: "))
v3 = int(input("Enter the third number: "))
answer = product_largest(v1, v2, v3)
print(f"The product of the two greatest numbers entered is {answer}")