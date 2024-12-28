# Twttr problem
# author: jguerreiro

"""
    Links that helped:
    - https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/
    - https://www.guvi.in/blog/remove-an-element-from-a-list-in-python/
"""

"""
    When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting vowels, 
    much like Twitter was originally called twttr. 
    Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels 
    (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""


text = "Your"

def remove_vowels(s):

    lower_vowels = ['a', 'e', 'i', 'o', 'u']
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    
    string_list = list(s)

    counter = 0
    # Loop over compare LOWER case and remove vowel

    # run cleaner 2 times
    while True:
        for i in string_list:
            for j in lower_vowels:
                if i == j:
                    string_list.remove(i)
                    
        # Loop over compare UPPER case and remove vowel
        for i in string_list:
            for j in upper_vowels:
                if i == j:
                    string_list.remove(i)

        no_vowel_string = ''.join(string_list)

        counter = counter + 1

        if counter == 2:
            break

    print(no_vowel_string)


remove_vowels(text)

"""
    TODO:
    - Minor code refactor / improvement - can still be improved - using magic number is not good!
"""