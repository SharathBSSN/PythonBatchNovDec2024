"""
    Purpose: Print() usage and syntax
"""

name = "cuddly-giggle-q7jvj5q6vx539jx"

# Use of '+' in print(), conactinates left and right side as is
print("Current codespace name is"+ name)
print("Current codespace name is "+ name)

# Use of ',' in print(), it also take in another parameter which is by default sep = " "
print("Current codespace name is", name, sep=" ")
print("Current codespace name is", name, sep="->")
print("Current codespace name is", name, sep=" - ")

name = 11242024

# print("Current codespace name is"+ name) -- TypeError: can only concatenate str (not "int") to str

# NOTE: PYTHON is a strictly typed lang, meaning it will only add exact data types

# NOTE: type: python in cmd to enter into interactive mode, generally used for DEBUGGING purposes

#Use built_in functions to convert Str -> Int or vice versa

print("Current codespace name is "+ str(name))

# int() limitations
# print(int("9.8"))
# print(int("three"))

