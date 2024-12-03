#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) Check if given char is empty 
2) Check if given char is alphabet
3) Check if given char is vowel

NOTE: handle case-sensitivity 

"""

VOWELS = ['a', 'e', 'i', 'o', 'u']

get_char = input("Enter a character to check if it is a vowel (input -> a-z, A-Z) ").strip().lower()

if get_char.isalpha() and get_char != "":
    if get_char in VOWELS:
        print("HORRAY!!! Given charater is an VOWEL!!")
    else:
        print("Given charater is an CONSONENT!!")
else:
    print("Please enter a valid charater: a-z, A-Z")


