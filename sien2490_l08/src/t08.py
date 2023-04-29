"""
-------------------------------------------------------
t08
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
from functions import linear_search
a = []
again = "y"
while again =="y":
    value = int(input("Enter a value: " ))
    a.append(value)
    print("Do you want to add nother value to the list?")
    again = input("y = yes, n = no: ")
    print()
v = int(input("Value: "))
index = linear_search(a, v)
print(f"Values: {a}")
print("")
print(f"Index of {v}: {index}")