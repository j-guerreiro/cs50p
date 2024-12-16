"""
  Support material found in the web:
  - https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
  - https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-python/
"""
# Camel case problem
# author: jguerreiro

"""
  Implement a program that prompts the user for the name of a 
  variable in camel case and outputs the corresponding name in snake case. 
  Assume that the user's input will indeed be in camel case.

  Snake case example: snake_case
  Camel case example: camelCase
"""

def main():
    
  # name_of_variable = input("🐪 Camel case variable: ")
  snakefy("myCutePet")


def snakefy(variable_name):
  """
    Ex: myDog, myCutePet
        my_dog, my_cute_pet

  1. Find the uppercase char on the string
  2. After finding the char, get its char index
  3. Store the found index(es) and uppercase char
  3. Insert a "_" before the uppercase character
  """
  upper_case_index = []
  upper_case_char = []

  for char in variable_name:
    if char.isupper():
      upper_case_char.append(char)
      upper_case_index.append(variable_name.index(char))
  
  char_index_dict = dict(zip(upper_case_char, upper_case_index))
  # {'C': 2, 'P': 5}
  print(char_index_dict['P']) # get the key value

  snake_cased = variable_name[0:char_index_dict["P"]] + "_" + variable_name[char_index_dict["P"]:]
  snake_cased = variable_name[0:2] + "_" + variable_name[2:]
  snake_cased = snake_cased.lower()

  print(snake_cased)

if __name__ == "__main__":
  main()