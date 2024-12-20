# Plates problem
# author: jguerreiro

import string


"""
    In Massachusetts, home to Harvard University, 
    it's possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. 
    
    Among the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. 
    For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a '0'.”
    “No periods, spaces, or punctuation marks are allowed.”
    In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
    Assume that any letters in the user's input will be uppercase. 
    Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
    You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def check_length(s):
    # All vanity plates must start with at least two letters.   
    return len(s) >= 2 and len(s) <= 6


def check_first_two(s):
    # check if the first two characters are not numbers
    first_two_type = str(type(s[0:2]))
    return  first_two_type == "<class 'str'>"


def check_illegal_chars(s):
    illegal_chars = string.punctuation
    counter = 0
    
    for i in illegal_chars:
        for j in s:
            if i == j:
                counter = counter + 1

    return counter == 0


def is_valid(s):
    # maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    validate_length = check_length(s)
    validate_first_2_letters = check_first_two(s)
    validate_illegal_chars = check_illegal_chars(s)

    return validate_length and validate_first_2_letters and validate_illegal_chars
main()

