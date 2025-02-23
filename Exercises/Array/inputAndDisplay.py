# Exercise: Store n names in an array and display on screen. Ask a user for the number of names then ask for each name.
numbers = int(input("Number of names you want to input: "))
names = [[] for index in range(numbers)]
for index in range(numbers):
    names[index] = str(input(f"Name {index + 1}: "))
print("\nSo these are names you input:")
for i, name in enumerate(names):
    print(f"\t{i+1}. {name}")