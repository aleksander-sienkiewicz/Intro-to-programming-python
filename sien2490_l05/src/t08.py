"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-18"
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

number=int(input("Enter a number from 1 to 10: "))
from functions import roman_numeral
result = roman_numeral(number)
if result=="Error":
    print("Error")
else:
    print(f"The roman numeral equivalent of {number} is {result}")


















