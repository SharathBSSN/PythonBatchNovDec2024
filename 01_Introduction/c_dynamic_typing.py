"""
    Purpose: Python is a dynamically typed lang

    How Python runs?
    .py file -> python byte code -> pythonInterpetor -> C Compiler -> Machine Level

    thus, python is slow in comparision with other compiler pased languages resulting in an line by line or block based execution of code

    Static Vs Dynamic

        Variables:
            In Static: first declaration and then utlize
            In Dynamic: no declaration needed, create and use on the go

"""

num1 = 100

#Print can be acces in multiple wasys by using the comma(,) saperator
print("1. num1 =", num1, " having type =", type(num1))

#Overwriting a var - works in both Static and Dynamic Typed lang(s)
num1 = 300
print("2. num1 =", num1, " having type =", type(num1))

#Only works in Python
num1 = 300.00 # works even with 300.
print("3. num1 =", num1, " having type =", type(num1))

num1 = -300.00 # works for -ve numbers as well
print("3. num1 =", num1, " having type =", type(num1))

num1 = 300, # makes this a Tuple
print("3. num1 =", num1, " having type =", type(num1))

num1 = 300j # makes this a complex number
print("3. num1 =", num1, " having type =", type(num1))

num1 = "300j" # makes this a string
print("3. num1 =", num1, " having type =", type(num1))

# NOTE: String must always be declated in quotes(")

num1 = True # makes this a boolean val
print("3. num1 =", num1, " having type =", type(num1))

num1 = None # makes this a NoneValue
print("3. num1 =", num1, " having type =", type(num1))

# num1 = true will throw an 'not defined' error as PYTHON IS A CASE SENSITIVE LANG


