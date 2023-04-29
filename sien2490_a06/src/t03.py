"""
-------------------------------------------------------
t03
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
from functions import interest_table
principal=float(input("Principal: "))
rate=int(input("Rate: "))
payment=float(input("Monthly Payment: "))
interest_table(principal, rate, payment)
