# Exercise: Write a program that asks the user for their score (out of 100). Assign a letter grade based 
#           on the score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
print("We'll provide a letter grade based on score you input")
score = int(input("Please enter your score: "))
def score_grade(score):
    if score < 60:
        return "You got F."
    elif score < 70:
        return "You got D."
    elif score < 80:
        return "You got C."
    elif score < 90:
        return "You got B."
    elif score < 100:
        return "You got A."
print(score_grade(score)) # If they inout more than 100, then Python will display 'None' not error.