# Fuel problem
# author: jguerreiro

"""
    Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
    For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

    In a file called fuel.py, implement a program that prompts the user for a fraction, 
    formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, 
    how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
    And if 99% or more remains, output F instead to indicate that the tank is essentially full.

    If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
    (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

def fraction_to_percentage(user_fraction):
    expression_list = list(user_fraction)

    dividend = int(expression_list[0])
    divisor = int(expression_list[2])

    fraction = (dividend / divisor) * 100

    # Remove decimal ex: 50.0 -> 50
    result = int(fraction)

    if result == 100:
        print("F")
    elif result == 0:
        print("E")
    else:
        print(f"{result}%")

# Read fraction as X / Y
fraction = "0/4" #input("Fraction: ")

fraction_to_percentage(fraction)

# TODO's:
# Validation: X or Y is not an integer, X is greater than Y, or Y is 0
# Catch exceptions:  ValueError or ZeroDivisionError