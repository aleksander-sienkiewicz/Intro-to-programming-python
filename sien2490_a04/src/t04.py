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
from functions import rgb_mix
rgb1 = str(input("Enter a color (red, green, or blue): "))
rgb2 = str(input("Enter a color to add (red, green, or blue): "))
color = rgb_mix(rgb1, rgb2)

if color == "Error":
    print(color)
else:
    print(f"Adding {rgb2} to {rgb1} results in {color}")