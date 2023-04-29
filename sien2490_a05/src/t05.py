"""
-------------------------------------------------------
a05 t05 testing
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-05"
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
from functions import range_total

start = int(input("Start: "))
increment = int(input("Increment: "))
count = int(input("Count: "))
tot = range_total(start, increment, count)
print(f"The total is {tot} ")