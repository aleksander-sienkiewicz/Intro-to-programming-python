"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-18"
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
from functions import pay_raise
eStatus = str(input("Status: "))
eYears = float(input("Years: "))
eSalary = float(input("Salary: "))
printSalary = pay_raise(eSalary, eYears, eSalary)
print(f"New Salary: ${printSalary:,.2f}")