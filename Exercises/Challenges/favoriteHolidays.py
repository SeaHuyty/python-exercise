# Exercise:  Write a C program that prompts the user to choose their favorite holiday event from a list 
#            and displays information about the selected event. For example: 
#             Choose your favorite holiday event:
#             1. International New Year Day
#             2. Day of Victory over the Genocidal Regime
#             3. International Women's Rights Day
# Enter the number of your favorite holiday event: 3
# Your favorite holiday event is International Women's Rights Day, which falls on 08 Mar.
event = ["International New Year Day", "Day of Victory over the Genocidal Regime", "International Women's Rights Day", 
"Halloween", "Christmas", "Valentine's Day"]
print("Choose your favorite holiday event from the list below")
for i, day in enumerate(event):
    print(f"  {i+1}. {day}")
select = int(input("Please enter the number of your favorite holiday: "))
def selected_case(select):
    if select == 1:
        return "\nInternational New Year’s Day is celebrated on January 1st each year. It marks the start of a new calendar year in the Gregorian calendar, which is used by most countries around the world. This day is a public holiday in many countries, making it one of the most widely observed holidays globally. Celebrations typically include fireworks, parades, concerts, and other festive events.\n"
    elif select == 3:
        return "\nInternational Women’s Day (IWD) is celebrated annually on March 8. It serves as a focal point in the women’s rights movement. The day is dedicated to honoring the achievements of women and promoting women’s rights. It gives focus to issues such as gender equality, reproductive rights, and violence and abuse against women.\n"
    elif select == 2:
        return "\nThe “Day of Victory Over Genocide” is a significant day observed in Cambodia on January 7th each year. This day commemorates the end of the Khmer Rouge regime in 1979.\n"
    elif select == 4:
        return "\nHalloween, also known as Allhalloween, All Hallows’ Eve, or All Saints’ Eve, is a celebration observed in many countries on October 31. This date marks the eve of the Western Christian feast of All Hallows’ Day.\n"
    elif select == 5:
        return "\nChristmas is a Christian holiday that celebrates the birth of Jesus Christ. It is observed annually on December 25th. The term “Christmas” means “The Mass of Christ” and is also a cultural holiday for many non-Christians all over the world.\n"
    elif select == 6:
        return "\nValentine’s Day, also known as Saint Valentine’s Day or the Feast of Saint Valentine, is celebrated annually on February 14th. It originated as a Christian feast day honoring a martyr named Valentine. Through later folk traditions, it has also become a significant cultural, religious, and commercial celebration of romance and love in many regions of the world.\n"
print(selected_case(select))