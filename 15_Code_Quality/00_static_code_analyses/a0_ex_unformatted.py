"""
Purpose: Static Code Analyses, using pylint

    pip install -U pylint

    python -m pylint script.py

"""
a=23; b=45
c=a+b

print(c)

"""
@SharathBSSN ➜ /workspaces/PythonBatchNovDec2024/15_Code_Quality/00_static_code_analyses (
class32) $ python -m pylint a0_ex_unformatted.py 
************* Module a0_ex_unformatted
a0_ex_unformatted.py:9:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
a0_ex_unformatted.py:9:6: C0321: More than one statement on a single line (multiple-statements)
a0_ex_unformatted.py:9:6: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
a0_ex_unformatted.py:10:0: C0103: Constant name "c" doesn't conform to UPPER_CASE naming style (invalid-name)

-----------------------------------
Your code has been rated at 0.00/10
"""
