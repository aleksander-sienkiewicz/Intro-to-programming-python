"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-07"
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
from functions import multiply_fractions
numerator1=int(input("Numerator 1: "))
denominator1=int(input("Denominator 1: "))
numerator2=int(input("Numerator 2: "))
denominator2=int(input("denominator 2: "))
top, bottom, product = multiply_fractions(numerator1, denominator1, numerator2, denominator2)

print(f"Result: {top}/{bottom} = {product}")