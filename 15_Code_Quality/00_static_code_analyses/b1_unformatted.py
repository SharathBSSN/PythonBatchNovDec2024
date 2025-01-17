# Unused import
import os
# Enforcing consistent import order
import sys

# Detecting unused variables


def my_function():
    unused_variable = 10


# Enforcing naming conventions
invalid_variable = 10


# Detecting unused function arguments
def my_function(arg1, arg2):
    return arg1


# Identifying missing docstrings
def my_function():
    pass


# Enforcing line length limit
long_line = "This is a very long line that exceeds the line length limit defined by Pylint"
# Identifying unused class methods


class MyClass:
    def unused_method(self):
        pass


# Detecting unreachable code
def my_function():
    return 10
    print("This code is unreachable")


# Identifying missing return statements in functions/methods
def my_function():
    pass


# Enforcing consistent whitespace usage
invalid_whitespace = 10 + 5

# Identifying incorrect use of mutable default function arguments


def my_function(arg=[]):
    arg.append(10)


# Checking for inconsistent use of quotation marks
invalid_string = 'This string uses single quotes instead of double quotes'

# Detecting unnecessary pass statements
try:
    1 / 0
except Exception as ex:
    print(ex)
    pass

# Identifying incorrect variable reassignment
variable = 10
variable = "updated value"

"""
pylint can only list the problems, but not rectify themStop.
        @SharathBSSN ➜ /workspaces/PythonBatchNovDec2024/15_Code_Quality/00_static_code_analyses (class32) $ python -m pylint b1_unformatted.py 
        ************* Module b1_unformatted
        b1_unformatted.py:90:0: C0304: Final newline missing (missing-final-newline)
        b1_unformatted.py:90:0: C0304: Final newline missing (missing-final-newline)
        b1_unformatted.py:1:0: C0114: Missing module docstring (missing-module-docstring)
        b1_unformatted.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
        b1_unformatted.py:12:0: C0103: Constant name "invalid_variable" doesn't conform to UPPER_CASE naming style (invalid-name)
        b1_unformatted.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
        b1_unformatted.py:16:0: E0102: function already defined line 7 (function-redefined)
        b1_unformatted.py:16:22: W0613: Unused argument 'arg2' (unused-argument)
        b1_unformatted.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
        b1_unformatted.py:22:0: E0102: function already defined line 7 (function-redefined)
        b1_unformatted.py:27:0: C0103: Constant name "long_line" doesn't conform to UPPER_CASE naming style (invalid-name)
        b1_unformatted.py:31:0: C0115: Missing class docstring (missing-class-docstring)
        b1_unformatted.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
        b1_unformatted.py:31:0: R0903: Too few public methods (1/2) (too-few-public-methods)
        b1_unformatted.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
        b1_unformatted.py:37:0: E0102: function already defined line 7 (function-redefined)
        b1_unformatted.py:39:4: W0101: Unreachable code (unreachable)
        b1_unformatted.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
        b1_unformatted.py:43:0: E0102: function already defined line 7 (function-redefined)
        b1_unformatted.py:48:0: C0103: Constant name "invalid_whitespace" doesn't conform to UPPER_CASE naming style (invalid-name)
        b1_unformatted.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
        b1_unformatted.py:51:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
        b1_unformatted.py:51:0: E0102: function already defined line 7 (function-redefined)
        b1_unformatted.py:56:0: C0103: Constant name "invalid_string" doesn't conform to UPPER_CASE naming style (invalid-name)
        b1_unformatted.py:61:7: W0718: Catching too general exception Exception (broad-exception-caught)
        b1_unformatted.py:63:4: W0107: Unnecessary pass statement (unnecessary-pass)
        b1_unformatted.py:66:0: C0103: Constant name "variable" doesn't conform to UPPER_CASE naming style (invalid-name)
        b1_unformatted.py:67:0: C0103: Constant name "variable" doesn't conform to UPPER_CASE naming style (invalid-name)
        b1_unformatted.py:2:0: W0611: Unused import os (unused-import)
        b1_unformatted.py:4:0: W0611: Unused import sys (unused-import)

        -----------------------------------
        Your code has been rated at 0.00/10

autopep8 can help to auto format


python b1_unformatted.py
python -m autopep8 b1_unformatted.py   
python -m autopep8 -d b1_unformatted.py

cp b1_unformatted.py b0_unformatted.py.bak
python -m autopep8 -i b1_unformatted.py


TO update changes on same file
    autopep8 --in-place --aggressive --aggressive <filename>

To create backup and to changes
    cp b1_unformatted.py b1_unformatted.py.bak && autopep8 --aggressive --in-place b2_formatted.py


"""
