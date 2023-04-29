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
target=float(input("Enter target: "))
v1=float(input("Enter v1: "))
v2=float(input("Enter v2: "))

from functions import closest
answer = closest(target, v1, v2)

print(f"Closest value to {target} is {answer}")

    
    
    
    
    
    
    
    
    