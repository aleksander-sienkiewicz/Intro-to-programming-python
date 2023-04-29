"""
-------------------------------------------------------
t10 test file
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
from functions import count_frequency_word
fh=open("words.txt","r")
print("file 'words.txt' open for reading")
print("Word to count: Exercise")
count=count_frequency_word(fh, "Exercise")
print(f"'Exercise' appears {count} time(s)")
fh.close()
