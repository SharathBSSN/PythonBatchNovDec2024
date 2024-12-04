"""
Purpose: Check even-ness of a given number, in runtime.
"""
# Alogorithm: determining odd/even status using the modulus arithmetic operator

# number = 33
# print(f"{number             = }")
# print(f"{number / 2         = }")
# print(f"{number % 2         = }")
# print(f"{number % 2 == 0    = }")


# if number != 0:
#     print(f"{number} is non-zero")

# if number:
#     print(f"{number} is non-zero")


# """
# It can evaluate that
#     number != None and
#     number != False and
#     number != 0 and
#     number != ""
# """


# if number % 2 == 0:
#     print(f"{number} is Even")

# if number % 2:  # number % 2 != 0
#     print(f"{number} is odd")


# # --------------------
# print()
# number = 13
# print(f"{number             = }")
# print(f"{number % 2         = }")
# print(f"{number % 2 == 0    = }")

# if number % 2:  # number % 2 != 0
#     print(f"{number} is odd")

# if number % 2 == 0:
#     print(f"{number} is Even")

# # --------------------------------

# # Rewriting with else
# if number % 2 == 0:
#     print(f"{number} is EVEN")
# else:
#     print(f"{number} is ODD")

# # rewriting
# if number % 2:
#     print(f"{number} is ODD")
# else:
#     print(f"{number} is EVEN")



# Assignment: Generate even numbers between 45 & 137
# loop values between limits, test eveness for each number
# and display, if it is even

# TIP - range, if condition within it, print function


get_range = input("Enter range of numbers of which to generate a list of even numbers.. Eg -> 45 137\n")

a,b = get_range.split()

NUMS = range(int(a),int(b)) 
even = []

for i in NUMS:
    if i % 2 == 0: even.append(i)

print("List of even numbers between ",a, " and ",b," are: ", even)