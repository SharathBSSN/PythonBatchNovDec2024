#!/usr/bin/python
"""
Purpose: Writing csv using csv module with diff delimiter(s)

"""
import csv
import re # Regular Expression Module


DELIMITERS = '[/;:]'

with open("my_fourth.csv", "w", newline="") as fh:
    header_names = ("sno", "data", "delimiter_used")
    writer = csv.writer(fh, delimiter="/")

    # To write the headers
    writer.writerow(header_names)

    # print(dir(writer))
    writer.writerow([1, "data_write", "frwd_slash"])
    writer.writerows([[2, "data_write", "frwd_slash"], [3, "data_write", "frwd_slash"]])
    fh.close()


# assignment - create csv files with all possible delimiters and read the content also

with open("my_fourth.csv", "a", newline="") as fh:
    writer = csv.writer(fh, delimiter=":")

    writer.writerows([[4, "data_append", "colan"], [5, "data_append", "colan"]])
    fh.close()

with open("my_fourth.csv", "a", newline="") as fh:
    writer = csv.writer(fh, delimiter=";")

    writer.writerows([[6, "data_append", "semi-colan"], [7, "data_append", "semi-colan"]])
    fh.close()

with open("my_fourth.csv", "r", newline="") as fh:
    for line in fh:
        # Split using multiple delimiters
        row = re.split(DELIMITERS, line.strip())
        print(row)
    fh.close()


"""
Delimiter	Symbol	Description	        Example
Comma	    ,	    Standard delimiter	John,25,USA
Semicolon	;	    Common in Europe	John;25;USA
Tab	        \t	    Tab-separated 	    John 25 USA
Pipe	    `	`	Often used in logs
Colon	    :	    Less common	        John:25:USA
Space	    ' '	    For readability	    John 25 USA
Hash	    #	    Rarely used	        John#25#USA
Caret	    ^	    In legacy systems	John^25^USA
Ampersand	&	    Rarely used	        John&25&USA
"""