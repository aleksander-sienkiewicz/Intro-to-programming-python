"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-16"
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
from functions import mow_lawn
import math
#calculations
width=int(input("Width (m): "))
length=int(input("Length (m): "))
speed=int(input("Speed (m^2/minute): "))
#call function
duration=mow_lawn(width, length, speed)
#print
print(f"Mowing the lawn takes {math.trunc(duration)} minutes.")