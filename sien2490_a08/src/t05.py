"""
-------------------------------------------------------
t05
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-28"
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
from functions import is_word_chain
word_list = ["camel","leopard","dog","giraffe","elephant"]
word_chain=is_word_chain
print(f"The list of words is {word_list}")
print()
if word_chain==True:
    print("It is a word chain")
else:
    print("It is not a word chain")