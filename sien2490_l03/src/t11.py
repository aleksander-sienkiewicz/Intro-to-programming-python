"""
-------------------------------------------------------
print statements with specified format
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-23"
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
location1 = "left"
location2 = "middle"
location3 = "right"

print(f"{location1:-<20s}")
print(f"{location2:-^20s}")
print(f"{location3:->20s}")