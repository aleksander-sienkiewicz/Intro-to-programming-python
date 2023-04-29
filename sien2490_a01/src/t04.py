"""
-------------------------------------------------------
Caculate total cost for a customer given the cost of burriots and number of burritos purchased
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
#inputs from user
cost= float(input('Cost of 1 burrito: $'))
numBurritos= int(input('Number of burritos: '))
#calculation for total cost of burritos
totalCost = cost*numBurritos
#print statement for total cost
print(f'Total cost of {numBurritos} burritos: $ {totalCost}')