plant = input("What is the name of your plant? ")

if plant == "Spathiphyllum":
    print("\nYes - Spathiphyllum is the best plant ever!")
    exit()
elif plant == "spathiphyllum":
    print("\nNo, I want a big Spathiphyllum!")
else:
    print(f"\nSpathiphyllum! Not {plant} !") # print("Spathiphyllum! Not " + plant + "!")
print()

########################################################################################################

income = float(input("Enter the annual income: "))
print()

print(f"Your annual income is evaluated at {income}" + "\nThank you.")

if income <= 85528:
    tax = (.18 * income) - 556.02
    if tax < 0:
        tax = 0.
elif income > 85528:
    tax = 14839.02 + (.32 * (income - 85528))
else:
    tax = 0.
#

tax = round(tax, 0)
print("\nThe tax is:", tax, "thalers")
print()

########################################################################################################

year = int(input("Enter a year: "))
print()

#
if year >= 1582:
    if year % 4 != 0:
        print("Common year")
        print()
    elif year % 100 != 0:
        print("Leap year")
        print()
    elif year % 400 != 0:
        print("Common year")
        print()
    else:
        print("Leap year")
        print()
else:
    print("Not within the Gregorian calendar period")
    print()

########################################################################################################
	
