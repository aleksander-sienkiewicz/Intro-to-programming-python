"""
-------------------------------------------------------
a08 functions file
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-28"
-------------------------------------------------------
"""
# Imports
from pickle import TRUE

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
def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    count = 0
    newString=""
    for index in string:
        if index.isupper():
            if count==0:
                count+=1
                newString+=index
            else:
                newString= newString+" "+index.lower()
        else:
            newString+=index
    return(newString)
#t02
def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    if string[-1]=="s" or string[-2:]=="sh" or string[-2:]=="ch":
        string+="es"
    elif string[-2:]=="oy":
        string+="s"
    elif string[-2:]=="ay":
        string+="s"
    elif string[-1]=="y":
        string=string[:-1]+"ies"
    else:
        string+="s"
    plural=string
    return(plural)
#t03
def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    common = ""
    num=len(string1)-1
    letter=string1[num:]
    while num>=0 and string2.endswith(letter):
        common=letter 
        num-=1
        letter=string1[num:]
    return(common)
#t04
def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True 
    counter=0
    while(counter<len(isbn)-1):
        if isbn[counter] !="" and isbn[counter].isdigit()!=True:
            valid=False 
        counter+=1
    if len(isbn)!=17:
        valid=False 
    if isbn[len(isbn)-1].isdigit()==False and isbn[len(isbn)-2]!="-":
        valid=False 
    dash=isbn.split('-')
    for index in range(5):
        if dash[index].isdigit()==False:
            valid=False 
    if dash[0]!="978" and dash[0]!="979":
        valid=False
    return(valid)
#t05
def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain=True 
    for index in range(len(word_list)-1):
        list1=word_list[index]
        list2=(word_list[index+1])
        
        if list1[len(list1)-1]!=list2[0]:
            word_chain=False 
    
    return(word_chain)







