# Nested Loop:

for x in range(4):
    for y in range(3):
        # It displays both number of x and y. But it continues to x loop only when y loop is completed.
        print(f"({x}, {y})")

likes = [1, 1, 1, 1, 5]
for i in likes:
    output = '' # Here we set output to nothing
    for count in range(i): # We can use range like this.
        # We can't set range to range(likes) because list cannot be interpreted as an integer.
        # When likes = 5, it is range(5)
        output += '*'
    print(output)