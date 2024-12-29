# Nutrition problem
# author: jguerreiro

"""
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most 
frequently consumed raw fruits … in the United States. 
Retail stores are welcome to download the posters, print, display and/or distribute them 
to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) 
and then outputs the number of calories in one portion of that fruit, per the FDA's poster for fruits, which is also available as text. 
Capitalization aside, assume that users will input fruits exactly as written in the poster 
(e.g., strawberries, not strawberry). Ignore any input that isn't a fruit.

"""

fruit_choice = input("Type in the fruit and I will tell its calories: ")

fruits = {
  "Apple": 130,
  "Avocado": 50,
  "Sweet Cherries": 100
}

def number_of_calories(fruits, user_input):
    # Function will accept apple or Apple (letter case fix)
    # Also accepts strings like: sweet cherries-> (outputs) -> Sweet Cherries
    fruit_word_list = user_input.split()
    capitalized = []

    for word in fruit_word_list:
        capitalized.append(word.capitalize())

    capitalized_input = " ".join(capitalized)

    for fruit in fruits:
        if capitalized_input == fruit:
            # {fruits[fruit]} -> access the key's value
            print(f"Fruit: {fruit} | Calories: {fruits[fruit]}")

number_of_calories(fruits, fruit_choice)