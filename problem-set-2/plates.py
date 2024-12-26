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

    Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
    Assume that any letters in the user's input will be uppercase. 
    Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
    You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid plate")
    else:
        print("Invalid plate")


def check_length(s):
    # All vanity plates must start with at least two letters.   
    return len(s) >= 2 and len(s) <= 6


def check_first_two(s):
    # check if the first two characters are not numbers.
    char_list = list(s)
    numbers_found = 0
    loop_counter = 0

    for char in char_list:
        try:
            int(char)
        except:
            print("Strings cannot be converted to int")
        else:
            print("A number was found, flagging as FALSE")
            numbers_found = numbers_found + 1
        
        loop_counter = loop_counter + 1

        if loop_counter > 1:
            break
            
    """  
       if numbers ARE FOUND, return False
       if numbers ARE NOT found, return True
    """
    return not(numbers_found > 0)


def check_illegal_chars(s):
    # Check for: periods, spaces, or punctuation marks.
    illegal_chars = string.punctuation
    counter = 0
    
    # In the future could use regex to validate, but now that should be enough.
    for i in illegal_chars:
        for j in s:
            if i == j:
                counter = counter + 1

    # Empty spaces check:
    for letter in s:
        if letter == " ":
            counter =  counter + 1

    return counter == 0


def check_number_pattern(s):
    """
        # KEY RULES:

        If the plate contains any numbers, they cannot appear in the middle of the plate or at the beginning.
        Example:
        Numbers must be at the end of the plate:

        If the plate contains any numbers, they cannot appear in the middle of the plate or at the beginning.
        Example:
        ✅ ABC123 (Valid, numbers are at the end).
        ❌ AB1C23 (Invalid, numbers are in the middle).
        ❌ 1ABC23 (Invalid, numbers are at the beginning).
        No numbers in the middle or mixed with letters:

        Numbers cannot interrupt letters; they must all come after all the letters.
        Example:
        ✅ AAA222 (Valid, letters first, numbers at the end).
        ❌ AAA22A (Invalid, numbers appear before another letter).
        The first number cannot be a '0':

        If numbers are included in the plate, they cannot start with a 0.
        Example:
        ✅ ABC123 (Valid, first number is not 0).
        ❌ ABC012 (Invalid, the first number is 0).

    """
    char_list = list(s)

    # 1. Check length range (2 to 6) and check if the first 2 chars are not nums
    if check_length(s) and check_first_two(s):

        # 2. Check if first number found is zero
        for char in char_list:
            try:
                char_to_num = int(char)
            except:
                print("Strings cannot be converted to int")
            else:
                print("A number was found, check if it is zero")
                if char_to_num == 0:
                    print("First number found is zero!")
                    return False

        # 3. TODO a pattern found is: after a number, there cant be a character next
        # Ex:
    else:
        return False
    
    return True


def is_valid(s):
    s = s.upper()
    return (
        check_length(s)
        and check_first_two(s)
        and check_illegal_chars(s)
        and check_number_pattern(s)
    )
main()


