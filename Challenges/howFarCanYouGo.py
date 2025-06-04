def howFarCanYouGo(mainTank, secondaryTank):
    # Calculate the fuel that will be transfered for every 5 litres of fuel we used in the main tank.
    transferableFuel = int(mainTank / 5)
    # There's a problem because sometimes the amount of fuel that need to be transferred is not enough.
    # Solution is we have to adjust the transfer amount.
    if transferableFuel > secondaryTank:
        transferableFuel = int(secondaryTank)
    # Amount of fuel we have includes the fuel
    fuelUse = transferableFuel + mainTank
    # The power of a litre of fuel can travel.
    fuelPower = 10
    # Calculate how far we can go with the amount of fuel and its power.
    distance = fuelUse * fuelPower
    return distance

# We use loop here to let user input the number again when they made mistakes.
# i = 0 uses to make the loop continues, in fact we can put any numbers except i = 1.
i = 0
while i != 1:
    # We use exception here to catch error when user input any invalid value or values that are not integer.
    try:
        # We let user input integer number and store it in 'mainTank'.
        mainTank = int(input("Enter fuel in the main tank: "))
        if mainTank <= 0:
            print("Main tank can't be 0 or less than zero.\n")
        else:
            # Here we give the value i = 1 to terminate the loop when user've input the correct value.
            i = 1
    except ValueError:
        # We display a text to tell them that they've input invalid value.
        print("Invalid Value!!\n")
        
# Same process apply to store and catch errors for the secondary tank.
k = 0
while k != 1:
    try:
        secondaryTank = int(input("Enter fuel in the secondary tank: "))
        if secondaryTank > 100 or secondaryTank < 0:
            print("Secondary tank can't be over 100 or less than zero.\n")
        else:
            k = 1
    except ValueError:
        print("Invalid Value!!\n")

# Here we call the function to use and display some words to tell them what it is.
print(f"\nYou're able to travel {howFarCanYouGo(mainTank, secondaryTank)} km\n")