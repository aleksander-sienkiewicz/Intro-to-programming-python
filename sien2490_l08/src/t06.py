"""
-------------------------------------------------------
t06
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-11"
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
from functions import list_stats
values = []
again = "y"
while again =="y":
    value = int(input("Enter a value: " ))
    values.append(value)
    print("Do you want to add nother value to the list?")
    again = input("y = yes, n = no: ")
    print()

min, max, tot, avg = list_stats(values)
print(f"Values: {values}")
print(f"Smallest value: {min}")
print(f"Largest value: {max}")
print(f"Total: {tot}")
print(f"Average: {avg}")