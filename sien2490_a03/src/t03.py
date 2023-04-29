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
from functions import date_extract
date_number= int(input("Enter a date in the format MMDDYYYY: "))
year, month, day = date_extract(date_number)
print(f"The reformatted date is {year}/{month}/{day}")