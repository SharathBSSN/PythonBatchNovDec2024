#!/usr/bin/python
"""
Purpose: Importing & using python script
"""
import package3

print(dir(package3))


print(package3.__doc__)
print(package3.calc.__doc__)
print(package3.operations.__doc__)
print()

print(package3.calc.addition.__doc__)
print()

from package3 import calc
from package3.calc import division

print(dir(calc))

# print(calc.__builtins__)

print(f"{calc.addition(10, 20) =}")
print()

print(f"{calc.__doc__          =}")
print(f"{calc.addition.__doc__ =}")
print(f"{division.__doc__            =}")


help(calc)