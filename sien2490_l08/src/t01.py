"""
-------------------------------------------------------
t01 
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
from functions import get_weekday_name
d = int(input("Enter the number of the day of the week: "))
dayOfWeek = get_weekday_name(d)
print (f"The day of the week is {dayOfWeek}")