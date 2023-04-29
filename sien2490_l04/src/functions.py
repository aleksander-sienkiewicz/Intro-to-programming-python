"""
-------------------------------------------------------
functions library
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-04"
-------------------------------------------------------
"""

#t01 function
def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diamater of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
     Parameters:

        radius - radius of a circle (float>=0)
    Returns:
        diam - diameter of a circle (float))
    -------------------------------------------------------
    """
    diam = radius*2
    return(diam)

#t04 function
def square_pyramid(base, height):
    """
    --------------------------------------------------------
    Calculates and returns the slant height, area, and volume of a square based pyramid given the base and perpendicular height.
    Use: sh, area, vol = square_pyramid(base, height)
    --------------------------------------------------------
    Parameters:
        base - length of the base pyramid (float > 0)
        height - perpenducular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        col - volume of the square pyramid (float)
    --------------------------------------------------------
    """
    import math
    ph = height
    sh = (((base/2)**2+ph**2))**0.5
    area = base**2+2*base*math.sqrt(base**2/4+ph**2)
    vol = (base**2)*(ph/3)
    return(sh,area,vol)
#t07 function
def total_change(nickels,dimes,quarters,loonies,toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """

    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.10
    QUARTER_VALUE = 0.25
    LOONIE_VALUE = 1
    TOONIE_VALUE = 2

    total_nickels = nickels * NICKEL_VALUE
    total_dimes = dimes * DIME_VALUE
    total_quarters= quarters * QUARTER_VALUE
    total_loonies= loonies * LOONIE_VALUE
    total_toonies= toonies * TOONIE_VALUE

    total = total_nickels+total_dimes+total_quarters+total_loonies+total_toonies

    return(total)


#t11 function
def slope(x1,y1,x2,y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: slp = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        slp - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """
    slp = (y2-y1)/(x2-x1)
    return(slp)

#t14 function
def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    ----------------------------------------
    """
    DAY_SECONDS=86400
    HOURS_SECONDS = 3600
    MINUTES_SECONDS=60
    
    days = seconds//DAY_SECONDS
    hours= seconds//HOURS_SECONDS
    minutes= seconds//MINUTES_SECONDS

    return(days,hours,minutes)
    