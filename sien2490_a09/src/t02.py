"""
-------------------------------------------------------
t02
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
from functions import file_integers
fh = open('numbers.txt', 'r', encoding='utf-8')
numbers = file_integers(fh)
fh.close()
#prints
print(type(numbers))
print(type(numbers[0]))
print(f"Numbers: {numbers}")