# Exercise: Organize a small program.
# Then import it to another file.
import utilis
from utilis import find_maxi
numbers = [10, 20, 40, 32]
maximum = find_maxi(numbers)
print(maximum)

# Since Python have the function that help us find the maximum number.
# We can find it easily by using the (max) function.
print(max(numbers))