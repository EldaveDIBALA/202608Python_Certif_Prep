x = int(input("Entrer un chiffre : "))
print()

if x == 10:
    print("x == 10")

if x > 15:
    print("x > 15")

elif x > 10:
    print("x > 10")

elif x > 5:
    print("x > 5")

else:
    print("else will not be executed")
print()

##########################################################################################

x = int(input("Entrer un autre chiffre : "))
print()

if x > 5:
    if x == 6:
        print("nested: x == 6")
    elif x == 10:
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")
print()

##########################################################################################

x, y, z = 5, 10, 8 # Je prends cet exemple pour enrichir ma notation des assignations

print(x > z)
print((y - 5) == x)

exit()
