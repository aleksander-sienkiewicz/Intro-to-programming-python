"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-16"
-------------------------------------------------------
"""
# Imports
from random import randint

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
#constant
ACRE=43,560
#t01 function
def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    numAcres = square_footage/43560
    return numAcres
#t02 function
def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    squareFootage=width*length 
    duration=squareFootage/speed
    return duration
#t03 function
def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    #seperate the digits
    year = date_number%10000
    day = date_number%1000000//10000
    month = date_number//1000000
    #print statements
    return year, month, day

#t04
def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    top=num1*num2
    bottom=int(denom1)*int(denom2)
    product=top/bottom
    return top, bottom, product
#t05 function
def math_quiz():
    """
    -------------------------------------------------------
    Displayes two numbers two add, user types in an answer and program outputs correct answer
    Use: num1,num2,userAnswer,expected
    -------------------------------------------------------
    Parameters:
        num1 - int 0,999
        num2 - int 0,999
    Returns:
         Print num1 - first number in operation
         Print num2 - number to be added to frist
         Print userAnswer - user answer
         Print expected - expected answer
    ------------------------------------------------------
    """
    num1= randint(0,999)
    num2= randint(0,999)
    print(f"{num1:>5}")
    print(f"+{num2:>4}")
    print()
    userAnswer=int(input("Your answer: "))
    print()
    print(f"Your answer:  {userAnswer:>3}")
    expected=num1+num2
    print(f"Expected: {expected:>7}")
    return
    
    
    
    
    
    
    
    
    