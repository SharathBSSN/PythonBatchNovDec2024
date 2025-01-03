"""
Purpose: Reading(Parsing) CSV using csv module
"""

import csv

"""
print(dir(csv))
['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'QUOTE_NOTNULL', 'QUOTE_STRINGS', 'Sniffer', 'StringIO', '_Dialect', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'types', 'unix_dialect', 'unregister_dialect', 'writer']

for each_attribute in dir(csv):
    if each_attribute.startswith('__'):
        continue
    print(each_attribute)

Dialect
DictReader
DictWriter
Error
QUOTE_ALL
QUOTE_MINIMAL
QUOTE_NONE
QUOTE_NONNUMERIC
QUOTE_NOTNULL
QUOTE_STRINGS
Sniffer
StringIO
_Dialect
excel
excel_tab
field_size_limit
get_dialect
list_dialects
re
reader
register_dialect
types
unix_dialect
unregister_dialect
writer
"""

# Method 1 
fh  = open("my_file.csv", mode="r")

# fh.read()
file_content = csv.reader(fh, delimiter=",")
print(file_content)

# To skip the header
next(file_content, None)

# print(list(file_content))
# [['sno ', 'name   ', 'age ', 'designation'], ['  1 ', 'kotha  ', ' 11 ', 'thopu'], ['  2 ', 'bunty  ', ' 12 ', 'phodi'], ['  3 ', 'challa ', ' 13 ', 'thurumu']]

names = []
for eachline in file_content: 
    # print(eachline)
    names.append(eachline[1])

print(f"{names =}")
fh.close()

# Method 2 - using context manager
with open("my_file.csv", mode="r") as fh:

    # file_content = fh.read()
    file_content = csv.reader(fh, delimiter=",")
    print(file_content)

    # To skip the header
    next(file_content, None)

    # print(list(file_content))
    names = []
    for eachline in file_content: 
        names.append(eachline[1])

    print(f"{names =}")