"""
-------------------------------------------------------
task 15 from lab 6
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-28"
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
from functions import statistics
n = int(input('Enter number of values: '))
min, max, sum, avg = statistics(n)
print()
print(f"Minimum: {min:.2f}")
print(f"Maximum: {max:.2f}")
print(f"Total: {sum:.2f}")
print(f"Average: {avg:.2f}")
