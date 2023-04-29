"""
-------------------------------------------------------
program to calculate the BMI (Body Mass Index) and BMI' (BMI Prime) for a user.
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-21"
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
#inputs
height= float(input('Enter your height (m): '))
mass= float(input('Enter your weight(kg): '))
upperLimit= int(input('Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): '))
#calculations for bmi and bmi'
bmi= float(mass/(height**2))
bmiPrime= float(bmi/upperLimit)
#print bmi and bmi' to user
print(f'Body Mass Index (kg/m^2) = {bmi}')
print(f'BMI Prime = {bmiPrime}')