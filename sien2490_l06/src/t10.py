"""
-------------------------------------------------------
task 10 from lab 6
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-28"
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
from functions import treadmill

burnt_per_minute = float(input("Enter calories burned per minute: "))
start = int(input("Enter beginning number of minutes: "))
end = int(input("Enter ending number of minutes: "))
inc = int(input("Enter the increment in minutes: "))
treadmill(burnt_per_minute, start, end, inc)
