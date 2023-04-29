"""
-------------------------------------------------------
t02 test file
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
from functions import generate_matrix_char
rows=int(input("Number of rows: "))
cols=int(input("Number of columns: "))
matrix=generate_matrix_char(rows, cols)
print(matrix)