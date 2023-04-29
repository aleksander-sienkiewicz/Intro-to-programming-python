"""
-------------------------------------------------------
t04
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
from functions import flatten
matrix = [[1, 2, 9], [8, 7, 12], [4, 2, 0]]
flatMatrix = flatten(matrix)
#print
print(f"Original matrix is: {matrix}")
print(f"Flattened matrix is: {flatMatrix}")