"""
    Purpose: Importance of Indentation

    Python does have any braces to open or close a function, each functional block or code will be enclosed under with an indentaion

    Recommended use of Indentaion: 4 whitespaces -> 1 tabspace
"""

# print("IndentaionError") IndentationError: unexpected indent

#IndentationError: expected an indented block after 'if' statement on line 7
# if True:
# print("True")

if True:
    print("if clause")
else:
    print("else clause")


i = 0
while i>0 :
    print("in while")
    j = i+7
    while j<9 :
        print("in while-> while")
