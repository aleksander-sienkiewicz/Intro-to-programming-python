"""
-------------------------------------------------------
print slope from two points
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-04"
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
    #imports
from functions import slope

x1=float(input("Enter first x: "))
y1=float(input("Enter first y: "))
x2=float(input("Enter second x: "))
y2=float(input("Enter second y: "))

slope=slope(x1, y1, x2, y2)
print()
print(f"The slope is {slope}")
