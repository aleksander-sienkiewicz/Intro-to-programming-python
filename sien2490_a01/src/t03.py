"""
-------------------------------------------------------
convert from miles to km and display output to user
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-21"
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
#input from user
miles = float(input('Enter length in miles: '))
#calculation to convert fro miiles to km
kmlength = float(miles*1.60934)
 #print statement to display length in km to suer   
print(f'{miles} miles is equal to {kmlength} kilometres' )