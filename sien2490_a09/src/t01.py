"""
-------------------------------------------------------
t01
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
from functions import file_head
file = input("Enter your filename: ")
line_count = int(input("Enter your number: "))
file = open(file, "r", encoding="utf-8")
file_head(file, line_count)

file.close()