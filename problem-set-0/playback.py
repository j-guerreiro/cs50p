# Playback problem
# Author: jguerreiro

"""
  read a string
  check spaces
  if space exist, then replace by '...'
"""

text = "This is CS50"
dots = "..."

new_text = ""
new_text = text.replace(' ', dots)

print(new_text)