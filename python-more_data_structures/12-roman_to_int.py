#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    value_a = 0

    for char in roman_string[::-1]:
        value = roman_numerals[char]
        total += value if value >= value_a else -value
        value_a = value

    return total
