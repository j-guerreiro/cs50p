# Coke problem
# author: jguerreiro

"""
    Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents 
    and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
    Implement a program that prompts the user to insert a coin, one at a time, 
    each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
    output how many cents in change the user is owed. 
    Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

value_counter = 0

while True:
    insert_a_coin = input("Inser a coin: ")
    value_counter += insert_a_coin

    if value_counter > 50:
        break

print(value_counter)