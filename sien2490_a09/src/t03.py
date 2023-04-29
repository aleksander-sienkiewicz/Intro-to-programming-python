"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-12-04"
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
from functions import file_stats
fh = open('addresses.txt', 'r', encoding='utf-8')
ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()
#prints
print(f"Uppercase letters: {ucount}")
print(f"Lowercase letters: {lcount}")
print(f"Digits: {dcount}")
print(f"Whitespace characters: {wcount}")