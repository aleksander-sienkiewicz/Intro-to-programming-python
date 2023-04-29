"""
-------------------------------------------------------
t05 test file
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
from functions import customer_append
fh = open("customers.txt","r")
fields=["94312","Brown","David","125.75","1998-06-24"]
customer_append(fh,fields)
print("data append to file")
fh.close