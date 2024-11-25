"""
    Purpose: print() function and usage
        Escapes Sequences
        \t - tab space
        \n - next line
        \b - overwrites prev char

        r"" - raw string

        Similar to sep="", there is also and end="\n" <- default value

"""

print("This is how you use eEscape Sequences")
print("\tThis is how you use \ne\bEscape Sequences")

# to ignore the esc seq
print("C:\my\\newfolder")
print("C:\my\newfolder")
print(r"C:\my\newfolder")

print("Exhit A with end=' '", end=" ")
print("Exhibit B comming from another print()")