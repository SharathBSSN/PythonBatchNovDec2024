"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""

get_str = (input("Enter a temparature in Celsius/Fahrenheit (xxF or xxf or xxC or xxC): ")).strip().lower()

temp_type = get_str[-1]

temp = float(get_str.split(temp_type)[0])

if temp_type == 'c':
    out_temp =  (temp * (9/5)) + 32
    print(temp,"°C = ", out_temp,"°F")
elif temp_type == 'f':
    out_temp = (temp - 32) * 5/9
    print(temp,"°F = ", out_temp,"°C")
else:
    print(temp_type, temp, int(temp), temp_type in ['c', 'f'])
    print("Please enter in a valid format: (xxF or xxf or xxC or xxC)")


