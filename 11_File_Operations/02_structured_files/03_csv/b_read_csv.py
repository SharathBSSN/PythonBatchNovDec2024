"""
Purpose: Reading(Parsing) csv, using unstructure file ops
"""
# Method 1
with open("my_file.csv", mode="r") as fh:
    file_content = fh.read()


# print(file_content.split())
# ['sno', ',name', ',age', ',designation', '1', ',kotha', ',', '11', ',thopu', '2', ',bunty', ',', '12', ',phodi', '3', ',challa', ',', '13', ',thurumu']
# print(file_content.splitlines())
# ['sno ,name   ,age ,designation', '  1 ,kotha  , 11 ,thopu', '  2 ,bunty  , 12 ,phodi', '  3 ,challa , 13 ,thurumu']

# names = []
# for each_line in file_content.splitlines()[1:]:
#     name = each_line.split(',')[1]
#     names.append(name)

# print(f"{names = }")
# # names = ['akhila Bhopal', 'neha', 'hiral']



# Method 2
with open("my_file.csv", mode="r") as fh:
    file_content = fh.readlines()

names = []
for each_line in file_content[1:]:
    name = each_line.split(',')[1].strip()
    names.append(name)

print(f"{names = }")