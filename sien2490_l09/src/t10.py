"""
-------------------------------------------------------
t10
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-15"
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
from functions import text_analyze
txt=input("Enter a string: ")
uppr,lowr,dgts,whtspc=text_analyze(txt)
print(f"upper case letters: {uppr}")
print(f"lower case letters: {lowr}")
print(f"digits: {dgts}")
print(f"whitespace characters: {whtspc}")