"""
-------------------------------------------------------
t02
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-14"
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
from functions import is_prime
num=int(input("Enter a number: "))
result = is_prime
if result == True:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")