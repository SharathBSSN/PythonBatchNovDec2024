
"""
Purpose: Grocery Store

    Item       cost
    ------------------------
    rice        10/kg
    wheat       34/kg

Algorithm
---------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user(in run time)

NOTE: input()
        -> to get value in run-time
        -> will give any input as string only

"""

# cost of items
cost_of_rice = 10  # per kg
cost_of_wheat = 34  # per kg


# Quantities of Items
qty_of_rice = input("Enter Qty. of Rice  (in Kgs):")
qty_of_rice = float(qty_of_rice)
qty_of_wheat = float(input("Enter Qty. of Wheat(in Kgs):"))

print("Qty of Rice  :", qty_of_rice, type(qty_of_rice))
print("Qty of Wheat  :", qty_of_wheat, type(qty_of_wheat))


# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
print("SP of Rice   :", sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("SP of Wheat  :", sp_of_wheat)


total_sp = sp_of_rice + sp_of_wheat
print("Total SP     :", total_sp)



# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


from datetime import datetime
current_time = datetime.now()


HOST = "cuddly-giggle"
LINE_SPACE = 78
HALF_LINE_SPACE = 39

designer_str_01 = LINE_SPACE * '*'
designer_str_02 = LINE_SPACE * '-'


print(designer_str_01)
print()
print("TECHVISTA SUPER CENTER".center(LINE_SPACE,))
print("ATLANTA, GA. 30033".center(LINE_SPACE,))
print()
print("RECEIPT".center(LINE_SPACE, "-"))
print()
print(designer_str_01)
print(HOST.ljust(HALF_LINE_SPACE) + current_time.strftime(current_time.strftime("%Y-%m-%d %H:%M:%S")).rjust(HALF_LINE_SPACE))
print(designer_str_02)
print()
print(("Quantity" + " X " + "ITEM").ljust(HALF_LINE_SPACE) + ("PRICE").rjust(HALF_LINE_SPACE))
print()
print((str(qty_of_rice) + " X " + "RICE").ljust(HALF_LINE_SPACE) + ("$"+str(sp_of_rice)).rjust(HALF_LINE_SPACE))
print((str(qty_of_wheat) + " X " + "WHEAT").ljust(HALF_LINE_SPACE) + ("$"+str(sp_of_wheat)).rjust(HALF_LINE_SPACE))
print(designer_str_02)
print(designer_str_02)
print(("TOTAL AMOUNT").ljust(HALF_LINE_SPACE) + ("$"+str(total_sp)).rjust(HALF_LINE_SPACE))
print(("CASH").ljust(HALF_LINE_SPACE) + ("$"+str(total_sp)).rjust(HALF_LINE_SPACE))
print(("CHANGE").ljust(HALF_LINE_SPACE) + ("$0").rjust(HALF_LINE_SPACE))
print()
print()
print(("Transaction#").ljust(HALF_LINE_SPACE) + ("12012024").rjust(HALF_LINE_SPACE))
print(designer_str_02)
print()
print("THANK YOU!!".center(LINE_SPACE, "*"))
print()
print()

