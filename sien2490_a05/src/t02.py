"""
-------------------------------------------------------
a05 t02 testing
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
from functions import calories_burned
per_minute = float(input("Enter calories burned per minute: "))
minutes = int(input("Enter time on treadmill: "))
calories_burned(per_minute, minutes)