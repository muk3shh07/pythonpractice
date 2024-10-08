balance = 80000


print("Welcome to NIMB Pvt. Ltd.")
while(True):
    inputText = """
What do you want to perform?
1.Check Balance.
2.Deposit Money.
3.Cash Withdrawl.
4.Exit
"""
    userInput = int(input(inputText))

    if userInput == 1:
        print(f"Your Current balance is {balance}")
    elif userInput == 2:
        deposit_amt = float(input("Enter the Deposit amount::"))
        balance= balance + deposit_amt
        print(f"The Amount is successfully deposited in your acc. and your current balance is:${balance:.2f} ")
    elif userInput == 3:
        withdrawl_amt = int(input("Enter the amount you want withdraw::"))
        if withdrawl_amt > balance:
            print("Sorry! Insufficient Amount")
        else:
            balance-= withdrawl_amt
            print("Your amount is succesfully withdrawaled")
            print(f"And your current balance is:${balance:.2f}")
    elif userInput==4:
        print("Thank you!!")
        break
    else:
        print("Invalid Choice")    

