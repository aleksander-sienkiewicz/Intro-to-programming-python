"""
-------------------------------------------------------
ask for number of children and balloons and divides them
program will display how many balloons each child receives 
and left over balloons
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
numBalloons = int(input("Number of balloons: "))
numChildren = int(input("Number of children: "))
balPerChild = numBalloons//numChildren
leftovers = numBalloons%numChildren
print(f"Each child receives {balPerChild} balloons")
print(f"Balloons that won't be distributed: {leftovers}")