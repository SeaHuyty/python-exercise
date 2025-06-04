# Exercise:  Simulate a simple ATM. Ask for a PIN and account balance. If the PIN is correct (predefined value), 
#            allow the user to withdraw money. Check if the withdrawal amount is greater than the balance (insufficient funds message).
import os
options = ["Cash Deposit", "Cash Withdrawal", "Exit"]
i = 0
k = 4
money = 100
print("This is an ATM's Terminal Simulation")
while k != 3:
    pin = int(input("Please enter your PIN(6363): "))
    tru_pin = 6363
    if pin == tru_pin:
        k = 3
    else:
        print("Incorrect PIN!!\nPlease try again.")
select = 4
while select != 3:
    print("\nWelcome to our ATM's Terminal Simulation")
    for i, option in enumerate(options):
        print(i+1, option.title())
    select = int(input("=> Select an option: "))
    if select == 1:
        print("\n\t----Cash Deposit----")
        deposit = float(input("Enter amount: "))
        money += deposit
        print("Transaction Completed!!")
        print(f"Your account: {money}")
        # I don't know function that can back in Python, so this deposit option won't work.
        # Let's just initial the money for user.
    elif select == 2:
        while i != 2:
            print(f"\n\t----Cash Withdrawal----\nYour account: {money}$")
            withdraw = float(input("Enter amount you want to withdraw: "))
            if money - withdraw < 0:
                print("\nInsufficient Amount!!")
                # Here we need them to try again
                # So we will use while loop
            else: 
                print("Transaction Completed!!")
                print("\n\t----Reciept----")
                print(f"Withdraw amount: {withdraw} $")
                money -= withdraw
                print(f"Your account: {money} $")
                i = 2
    elif select == 3:
        os.system('cls')
        quit()
    else:
        print("Invalid Option!!")