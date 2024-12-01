"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""

type_of_convesion = (input("Enter your conversion type!! A-> Ft to Cms, B-> Cms to Ft:"))

if (type_of_convesion == 'A' or type_of_convesion == 'a'):
    get_Ft = float(input("Enter your height in Ft:"))
    conv_cms = ((get_Ft * 12) * 2.54)
    print("FT: ", get_Ft, "CMS: ", conv_cms)

elif (type_of_convesion == 'B' or type_of_convesion == 'b'):
    get_cms = float(input("Enter your height in CMS:"))
    conv_ft = ((get_cms / 2.54) / 12)
    print("CMS: ", get_cms, "FT: ", round(conv_ft, 1))

else:
    print("Please choose A or B")
    