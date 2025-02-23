# Code to operate in 'organizeSmallProgram.py'
def find_maxi(numbers):
    maxi = numbers[0]
    for number in numbers:
        if number > maxi:
            maxi = number
    return maxi