"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-10-24"
-------------------------------------------------------
"""
# Imports

# Constants


#t01
def day_of_week(day_number):
    """
    -------------------------------------------------------
    uses day number to return the day of the week. Return error if not from 1-7
    Use: day=day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
       day_number = int 1-7
    Returns:
         day - day of the week
    ------------------------------------------------------
    """
    if day_number == 1:
        dayName = "Monday"
    elif day_number == 2:
        dayName = "Tuesday"
    elif day_number == 3:
        dayName = "Wednesday"
    elif day_number == 4:
        dayName = "Thursday"
    elif day_number == 5:
        dayName = "Friday"
    elif day_number == 6:
        dayName = "Saturday"
    elif day_number == 7:
        dayName = "Sunday"
    else:
        dayName = "Error"
    return dayName
#t02
def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if aqi<0:
        pol = "Error"
    elif aqi >= 300:
        pol = "Hazardous"
    elif aqi>= 201:
        pol = "Very Unhealthy"
    elif aqi>= 151:
        pol = "Unhealthy"
    elif aqi >= 101:
        pol = "Unhealthy for Sensitive Groups"
    elif aqi >= 51:
        pol = "Moderate"
    else:
        pol = "Good"
    
    return pol

#t03
def product_largest(v1,v2,v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1>v2 and v2>v3:
        answer = v1* v2
    elif v3>v1 and v2>v1:
        answer = v2*v3
    else:
        answer = v3*v1
    
    return answer


#t04
def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if rgb1 == "blue" and rgb2 == "red" == "blue" or rgb1 == "blue" and rgb2 == "red":
        color = "fuchsia"
    elif rgb1 == "green" and rgb2 == "blue" or rgb1 == "blue" and rgb2 == "green":
        color = "aqua"
    elif rgb1 == "red" and rgb2 == "green" or rgb1 == "green" and rgb2 == "red":
        color = "yellow"
    elif rgb1 == rgb2:
        color = rgb1
    else:
        color = "Error"
    return color
#t05
def yee_ha(number):
    """
    -------------------------------------------------------
    yee_ha takes an integer parameter and returns one of the following strings:
    "Yee" if number is evenly divisible by 3
    "Ha" if number is evenly divisible by 7
    "Yee Ha" if number is evenly divisible by both 3 and 7
    "Nada" if number is none of the above
    Use: text = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - int
    Returns:
        text - text (str)
    -------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 == 0:
        text = "Yee Ha"
    elif number % 3 == 0:
        text = "Yee"
    elif number % 7 == 0:
        text = "Ha"
    else:
        text = "Nada"
    return text
        
        
        
        