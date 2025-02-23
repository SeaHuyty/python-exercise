# Generating Random Values
import random # random is a built-in module, so we don't need the file name "random.py"
# If you want to find that random modules:
#   Vscode:
#       Go to folder named "Lib">folder named "pip">folder named "_internal".
#       Then find it yourself, there are so many files.
#   Pycharm:
#       Go to folder name "External Libraries">folder named "python3.">folder named "python3. library root".
#       Then find it yourself, there are so many modules in that folder.
for i in range(3):
    # The code below generate random value 3 times.
    print(random.random())
    # To specify our range: The code below generate random value between 10 and 20.
    print(random.randint(10, 20))
# A follow up practice: If we want to find a leader in a group.
members = ["Acadina", "Gwendal", "Roger Skaler", "Saudiora"]
print(random.choice(members))