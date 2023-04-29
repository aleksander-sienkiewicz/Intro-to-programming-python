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
#t01
def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    if day*month == year:
        dateMagic = True
    else:  
        dateMagic = False
    return dateMagic
#t04
def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    if abs(target-v1)>abs(target - v2):
        closerNum=v2
    else:
        closerNum=v1
    return closerNum
    
        
    
#t08
def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    if (n == 1):
        result= "I"
    elif (n == 2):
        result ="II"
    elif (n ==3): 
        result ="III"
    elif (n==4):
        result ="IV"
    elif (n==5):
        result ="V"
    elif (n==6):
        result ="VI"
    elif (n ==7):
        result ="VII"
    elif (n == 8):
        result ="VIII"
    elif (n ==9):
        result ="IX"
    elif (n == 10):
        result ="X"
    else:
        result ="Error"
    
    return result
    
#t12
def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    FT_TEN_YEARS = 0.05
    FT_LESS_FOUR_YEARS = 0.015
    PT_TEN_YEARS = 0.03
    PT_LESS_FOUR_YEARS = 0.01
    OTHER = 0.02
    if status == "F":
        if years >=10:
            raisePercent = FT_TEN_YEARS
        elif years <4:
            raisePercent = FT_LESS_FOUR_YEARS
        else:
            raisePercent = OTHER
    elif status == "P":
        if years >= 10:
            raisePercent = PT_TEN_YEARS
        elif years <4:
            raisePercent = PT_LESS_FOUR_YEARS
        else:
            raisePercent = OTHER
    else: 
        raisePercent = OTHER
    newSalary = salary * ( 1 + raisePercent)
    return newSalary
    
    
    

#t14
def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    ADULT = 18
    INFANT = 3
    SENIOR = 65
    STUDENT = 18
    KID = 10
    age = int(input("How old are you? "))
    if age >= SENIOR:
        price = 4.00
    elif age >= STUDENT and age < SENIOR:
        price = 5.00
    elif age >= KID and age < STUDENT:
        askQ = input("Are you a student at this school? (Y/N): ")
        if askQ == "Y":
            price = 1.00
        else:
            price = 3.00
    elif age >= INFANT and age < KID:
        price = 2.00
    else:
        price = 0.00
    return price
