#!/usr/bin/python
"""
Purpose: Read numeric data from csv files

By default, data is read as a list of strings.
If we specify the QUOTE_NONNUMERIC format,
non-quoted values are converted into float values.

"""
import csv

with open("my_non_english2.csv", "w", newline="", encoding="utf-8") as gh:
    header_names = ("sno", "name", "language")
    writer = csv.writer(gh, delimiter=",", dialect="excel") # dialect="excel" is the key difference, no noticable diff in .csv file, diff can be percieved while opening as an .xlsx file

    # To write the headers
    writer.writerow(header_names)

    writer.writerow([1, "english", "Python"])
    writer.writerows(
        [
            [2, "Russian", "питон"],
            [3, "Italian", "Pitone"],
            [4, "Japanese", "パイソン"],
            [5, "Chinese", "蟒蛇"],
            [6, "Telugu", "పైథాన్"],
            [7, "Tamil", "பைதான்"],
            [8, "Hindi", "अजगर"],
        ]
    )