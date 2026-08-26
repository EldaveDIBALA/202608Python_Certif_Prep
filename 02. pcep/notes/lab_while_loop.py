from decimal import Decimal 

# Petit exercice conçu par moi pour travailler le while loop

i = 0
i = int(input("\nEntrez une valeur de i : "))

if i < 10:
    print(f"Pour commencer, vous avez attribué à i la valeur {i} qui est inférieure à 10.")
    while i < 10:
        i = int(input("\nEntrez donc une nouvelle valeur de i : "))
        i += 1
        print(f"\ni est maintenant égale à {i} après exécution.")
        if i >= 10:
            print("Et sa valeur est supérieure ou égale à 10. Le programme doit s'arrêter.\n")
        else:
            print("Et sa valeur est inférieure à 10. Le programme peut donc continuer son exécution.\n")
else:
    print("i est supérieure ou égale à 10. Le programme doit s'arrêter prématurément.\n")

print(f"\n{'#' * 80}")

############################################################################################################################

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

number = int(input("\nEntrez un nombre entier ou tapez 0 pour arrêter le comptage : "))
print("Merci 🙂 !")

while number: # On peut aussi écrire cette condition de la manière suivante : 'while number != 0:'
    if number % 2 == 1:
        odd_numbers += 1
        if odd_numbers > 1:
            print("\nJusqu'ici nous comptons", odd_numbers, "nombres impairs")
        else:
            print("\nJusqu'ici nous comptons", odd_numbers, "nombre impair.")
    else:
        even_numbers += 1
        if even_numbers > 1:
            print("\nJusqu'ici nous comptons", even_numbers, "nombres pairs.")
        else:
            print("\nJusqu'ici nous comptons", even_numbers, "nombre pair.")
    number = int(input("Entrez un autre nombre entier ou tapez 0 pour arrêter le comptage : "))
else:
    print("\nC'est compris 👍.", f"\nVous avez tapé {number} afin d'arrêter le comptage.", f"\nEt nous avons compté au total {even_numbers} nombre(s) pair(s) et {odd_numbers} nombre(s) impair(s).\n", "\nNous vous souhaitons une agréable journée.")

print(f"\n{'#' * 80}")

############################################################################################################################

print(
"""
+=============================================================================+                          
| Développer un script Python interactif pour gérer un budget mensuel en      |
| déduisant des dépenses successives à partir d'un salaire initial.           |
| Pour garantir une précision financière absolue au centième près, le         |
| programme  doit utiliser le module decimal et formater chaque affichage     |
| avec strictement deux chiffres après la virgule.Une boucle interactive doit |
| être mise en place pour enregistrer les dépenses, tout en acceptant les     |
| confirmations de l'utilisateur sous toutes leurs formes (majuscules,        |
| minuscules, espaces). Le système doit automatiquement interrompre son       |
| exécution si le solde devient nul ou négatif, ou si l'utilisateur choisit   |
| volontairement de s'arrêter. Enfin, le programme doit se clôturer           |
| proprement en affichant le solde final accompagné d'un message de           |
| courtoisie.                                                                 |
+=============================================================================+
""")

# 1. Utilisation directe de Decimal pour éviter les bugs financiers
salary = Decimal(input("\nQuel est votre salaire ce mois-ci ? "))

# La boucle tourne à l'infini jusqu'à un 'break' volontaire
if salary != 0 and input("Voulez-vous poursuivre ? ").lower().strip() in ["oui", "ou", "o", "u", "i", "iou", "iuo"]:
    while salary: 
        # Étape 1 : Demande s'il y a des dépenses
        if input("\nAvez-vous dépensé ces derniers jours ? ").lower().strip() in ["oui", "ou", "o", "u", "i", "iou", "iuo"]:
            expense = Decimal(input("À hauteur de combien ? "))
            salary -= expense
            print(f"\nIl vous reste {salary:.2f} euros sur votre salaire.")
            
            # Sécurité : Si le solde atteint 0, on s'arrête immédiatement
            if salary <= 0:
                print(f"Solde actuel : {salary:.2f}€ \nBonne journée 🙂.")
                break
                
            # Étape 2 : On demande si on veut continuer après une dépense
            elif input("Voulez-vous continuer ? ").lower().strip() in ["oui", "ou", "o", "u", "i", "iou", "iuo"]:
                print("D'accord.")
                
            else:
                print(f"\nSolde actuel : {salary:.2f}€", "\nBonne journée 🙂.")
                break
                
        else:
            # Si l'utilisateur ne répond pas "Oui" à la question des dépenses
            print(f"Solde actuel : {salary:.2f}€ \nBonne journée 🙂.")
            break

    print("Merci d'avoir utilisé nos services. 🙏")
else:    
    print(f"\nSolde actuel : {salary:.2f} €. 😢")

print(f"\n{'#' * 80}")

############################################################################################################################

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number_picked = int(input("Enter an integer number: "))

while number_picked != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number_picked = int(input("\nEnter an integer number: "))
print(number_picked, "\nWell done, muggle! You are free now.")

print(f"\n{'#' * 80}")
exit()
