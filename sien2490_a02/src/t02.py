"""
-------------------------------------------------------
Take an input int and calculate the difference of the two digits
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
#inputs
number =int(input("Enter a positive digit number: "))
#seperate two digits with // and % opperators
firstDigit = number//10
secondDigit = number%10
#calculate difference
difference = firstDigit - secondDigit
#print statements
print(f"The difference of the digits of {number} is {difference}")