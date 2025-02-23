# Exercise: Write a program that asks the user for the purchase amount. If the amount is above $100, 
#           offer a 10% discount and print the discounted price. Otherwise, print the original price.
print("Pretend you're buying something but if it cost more than 100$, there will be 10 percent discount")
purchase = int(input("Purchase amount: "))
if purchase > 100:
    print("You get 10 percent discount!!")
    purchase = purchase * 0.9
    print(f"Price after discounted: {purchase}")
else:
    print(f"Purhcase amount: {purchase}")