"""
-------------------------------------------------------
   user imputs cost of supper lunch and breakfast, program outputs
   total cost formated correctly
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2021-09-23"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """
#inputs 
breakfast = float(input("Enter cost of breakfast: $"))
lunch = float(input("Enter cost of lunch: $"))
supper = float(input("Enter cost of supper: $"))
#calculate total cost of three items

total = breakfast + lunch + supper
#print statements for them with formatting
print(f"""
Meal        Cost""")
print (f"Breakfast   ${breakfast:6.2f}")
print(f"Lunch       ${lunch:6.2f}")
print(f"Supper      ${supper:6.2f}")
print(f"Total       ${total:6.2f}")





