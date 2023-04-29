"""
-------------------------------------------------------
t01 test file
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
from functions import generate_matrix_num
rows = int(input("Number of rows: "))
cols=int(input("Number of columns: "))
low=int(input("Low value: "))
high=int(input("High value: "))
value_type=input("Type of values: ")
matrix=generate_matrix_num(rows,cols,low,high,value_type)
print(matrix)