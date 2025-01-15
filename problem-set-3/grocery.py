# Taqueria problem
# author: jguerreiro

"""
    Grocery List
    Suppose that you're in the habit of making a list of items you need from the grocery store.

    In a file called grocery.py, implement a program that prompts the user for items, one per line, 
    until the user inputs control-d (which is a common way of ending one's input to a program). 
    Then output the user's grocery list in all uppercase, sorted alphabetically by item, prefixing 
    each line with the number of times the user inputted that item. 
    No need to pluralize the items. Treat the user's input case-insensitively.
"""


def grocery():
    grocery_list = []
    grocery_dict = {}

    while True:
        try:
            item = input()
            grocery_list.append(item.upper())
        except EOFError:
            break

    grocery_list = sorted(grocery_list)
    print(grocery_list)

grocery()

#----------------------------------------------------------------
# TODO:
#----------------------------------------------------------------
# Prefix each line with number of times item was inputted - todo
# Dictify the list and
#----------------------------------------------------------------
# DONE:
# Sort list alphabetically - check
# Get inputs until ctrl+d - check
# Treat input case-insensitively - check
#----------------------------------------------------------------


