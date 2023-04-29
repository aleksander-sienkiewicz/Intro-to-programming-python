"""
-------------------------------------------------------
t05
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
from functions import matrix_rotate_right
matrix= [[1, 2, 9], [8, 7, 12], [4, 2, 0]]
rotatedMatrix= matrix_rotate_right(matrix)
#print
print(f"Original matrix is: {matrix}")
print(f"Rotated matrix is: {rotatedMatrix}")