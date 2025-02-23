# Logical Operator: We use this operator to build complex rules and operations.
price = 30
print(price > 15 and price < 40) # If both conditions are true then the result would be true.
print(price > 15 or price < 20) # If one of these conditions is true then the result would be true.
print(not price > 40) # It means that price is not greater than 40. And it'll display true.
has_high_income = True
has_good_credit = True
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligible for loan")
if has_good_credit and not has_criminal_record:
    print("Good Citizen")