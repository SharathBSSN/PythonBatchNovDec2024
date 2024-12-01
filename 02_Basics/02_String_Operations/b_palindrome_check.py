
#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable
Step 2: create a reverse string , from the given string, using string reversal
Step 3: compare both with a condition and decide

"""

# test_string = input("Enter any string:")
# print("test_string    :", test_string)


# # reverse string
# reverse_string = test_string[::-1]
# print("reverse_string :", reverse_string)

# print(test_string == reverse_string)

# print("test_string == reverse_string:", test_string == reverse_string)


# if test_string == reverse_string:
#     print(test_string, "is palindrome")
# else:
#     print(test_string, "is NOT a palindrome")    



# Assignment: test if a given sentence is palindrome or not
# HINT: ignore the whitespace and check


inp_sentence = input("Enter any sentence:").lower()

test_sentence = inp_sentence.replace(" ", "")

# reverse string
reverse_sentance = test_sentence[::-1]

print()
if test_sentence == reverse_sentance:
    print(inp_sentence, "is palindrome")
else:
    print(inp_sentence, "is NOT a palindrome")    



# test_sentence = input("Enter any sentence:")
# print("test_sentence    :", test_sentence)

# test_sentence = test_sentence.split()

# #reversal
# rev_sentence = test_sentence[::-1]
# print("rev_sentence :", rev_sentence)

# print(test_sentence == rev_sentence)

# print("test_sentence == rev_sentence:", test_sentence == rev_sentence)


# if test_sentence == rev_sentence:
#     print(" ".join(test_sentence), "is palindrome")
# else:
#     print(" ".join(test_sentence), "is NOT a palindrome")    