"""
-------------------------------------------------------
functions file a06
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-14"
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
def winner():
    """
    -------------------------------------------------------
    ask user to enter teams (Str)
    stop when empty string is entered and return ammount of times each team won
    Use: bWin, gWin
    -------------------------------------------------------
    Parameters:
        N/A
    Returns:
        bWin - #of blue wins (int)
        gWin - #of grey wins (int)
    ------------------------------------------------------
    """
    bWin = 0
    gWin = 0
    win = input("Enter the winning team: ")
    
    while win != "":
        if win== "Blue" or win =="blue":
            bWin +=1
        elif win == "Grey" or win == "grey":
            gWin +=1
        win = input("Enter the winning team: ")
    return(bWin, gWin)

#t02
def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    count1=1
    count2=0
    while count1<=num:
        if num%count1==0:
            count2+=1
        count1+=1
    if count2==2:
        result=True
    else:
        result=False
    return(result)
#t03
def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    MONTHLY_RATE=(rate/12)/100
    month=1
    print(f"principal: ${principal}")
    print(f"Interest Rate: {rate:.1f}%")
    print(f"Montly Payment: ${payment:.2f}")
    print(f"---------------------------------")
    print(f"Month  Interest  Payment  Balance")
    print(f"---------------------------------")
    while(principal>0):
        interest=MONTHLY_RATE*principal
        principal+=interest
        if principal-payment>0:
            principal-=payment
        else:
            payment=principal
            principal=0
        print(f"{month:>5} {interest:>9,.2f} {payment:>8.2f} {principal:>8,.2f}")
        month+=1
    return
#t04
def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count=0
        
    while True: 
        num /= 10
        count+=1
        if num <0 and num >-1:
            break
        if num >0 and num <1:
            break
    return (count)
#t05
def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    count=1
    total=0
    while(count!=num):
        if num%count==0:
            if num!=count:
                total+=count
        count+=1
    return(total)



