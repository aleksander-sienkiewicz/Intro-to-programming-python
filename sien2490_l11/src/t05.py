"""
-------------------------------------------------------
t05 test file
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-29"
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
from functions import words_to_matrix

martrix=words_to_matrix(["cat","dog","big"])
print("""Strings: ["cat", "dog", "big"]
Matrix of characters:

      0    1    2
 0    c    a    t
 1    d    o    g
 2    b    i    g""")