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

amount_due = 50
value_counter = amount_due

while True:
    print(f"Amount due: {value_counter}")
    insert_a_coin = input("Insert a coin: ")
    insert_a_coin = int(insert_a_coin)

    if insert_a_coin == 5 or insert_a_coin == 10 or insert_a_coin == 25:
        value_counter = value_counter - insert_a_coin
        if value_counter == 0:
          break
        else:
           continue
    else:
       print("Invalid value, try again!")
       continue


print(f"Change owed: {value_counter}")

# TODO's
"""
  1. There is a bug when owing values, they are negative.
"""