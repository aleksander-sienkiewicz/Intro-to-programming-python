"""
-------------------------------------------------------
t13 test file
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-26"
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
from functions import file_copy
fh_1 = open("words.txt")
fh_2 = open("new_words","w")
file_copy(fh_1, fh_2)
print("Copying 'words.txt' to 'new_words.txt'")
fh_1.close()
fh_2.close()
