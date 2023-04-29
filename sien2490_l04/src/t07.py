"""
-------------------------------------------------------
print change form number of coins
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-04"
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
#imports
from functions import total_change
#constants

nickels=int(input("Enter number of nickels: "))
dimes=int(input("Enter number of dimes: "))
quarters=int(input("Enter number of quarters: "))
loonies=int(input("Enter number of loonies: "))
toonies=int(input("Enter number of toonies: "))

total=total_change(nickels,dimes,quarters,loonies,toonies)
print()
print(f"Total amount: ${total:.2f}")
