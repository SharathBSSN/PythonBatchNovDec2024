"""
Purpose: Importing and using python script(s)
"""

import calc
# import operations

# selective import
from operations import factorial

# wildcard import -> NOT A BEST PRACTICE
# from operations import *


print(f"{dir(calc)=}")
# print(f"{dir(operations)=}")

x = calc.addition(100,200)
# y = operations.factorial(25)
y = factorial(25)



print(f"{x = }")

print(f"{y = }")

# print(help(calc))

# byte code (.pyc) file created can be stopped, by setting
# environment variable
# export PYTHONDONTWRITEBYTECODE=1