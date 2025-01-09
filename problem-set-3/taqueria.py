# Taqueria problem
# author: jguerreiro
# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
"""
    One of the most popular places to eat in Harvard Square is Felipe's Taqueria, 
    which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

    {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, 
    until the user inputs control-d (which is a common way of ending one's input to a program). After each inputted item, display the 
    total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
    Treat the user's input case insensitively. Ignore any input that isn't an item. Assume that every item on the menu will be titlecased.

"""

tacos_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def check_input(order) -> bool:
    """
        Checks if the order input exists in the tacos_dict
        @Return bool
    """

    # Extract dict keys, generate a list, 
    # and assign to taco_names
    taco_names = list(tacos_dict.keys())
    count = 0

    for name in taco_names:
        if name.casefold() == order.casefold():
            count += 1
            break
    
    return count > 0


def process_order():
    total = 0

    while True:
        while True:
            order = input("Order: ")

            # if check passed, break loop
            # ignore input, ask again, check again.
            if check_input(order):
                break
            else:
                continue
        
        
        for taco in tacos_dict:
            if taco.casefold() == order.casefold():
                # get the tacos_dict value from order key
                # and sum with total
                total = total + tacos_dict.get(order)    
                print(f"Current total: ${total}")
                break

process_order()

# TODO's: 
# Ignore any input that isn't an item (fixed)
# Need to find a way to ignore case (bug in line 78)