"""
-------------------------------------------------------
[print diameter from radius]
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
from functions import diameter
#inputs
radius=float(input("Enter radius: "))
#TODO call function
diam = diameter(radius)
#outputs
print()
print(f"Diameter of a circle: {diam:.2f}")
