"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-18"
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
from functions import magic_date
print("Enter a date.")    
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year (2 digits): "))
dateMagic = False
function = magic_date(day, month, year)

if function == False:
    print(f"{day}/{month}/{year} is not a magic date.")
else: 
    print(f"{day}/{month}/{year} is a magic date.")