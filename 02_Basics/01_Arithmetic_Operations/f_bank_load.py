"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""
initial_principal_bal = float(input("Enter your Initial Principal Balance: "))

annual_intrest_rate = float(input("Enter your Annaual Intrest Rate: "))
annual_intrest_rate = annual_intrest_rate / 100

time_in_years = float(input("Enter your time (in years): "))

simple_intrest_amnt = (initial_principal_bal * annual_intrest_rate * time_in_years)

total_amnt_01 = initial_principal_bal + simple_intrest_amnt

total_amnt_02 = initial_principal_bal * ((1 + annual_intrest_rate / 12)**(12*time_in_years))


print("Total amount accured : ")
print("Simple Intreste: ", total_amnt_01)
print("Compound Intreste: ", total_amnt_02)





# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php