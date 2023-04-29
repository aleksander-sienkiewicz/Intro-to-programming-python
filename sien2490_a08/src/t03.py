"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-28"
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
from functions import common_ending
string1=input("Enter your first word to compare: ")
string2=input("Enter your second word to compare: ")
common = common_ending(string1, string2)
print(f"The common letter(s) is/are {common}")