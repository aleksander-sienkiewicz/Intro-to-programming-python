"""
-------------------------------------------------------
Convert from fahrenheit to celsuis 
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-20"
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
#constant
FAHRENHEIT = 32
#input
tempC = int(input('Temperature (C): '))
#calculate temp in fahrenheit given temp in celsius
tempF = 9/5*tempC + 32
#print the determined temperature in fahrenheit

print(f'Temperature (F): {tempF} ')