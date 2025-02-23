# For loop:
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item) # Display the number in the list. It's so short that it's hard to understand.
for item in 'Python':
    print(item)
for thing in [1, 2, 3, 4, 5, 6]: # But we don't need to do like this. We can use range().
    print(thing) # We can print a list like this with not need to declare a list above.
for names in ['Laura', 'Jesaxa', 'Sadra']:
    print(names)
for number in range(1, 11):
    print(number)
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    # We can create a list above and display number of string according to the value.
    print('x' * i) 