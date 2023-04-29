"""
-------------------------------------------------------
user inputs cost and percent discount and program outputs what was discounted off 
the cost formated correctly
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-23"
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
    # inputs from user
price = float(input("Enter number: "))    
discountPercent = float(input("Enter percent: "))
percentAsNumber = discountPercent/100 
discount = price * percentAsNumber
#print statement
print(f"A {discountPercent} discount on {price} is {discount:.1f}")

# I dont think $ or % is necessary for this question since it was not in the example
# if it is to be included i would write:
#print(f"A {discountPercent}% discount on ${price} is ${discount:.1f}")
