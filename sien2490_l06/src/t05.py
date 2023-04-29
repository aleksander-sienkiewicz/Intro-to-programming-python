"""
-------------------------------------------------------
task 5 from lab 6
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-28"
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
from functions import draw_rectangle
h = int(input("Enter height in characters: "))
w = int(input("Enter width in characters: "))
c = str(input("Enter the draw characters: "))
draw_rectangle(h, w, c)