"""
  Support material found in the web:
  - https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
  - https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-python/
  - https://www.geeksforgeeks.org/python-add-substring-at-specific-index/
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

  underscore = "_"
  var_name_list = list(variable_name)
  upper_found_counter = 0

  for char in variable_name:
    if char.isupper():
      # upper_case_char.append(char)
      upper_char_index = variable_name.index(char)
      if upper_found_counter > 0:
        upper_char_index += 1
        var_name_list.insert(upper_char_index, underscore)
      else:
        upper_found_counter += 1
        var_name_list.insert(upper_char_index, underscore)
      
  snakefied_string = ''.join(var_name_list).lower()

  print(snakefied_string)

if __name__ == "__main__":
  main()