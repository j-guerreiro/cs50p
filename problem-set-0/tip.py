# Tip problem
# Author: jguerreiro

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # remove $ sign from left side of string
    d = d.lstrip('$')
    return float(d)

def percent_to_float(p):
    # remove % sign from right side of string
    # divide value by 100
    p = p.rstrip('%')
    p = (float(p)) / 100

    return p
main()