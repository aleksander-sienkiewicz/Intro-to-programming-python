"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-15"
-------------------------------------------------------
"""
# Imports
from itertools import product

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
from functions import parse_code
product_code=input("Enter a product code: ")
pc,pi,pq=parse_code(product_code)
print(f"Category:{pc:>6}")
print(f"ID: {pi:>11}")
print(f"Qualifier: {pq:>4}")