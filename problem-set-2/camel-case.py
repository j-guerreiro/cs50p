"""
  Support material that helped a lot - found in the web:
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
  variable_to_snakefy = input("🐪 Camel case variable: ")
  snakefy(variable_to_snakefy)


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
  result = []

  for index, char in enumerate (var_name_list):
    if char.isupper():
      result.append(underscore)
    result.append(char.lower())
  snakefied_string = ''.join(result)

  print(snakefied_string)


if __name__ == "__main__":
  main()

"""
  Proposed tests passed:
  1. name 
  2. firstName
  3. prefferedFirstName
  4. myPrestigiousVariableName -> my_prestigious_variable_name (fixed)
  5. Pitfall! myCatCoconutCantChew (repeated letters break) -> my____catcoconutcantchew 
    (fixed using enumerate instead of getting the index of the first occurrence, and append instead of insert)
"""