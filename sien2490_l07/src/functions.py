"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-01"
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
from math import pow
from random import randint
#t01
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    tries = 1   
    num = randint(1,high)
    guess = int(input("Guess: "))
    while guess != num:
        tries += 1
        if guess > num:
            print("Too high, try again")
            guess = int(input("Guess: "))
        elif num > guess:
            print("Too low, try again")
            guess = int(input("Guess: "))
    print(f"Congratulations - good guess!")
    print(f"You made it in {tries} guess(es)")
    return(tries)

#t02
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    count = 0
    total = 0
    while total < target:
        total = pow(2, count)
        count += 1
    if target == 0:
        total = 1
    return(total)
    

#t04
def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    count = 0 
    final=0
    while (final-target) <=0:
        final = final+(count*count)
        count += 1
    return final 
    
    

#t07
def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, aTotal = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        aTotal - all meals cost (float)
    ------------------------------------------------------
    """
    aTotal = 0
    day = 1
    print(f"For day {day}")
    print()
    breakfast = float(input("How much was breakfast? $ "))
    lunch = float(input("How much was lunch? $ "))
    supper = float(input("How much was supper? $ "))
    total = breakfast + lunch + supper
    breakTotal = breakfast 
    lunchTotal = lunch
    supperTotal = supper
    aTotal = total
    print(f"Your total for the day was ${total:.2f}")
    print()
    response = str(input("Were you way another day (Y/N)? "))
    while response == "Y":
        day += 1
        print()
        print (f"For day {day}")
        print()
        breakfast = float(input("How much was breakfast? $ "))
        lunch = float(input("How much was lunch? $ "))
        supper = float(input("How much was supper? $ "))
        total = breakfast + lunch + supper
        breakTotal += breakfast
        lunchTotal += lunch
        supperTotal += supper
        aTotal += total
        print(f"Your total for the day was ${total:.2f}")
        print()
        response = str(input("Were you away for anoder day (Y/N? "))
        
    print()
    print(f"Total:")
    print(f"Breakfast: $ {breakTotal:^10.2f}")
    print(f"Lunch:     $ {lunchTotal:^10.2f}")
    print(f"Supper:    $ {supperTotal:^10.2f}")
    return(breakTotal, lunchTotal, supperTotal, aTotal)


#t10
def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    OVERTIME = 40
    OVERTIME_RATE = 1.5
    totalPayment = 0
    numEmployees = 0
    TAX_RATE = 0.03625
    empID = 1
    while empID > 0:
        empID = int(input("Employee ID: "))
        if empID == 0:
            break
        
        wageRate = float(input("Hourly wage rate: "))
        hoursWorked = float(input("Hours worked: "))
        
        if hoursWorked > OVERTIME:
            totalWage = 40 * wageRate
            totalWage += ((hoursWorked - OVERTIME) * (wageRate * OVERTIME_RATE))
        
        else:
            totalWage = wageRate * hoursWorked
        
        totalWage = totalWage * (1 - TAX_RATE)
        totalWage = round(totalWage, 2)
        
        numEmployees += 1 
        totalPayment += totalWage
        print(f"Net payment for employee {empID}: ${totalWage:,}")
        print()
    
    avgPayment = totalPayment / numEmployees
    return(totalPayment, avgPayment)
 







