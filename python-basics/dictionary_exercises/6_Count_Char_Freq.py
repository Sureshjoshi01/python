# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.


def char_freq(string1):
    dict1 = {}
    for char in string1:
        dict1[char] = dict1.get(char,0) + 1
    return dict1


def simple_way_char_freq(string1):
    dict1 = {}
    for char in string1:
        if char in dict1:
            dict1[char] = dict1[char] + 1
        else:
            dict1[char] = 1
    return dict1

string1 = 'Jessa'

print(f"Frequencies for '{string1}': {char_freq(string1)}")

print(f"Frequencies for '{string1}': {simple_way_char_freq(string1)}")
