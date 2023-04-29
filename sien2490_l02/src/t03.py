"""
-------------------------------------------------------
calculate daily earnings for grooming services given number of small and large dogs groomed 
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
#constants
LARGEDOGS = 75
SMALLDOGS = 50
#inputs
numLarge = int(input('Number of large dogs groomed: '))
numSmall = int(input('Number of small dogs groomed: '))
#calculate total earned using $75 for large dogs and $50 for small
totalEarned = (numLarge*LARGEDOGS)+(numSmall*SMALLDOGS)
#print total earned that day
print(f'Total earned for the day: ${totalEarned}')