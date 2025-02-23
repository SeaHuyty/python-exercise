# Exercise: Read input from user (n) then calculate the multiplication.
multi = int(input("Please enter the number: "))
i = 1
while i <= multi:
    print(f"{multi} x {i} = {i*multi}")
    i += 1