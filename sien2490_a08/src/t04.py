"""
-------------------------------------------------------
t04
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
from functions import is_valid_isbn
isbn=input("Enter ISBN: ")
valid = is_valid_isbn(isbn)
if valid == True:
    print(f"{isbn} is valid")
else:
    print(f"{isbn} is not valid")