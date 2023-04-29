"""
-------------------------------------------------------
t01
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-15"
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
from functions import is_hydroxide
chemical=input("Enter your chemical: ")
isHydroxide=is_hydroxide(chemical)
if isHydroxide == True:
    print(f"{chemical} is a hydroxide")
else:
    print(f"{chemical} is not a hydroxide")