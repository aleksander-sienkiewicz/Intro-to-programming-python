"""
-------------------------------------------------------
program that prompts the user for the size of the shed foundation,
height of its walls, the cost of concrete per m^3, and the cost
of bricks per m^2, and calculate and print the amount of concrete
and bricks needed, and the total cost of the materials.
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-30"
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
#user inputs
length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
height = float(input("Foundation height (m): "))
wallHeight = float(input("Wall height (m): "))
concretePrice = float(input("Cost of concrete ($/m^3): "))
bricksPrice = float(input("Cost of bricks ($/m^2): "))
#calculation for volume and cost of foundation
volume = length*width*height
costConcrete = concretePrice*volume
#calculation for surface area and cost of walls
surfaceArea = length*wallHeight*2+width*wallHeight*2
costBricks = surfaceArea*bricksPrice
#total cost calculation
totalCost = costConcrete+costBricks
#print statements
print(f"Concrete needed for foundation (m^3): {volume:.2f}")
print(f"Cost of concrete: ${costConcrete:.2f}")
print(f"Bricks needed for walls (m^2): {surfaceArea:.2f}")
print(f"Cost of bricks: ${costBricks:,.2f}")
print(f"Total Cost: ${totalCost:,.2f}")
