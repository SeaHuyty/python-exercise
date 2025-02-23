# Exercise: (Bonus) You're building a simple program for a small online fruit store. But with a twist - the password to access the store is a secret number!
# Instructions:
# 1. Welcome and Login (using if-else):
# − Greet the user and ask them to enter a password (integer).
# − Define a correct integer password (e.g., 1234).
# − Use an if-else statement to check if the entered password matches the correct password.
# − If correct, grant access to the store.
# − If incorrect, display an error message and ask to try again (provide a limited number of attempts, e.g., 3).
# 2. Product Selection (using switch):
# − Display a menu listing available fruits (e.g., 1 - Apple, 2 - Banana, 3 – Orange, etc.) 
#   with their corresponding prices (store prices in integer variables).
# − Ask the user to enter a number to select a fruit.
# − Use a switch statement to handle user selection.
#   o For each fruit selection, display the chosen fruit and its price.
# 3. Quantity (using loop): 
# − Ask the user to enter the desired quantity of the chosen fruit (integer).
# − Use a while loop to ensure the user enters a positive quantity (greater than 0).
# 4. Receipt (using printf): 
# − Calculate the total cost (quantity * price).
# − Use printf statements to display a small receipt:
#   o Purchased item and quantity
#   o Total price
#   o Thank you message.
# This exercise reinforces concepts like variables, data types (int, float), operators (comparison, arithmetic), 
# input/output functions (scanf, printf), control statements (if-else, while), and basic decision making (switch).
print("This is a small online fruit store program.\n")
print("-----Welcome to Online Fruit Store-----")
i = 0
while i != 1:
    password = int(input("Please enter your password (1234): "))
    if password == 1234:
        i = 1
    else:
        print("Incorrect Password!!\nTry again!!")
print("\tMenu of our fruit today")
fruits = ["a. Apple", "b. Banana", "c. Cocaine", "d. Dragon Fruit"]
for name in fruits:
    print(name)
select = str(input("=> Select a fruit you want to purchase: "))
def fruit_selected(select):
    if select.lower() == 'a':
        apple = {
            "quantity": 30,
            "price": 0.50
        }
        print(f"Fruit name: Apple\nFruit Quantity: {apple["quantity"]}\nFruit Price: {apple["price"]}$/apple")
        k = 0
        while k != 1:
            purchase_amount = int(input("Quantity you want to purchase: "))
            if purchase_amount > apple["quantity"]:
                print(f"We do not have more than {apple["quantity"]}")
            else:
                k = 1
        cost = purchase_amount * apple["price"]
        print("-----------------------")
        print("\tReciept\n-----------------------")
        print(f"Purchased item: Apple\nPurchased quantity: {purchase_amount}\nTotal Price: {cost}$\nTHANK YOU!!")
    elif select.lower() == 'b':
        banana = {
            "quantity": 25,
            "price": 1
        }
        print(f"Fruit name: Banana\nFruit Quantity: {banana["quantity"]}\nFruit Price: {banana["price"]}$/banana")
        k = 0
        while k != 1:
            purchase_amount = int(input("Quantity you want to purchase: "))
            if purchase_amount > banana["quantity"]:
                print(f"We do not have more than {banana["quantity"]}")
            else:
                k = 1
        cost = purchase_amount * banana["price"]
        print("-----------------------")
        print("\tReciept\n-----------------------")
        print(f"Purchased item: Banana\nPurchased quantity: {purchase_amount}\nTotal Price: {cost}$\nTHANK YOU!!")
    elif select.lower() == 'c':
        print("I'm just kidding, We don't sell Cocaine or any kinds of drug here!!")
    elif select.lower() == 'd':
        dragon_fruit = {
            "quantity": 50,
            "price": 0.75
        }
        print(f"Fruit name: Dragon Fruit\nFruit Quantity: {dragon_fruit["quantity"]}\nFruit Price: {dragon_fruit["price"]}$/dragon fruit")
        k = 0
        while k != 1:
            purchase_amount = int(input("Quantity you want to purchase: "))
            if purchase_amount > dragon_fruit["quantity"]:
                print(f"We do not have more than {dragon_fruit["quantity"]}")
            else:
                k = 1
        cost = purchase_amount * dragon_fruit["price"]
        print("---------------------------")
        print("\tReciept\n---------------------------")
        print(f"Purchased item: Dragon Fruit\nPurchased quantity: {purchase_amount}\nTotal Price: {cost}$\nTHANK YOU!!")
print(fruit_selected(select))