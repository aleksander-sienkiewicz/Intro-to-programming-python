"""
-------------------------------------------------------
print days hrs and minutes from given seconds
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
#imports
from functions import time_values

initial_seconds = int(input("Number of Seconds: "))

days,hours,minutes = time_values(initial_seconds)

print(f"{initial_seconds} is the same as:")
print(f"{days:>4} days")
print(f"{hours:>4} hours")
print(f"{minutes:>4} minutes")
