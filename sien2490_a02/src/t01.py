"""
-------------------------------------------------------
calculate amount of tax on a purchase
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
#user inputs    
totalSales = float(input("Enter the total sales: $"))
#constant
TAXRATE = 0.225
#calculate tax
tax = totalSales*TAXRATE
#print statements
print("Projected Tax Report")
print("------------------------")
print(f"Total sales: $ {totalSales:.2f}")
print(f"Annual tax:  % 22.50")
print("------------------------")
print(f"Tax:         ${tax:.2f}")