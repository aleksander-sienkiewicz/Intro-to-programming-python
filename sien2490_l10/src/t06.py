"""
-------------------------------------------------------
t06 test file
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-26"
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
from functions import number_stats
fh=open("customers.txt","r")
smallest,largest,total,average=number_stats(fh)
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")
fh.close()
