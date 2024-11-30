
"""
Purpose: Identifiers in Python

    Variable
        1. keyword   --> pre existing 'words' that hold a specific defination within the language
        2. Identifier -> user(dev) defined 'words'

"""
# To load or include a module
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print()


print(True)  # True

#Python is case sentve lang
# print(true) NameError: name 'true' is not defined. Did you mean: 'True'?

my_value = "undefined"
print(my_value)  # Identifier

# True = "undefined"
# SyntaxError: cannot assign to True


print(keyword.iskeyword("True"))        # True
print(keyword.iskeyword("true"))        # False
print(keyword.iskeyword("my_value"))    # False


# ------------------------------------------------------
# Identifiers - User-defined variables
#   - Naming Convention
#      1. keywords should not be used as identifiers
#      2. first character: a-z, A-Z, _
#      3. remaining chars: a-z, A-Z, _, 0-9

# ---- Rule 1
# Can not use keywords as identifiers
# True = 123        # SyntaxError: cannot assign to True
# None = 'Nothing'  # SyntaxError: cannot assign to None

# PEP 8 - Dont create identifiers which are similar as Keywords
true = 123          # NOT
none = "Nothing"    # NOT

true_value = 123        # ACCEPTABLE
none_result = "Nothing" # ACCEPTABLE

# ---- Rule 2 & 3

# ACCEPTABLE
name = "Quintus Lentulas Baiats"
name_of_student = "Spartacus"
first_name = "Quintis"
student_1 = "Illythia"
first_____child = "Crixus"

# NOT
# $name = "Numerious"
# name-of-student = "Lestrade"
# name of student = "Lestrade"
# 1st_name = "Ashur"

# PEP 8 recommends to use capitals for constants
PI = 3.1416
DOZEN = 12


# OOP -> name mangling
# variable   -> Public variable
# _variable  -> Protected variable
# __variable -> Private variable

_2nd_student = "Dominus"
_job = "Developer"
__role = "Product Designer"
___salary = 199919981997

# __variable__ ->  Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__


print("__name__ =", __name__)  # __main__
print("__file__ =", __file__)

# print("__Domina__ =", __Domina__)
# NameError: name '__Domina__' is not defined
