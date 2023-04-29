"""
-------------------------------------------------------
Calculate balance that customer has to pay given principal, interest rate, 
number of years, and number of times interest is compounded

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
principal= float(input('Principal: $ '))
interest= float(input('Interest (decimal) : '))
numYears= int(input('Number of years: '))
compoundedCount= int(input('Number of times interest compounded per year: '))
#calculation for balance
balance= principal* (1+ interest/compoundedCount)**(compoundedCount*numYears)
#use round function to round to 2 decimal places, user does not want an answer with 5 decimal places
roundedBalance = round(balance,2)
#print statement
print(f'Balance: ${roundedBalance}')