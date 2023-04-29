"""
-------------------------------------------------------
functions module//lab 6
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-29"
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
def sum_even(n):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range (2,n+1,2):
        total+= i
    
    return total

#t05
def draw_rectangle(h, w, c):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, h+1):
        print(f"{c*w}")
    return 


#t09
def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(n,2,-1):
        print(f"""{i} bottles of beer on the wall, {i} bottles of beer.
Take one down pass it around, {i-1} bottles of beer on the wall.""")
        print('--')
    print(f"""2 bottles of beer on the wall, 2 bottles of beer.
Take one down pass it around, 1 bottles of beer on the wall.""")
    print('--')
    print(f"""1 bottles of beer on the wall, 1 bottles of beer.
Take one down pass it around, no more bottles of beer on the wall.""")
    
    return 


#t10
def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(start, end + 1, inc):
        calories = burnt_per_minute*i 
        print(f"Calories burned after {i} minutes: {calories:.1f}")
    return 



#t15
def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    firstv = float(input("First Value: "))
    min = firstv
    max = firstv
    sum = firstv
    for i in range(n-1):
        nextv = float(input("Next Value: "))
        sum += nextv
        if nextv>max:
            max = nextv
        elif nextv < min:
            min = nextv
    avg = sum / n 
    return min, max, sum, avg 















