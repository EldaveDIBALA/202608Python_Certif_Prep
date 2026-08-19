from datetime import date

# Comparison: equality operator

print("Bonjour ! Nous avons besoin de quelques informations pour procéder.")
reponse = input("Cela ne vous dérange pas, j'espère ?" + "\nEntrez votre réponse : ")
print()

if reponse == "Non":
    a = int(input("Quel est votre année de naissance, s'il vous plaît ?" + "\nEntrez votre réponse : "))
    print()
    print("C'est noté ! Je vous remercie.")

    annee_actuelle = date.today().year
    age = annee_actuelle - a
    
    if age >= 18:
        print("Vous êtes en âge de voter et de conduire.")
    else:
        print("Prenez le temps de grandir. Tout vient à point à qui sait attendre. 🙂")
        print()
else:
    print("Je ne vous retiens pas plus longtemps.", "\nBonne continuation.")
    print()


# LAB 1
n = int(input())
print(n >= 100)
print()

# Une idée prise sur le net

for i in range(5, 0, -1):
    print("*" * i)

for j in range(2, 6, +1):
    print("*" * j)

print()

# Solution prise en ligne
n = 7

for i in range(2 * n - 1):
    for j in range(2 * n - 1):

        # Distance par rapport au centre
        if abs(i - (n - 1)) + abs(j - (n - 1)) < n:
            print(" ", end="")
        else:
            print("*", end="")

    print()


