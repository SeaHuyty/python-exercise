# Exercise: Get input as a number and print the corresponding month based on the given number (1 for January, 2 for February, etc.)
month = int(input("Input a month number: "))
def switch_case(month):
    if month == 1:
        return "It's January"
    elif month == 2:
        return "It's February"
    elif month == 3:
        return "It's March"
    elif month == 4:
        return "It's April"
    elif month == 5:
        return "It's May"
    elif month == 6:
        return "It's June"
    elif month == 7:
        return "It's July"
    elif month == 8:
        return "It's August"
    elif month == 9:
        return "It's September"
    elif month == 10:
        return "It's October"
    elif month == 11:
        return "It's November"
    elif month == 12:
        return "It's December"
    else:
        return "Invalid Number"
print(switch_case(month))