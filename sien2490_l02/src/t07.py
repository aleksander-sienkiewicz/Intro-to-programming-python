"""
-------------------------------------------------------
calculate number of flyers per volunteer and number of flyers left over
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
numFlyers = int(input('Number of flyers: '))
numVolunteers = int(input('Number of volunteers: '))
#calculate number of flyers per volunteer and left overs using // and % opterators respectevly
flyersPerVolunteer = numFlyers // numVolunteers
excessFlyers = numFlyers % numVolunteers
#print to user 

print(f'Flyers per volunteer: {flyersPerVolunteer}')
print(f'Flyers left over: {excessFlyers}')