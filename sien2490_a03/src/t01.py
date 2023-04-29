"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-16"
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
#import 
from functions import feet_to_acres
sqrfootage=float(input("square footage: "))
print()
solution=feet_to_acres(sqrfootage)
print(f"{solution:.2f} acres is equivalent to {sqrfootage:,.2f} square feet")