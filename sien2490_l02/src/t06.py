"""
-------------------------------------------------------
calculate monthly payments for mortgage
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


#inputs
principal = int(input('Mortgage principal ($): '))
numYears = int(input('Number of years: '))
interestNum = float(input('Yearly interest rate (%): '))
interest = float(interestNum/100)
monthlyRate = float(interest/12)
numMonths = numYears*12
#calculate monthly payments using formula
monthlyPayments = principal* (monthlyRate* ( 1 + monthlyRate ) ** numMonths ) / ( ( 1 + monthlyRate ) ** (numMonths) - 1 )
#print statement stating monthly payments
print(f'The monthly payments are: ${monthlyPayments}')