#!/usr/bin/python
"""
Purpose: Static Code Analyses, using pylint

    pip install -U pylint --user

    python -m pylint script.py

"""
# A = 23
# B = 45
# C = A + B

# print(C)

NUM1 = 23
NUM2 = 45
RESULT = NUM1 + NUM2

print(f"{RESULT =}")

"""
************* Module a1_ex_formatted
a1_ex_formatted.py:20:0: C0304: Final newline missing (missing-final-newline)

-----------------------------------
Your code has been rated at 7.50/10
"""