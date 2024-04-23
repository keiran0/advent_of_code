import re

with open('input.txt', 'r') as file:
    strings = file.read().splitlines()

# Part 1

def is_nice(string):

    no_banned_strings = len(re.findall(r'ab|cd|pq|xy', string)) == 0
    twice_in_row = len(re.findall(r'(\w)\1+', string)) >= 1
    contains_three_vowels = len(re.findall(r'[aeiou]', string)) >= 3

    if bool(contains_three_vowels and twice_in_row and no_banned_strings):
        return True

    return False

num_nice = 0

for string in strings:
    if is_nice(string):
        num_nice += 1

print(num_nice)

# Part 2

def is_nice(string):
    twice_in_string = len(re.findall(r'(\w{2})\w*?\1', string)) > 0
    one_letter_between = len(re.findall(r'(\w)\w\1', string)) > 0
    if twice_in_string and one_letter_between:
        return True

    return False

num_nice = 0

for string in strings:
    if is_nice(string):
        num_nice += 1

print(num_nice)