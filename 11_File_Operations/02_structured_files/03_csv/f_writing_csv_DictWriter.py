"""
Purpose: Writing csv using csv module

"""
import csv

with open("my_second.csv", mode="w", newline='') as fh:
    header_names = ("sno", "name", "age", "designation")
    writer = csv.DictWriter(fh, delimiter=",", fieldnames=header_names)

    # To write the headers
    writer.writeheader()

    # To write a single record
    writer.writerow({"sno": 1, "name": "Arthi", "age": 11, "designation": "carpenter"})

    # To write multiple records
    writer.writerows(
        [
            {"sno": 2, "name": "Preethi", "age": 12, "designation": "software"},
            {"sno": 3, "name": "Bhuvana", "age": 13, "designation": "business"},
            {"sno": 4, "name": "Bhuvana", "age": 13},  # , "designation": "business"},
            {"sno": 5, "name": "Bhuvana"},  # , "age": 13} #, "designation": "business"},
            {"sno": 6, "designation": "business"},
        ]
    )