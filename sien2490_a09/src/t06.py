"""
-------------------------------------------------------
t06/BONUS
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
from functions import get_addresses
fh= open("addresses.txt", "r", encoding="utf-8")
getAddresses= get_addresses(fh)
fh.close()
#print
for index in getAddresses:
    print(index)