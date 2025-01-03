"""
Purpose: writing(creating) a CSV, like unstructured data
"""

with open("my_file.csv", "w") as fh:
    fh.write("sno,name,age,designation\n")
    fh.write("1,kotha,11,thopu\n")
    fh.write("2,bunty,12,phodi\n")
    fh.write("3,challa,13,thurumu\n")

    fh.flush()
    fh.close()