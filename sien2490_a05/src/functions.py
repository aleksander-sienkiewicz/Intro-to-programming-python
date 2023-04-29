"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-11-05"
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
def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    factNum = 1
    for i in range (2, num + 1 ):
        factNum *= i 
        
    return(factNum)
#t02
def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    prints calories burned on treadmill in intervals of 5 min
    Use: calories_burned(perminute, minutes)
    -------------------------------------------------------
    Parameters: per_minute - cals burned per min (float)
                minutes - total num of min ran (int)
    Returns:
        None
    
    ------------------------------------------------------
    """
    print(f"calories_burned({per_minute}, {minutes})")

    for i in range(5, minutes + 1, 5):
        calories = i * per_minute
        print(f"{i:3d}:{calories:6.1f}")
    return
#t03
def open_triangle(num_rows):
    """
    -------------------------------------------------------
    prints a triangle with x amnt of rows
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters: num_rows - number of rows (int >= 1)
    
    Returns:
        None
    
    ------------------------------------------------------
    """
    for i in range(2, num_rows + 2):
        print(("#" + (" " * (i - 2) + "#")))
    return
#t04
def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"Multiplication_table({start}, {stop})")
    print("       ", end="")
    for i in range(start, stop + 1):
        print(f"{i:5d}", end="")

    print()
    dash = "-----" * (stop - start + 1)
    print(f"       {dash}")

    for i2 in range(start, stop + 1):
        print(f"{i2:5d} |", end="")

        for i3 in range(start, stop + 1):
            prod = i2 * i3
            print(f"{prod:5d}", end="")

        print()
    return
#t05
def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    tot = 0
    for i in range(start, start+(count*increment), increment):
        tot += i
    return tot








