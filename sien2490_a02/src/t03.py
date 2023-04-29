"""
-------------------------------------------------------
program asks for an int that represents the date in format MMDDYYYY
and then prings in the format YYYY/MM/DD
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-30"
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
#input
dateinpt=int(input("Enter a date in the format MMDDYYYY: "))
#seperate the digits
year = dateinpt%10000
day = dateinpt%1000000//10000
month = dateinpt//1000000
#print statements
print(f"The reformated date: {year}/{month}/{day}")
