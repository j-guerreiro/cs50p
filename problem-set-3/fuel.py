# Fuel problem
# author: jguerreiro
# Regarding exceptions this helped -> https://stackoverflow.com/questions/62062226/how-to-work-with-try-and-except-in-python

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

def transform_input(input):
    input_list = list(input)
    input_values = []

    for inputs in input_list:
        if inputs != '/':
            input_values.append(inputs)

    return input_values

def validator(user_input):
    value_error = True
    division_error = True

    try:
        int(user_input[0])
        int(user_input[1])
    except ValueError:
        print("Cannot convert to integer")
        value_error = False

    if (value_error):
        try:
            int(user_input[0]) / int(user_input[1])
        except ZeroDivisionError:
            print("Cannot divide by zero")
            division_error = False

    return value_error and division_error


def fraction_to_percentage():
    while True:
        user_fraction = input("Fraction: ")
        values = transform_input(user_fraction)
        evaluate = validator(values)
        
        if evaluate and int(values[0]) > int(values[1]):
            continue

        if evaluate:
            break

    fraction = (int(values[0]) / int(values[1])) * 100

    # Remove decimal ex: 50.0 -> 50
    result = int(fraction)

    if result == 100:
        print("F")
    elif result == 0:
        print("E")
    else:
        print(f"{result}%")

# Read fraction as X / Y

fraction_to_percentage()

# TODO's:
# Validation: X or Y is not an integer (seems ok)
# X is greater than Y (todo)
# or Y is 0 (seems ok)
# Catch exceptions: (seems ok)  
# ValueError (seems ok)
# or ZeroDivisionError (seems ok)
# Last validation should be for input 5/4 - should ask again - fixed