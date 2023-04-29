"""
-------------------------------------------------------
calculate slant height, area and volume
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
#import function
from functions import (square_pyramid)
#inputs
base=float(input("Length of base: "))
height=float(input("Perpendicular height of pyramid: "))

sh,area,vol=square_pyramid(base, height)
#outputs
print(f"Slant height of square pyramid: {sh:.2f}")
print (f"Area of square pyramid: {area:.2f}")
print(f"Volume of square pyramid: {vol:.2f}")
