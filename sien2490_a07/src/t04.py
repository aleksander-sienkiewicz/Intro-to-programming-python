"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-17"
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
from functions import list_positives
from functions import subtract_lists
print("Type in list (0 to stop)")
minuend= list_positives()
print("Type values to remove (0 to stop)")
subtrahend = list_positives()
newList = subtract_lists(minuend, subtrahend)
print(f"New list is {newList}")