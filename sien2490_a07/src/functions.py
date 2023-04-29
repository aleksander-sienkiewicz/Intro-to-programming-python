"""
-------------------------------------------------------
a07 functions 
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-17"
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
def list_factors(num):
    """
    -------------------------------------------------------
    Return list of numbers factors
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num-interger(int)
    Returns:
        factors-list of factors for num
    -------------------------------------------------------
    """
    factors=[]
    for i in range(1,num):
        if num % i ==0:
            factors.append(i)
    return(factors)

#t02
def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    num=int(input("Enter a positive number: "))
    numbers=[]
    while num != 0:
        if num>0:
            numbers.append(num)
        num=int(input("Enter a positive number: "))
    return(numbers)

#t03
def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []
    for location in range(0,len(values)):
        if values[location]==target:
            locations.append(location)
    return(locations)
#t04
def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for item in subtrahend:
        common = list_indexes(minuend, item)
        for x in range(len(common)):
            minuend.remove(item)
    return(minuend)


#t05

def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    index=0
    in_order=False 
    length=len(values)
    for i in range(length):
        if values[i]-values[i-1]!=1:
            index=i-1
            in_order=False 
        else:
            index=-1
            in_order=True 
    return(in_order, index)





