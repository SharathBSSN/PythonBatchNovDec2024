"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

balance = 0

#Initial Deposit min bal 1500
while True:
    initial_Deposit = float(input("Enter your initial deposit(min $1500):"))

    if(initial_Deposit >= 1500):
        break # Breaks out of WHILE, given IF is passed
    else:
        print("Initial deposit must be >= $1500. Try Again!!!")

balance += initial_Deposit

transaction_chk = 'Y'
print("Please create a transaction")
transaction_boo = True

while transaction_boo:
    if (transaction_chk == 'Y' or transaction_chk == 'y'):
        type = (input("Credit or Debit: (C or D): "))
        amnt = float(input("Enter your amount: "))
        
        if(type == 'C' or type == 'c'):
            balance += amnt
        elif(type == 'D' or type == 'd'):
            balance -= amnt

    elif(transaction_chk == 'N' or transaction_chk == 'n'):
        break
    else:
        print("Enter a valid resposne!!")

    transaction_chk = (input("Do you wish to make a transaction? Y/N: "))
    if(transaction_chk == 'N' or transaction_chk == 'n'):
        transaction_boo = False

print("Final Balance: $",balance)
