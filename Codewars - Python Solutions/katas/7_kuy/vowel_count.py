"""
    Return the number (count) of vowels in the given string.

    We will consider a, e, i, o, and u as vowels for this Kata.
"""

def getCount(inputStr):
    num_vowels = 0
    # your code here
    import re
    reg = re.compile(r'[aeiou]')
    num_vowels = len(re.findall(reg, inputStr))
    return num_vowels