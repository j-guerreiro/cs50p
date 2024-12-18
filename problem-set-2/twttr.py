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

lower_vowels = ['a', 'e', 'i', 'o', 'u']
upper_vowels = ['A', 'E', 'I', 'O', 'U']
text = "Your"
text_array = list(text)
no_vowel_string = []
vowel_counter = 0

# Loop over compare and remove pass I
for i in text_array:
    for j in lower_vowels:
        if i == j:
            text_array.remove(i)
            
# Loop over compare and remove pass II
for i in text_array:
    for j in upper_vowels:
        if i == j:
            text_array.remove(i)

no_vowel_string = ''.join(text_array)

print(no_vowel_string)

"""
    TODO's:
    - Bug with 'u' letter 
    - At first I used nested loops, but I should try a non nested loop solution later
"""