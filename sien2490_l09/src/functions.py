"""
-------------------------------------------------------
functions
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-15"
-------------------------------------------------------
"""
# Imports
from pickle import TRUE, FALSE

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
#t01
def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    if chemical.endswith("OH"):
        isHydroxide=True
    else:
        isHydroxide=False
    return isHydroxide
#t03
def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc=""
    pi=""
    pq=""
    for index in range(len(product_code)):
        if index<3:
            pc+=product_code[index]
        elif index<7:
            pi+=product_code[index]
        else:
            pq+=product_code[index]    
    return(pc,pi,pq)
#t04
def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    pc=""
    pi=""
    pq=""
    for index in range(len(product_code)):
        if index<3:
            pc+=product_code[index]
        elif index<7:
            pi+=product_code[index]
        else:
            pq+=product_code[index]
    if pc.isupper()and len(pc)==3:
        print(f"Category {pc} is valid.")
    else:
        print(f"Category {pc} is not valid.")
    if pi.isdigit() and len(pi)==4:
        print(f"ID {pi} is valid.")
    else:
        print(f"ID {pi} is not valid.")
    if len(pq)>0:
        if pq[0].isupper():
            print(f"Qualifier {pq} is valid.")
        else:
            print(f"Qualifier {pq} is not valid.")
    else:
        print(f"Qualifier {pq} is not valid.")
    
    return 
#t05
def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    for index in password:
        if index.isdigit():
            digits=True
        else:
            digits=False 
        if index.islower():
            lower=True 
        else:
            lower=False
        if index.isupper():
            upper=True 
        else:
            upper=False 
    if len(password)>8:
        longEnough=True 
    else:
        longEnough=False 
    print()
    if longEnough==False:
        print("not long enough")
    if digits == False:
        print("no digits")
    if upper==False:
        print("no upper case")
    if lower == False:
        print("no lower case")
    return
#t10
def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr=0
    lowr=0
    dgts=0
    whtspc=0
    for index in txt:
        if index.isupper():
            uppr+=1
        elif index.islower():
            lowr+=1
        elif index.isnumeric():
            dgts+=1
        elif index.isspace():
            whtspc+=1
            
    return(uppr,lowr,dgts,whtspc)





