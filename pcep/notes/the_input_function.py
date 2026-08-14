# La fonction input() est capable de lire la donnée entrée par l'utilisateur
# et de renvoyer la même donnée au programme en exécution.
print("Bonjour ! Dis-moi tout ...")
tout = input()
print("Hmm...", tout, "...vraiment ?!")
print()

# Type casting
annee_de_naissance = float(input("Quelle est ton année de naissance : "))
age_cette_annee = 2026 - annee_de_naissance
print("Cette année, vous avez :", age_cette_annee, " ans.")
print()

# Un peu plus loin avec le Type casting et la fonction input()
sin = float(input("Entrez la valeur du côté A du triangle rectangle ABC : "))
cos = float(input("Entrez la valeur du côté B du triangle rectangle ABC : "))
print("L'hypothénus du triangle rectangle ABC est long de :", ((sin ** 2) + (cos ** 2)) **.5)
print()

# String operators - introduction
name = input("Puis-je avoir votre nom, s'il vous plaît?")
firstname = input("Puis-je avoir votre prénom, s'il vous plaît?")
print("Je vous remercie.")
print("\nVous avez", age_cette_annee, "ans d'âge, cette année." + "\nEt Votre nom est donc", firstname, name, sep=" ")
print()

# Replication
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
print()

print(" " * 6 + "*")
print(" " * 3 + " " + "/" + " " * 3 + "\\")
print(" " * 2 + " " + "/" + " " * 4 + " \\")
print(" " * 3 + "=" * 7)
print(" " + "/" + " " * 8 + " \\")
print("/" + " " * 10 + " \\")
print()

# Conversion d'un Integer enn String
print("Je suis né en " + str(1990) + " à Brazzaville.")
print()


# LAB 1
# input a float value for variable a here
a = float(input("Entrez la valeur de a :"))

# input a float value for variable b here
b = float(input("Entrez la valeur de b :"))
print("\nJe vous remercie.")

# output the result of addition here
print("La somme entre a et b est :", a + b)

# output the result of subtraction here
print("La soustraction entre a et b est :", a - b)

# output the result of multiplication here
print("La multiplication entre a et b est :", a * b)

# output the result of division here
print("La division de a par b est :", a / b)

print("\nThat's all, folks!")

# LAB 2
x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + (1 / x)))) # Write your code here.

print("y =", y)
print()

# LAB 3
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
# Convert start time to total minutes since midnight
total_mins = hour * 60 + mins
# Add duration
end_total_mins = total_mins + dura
# Convert back to hours and minutes
end_hour = end_total_mins // 60 % 24
end_min = end_total_mins % 60

print(f"{end_hour:02d}:{end_min:02d}")
print()
