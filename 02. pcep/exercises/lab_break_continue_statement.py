import sys
from decimal import Decimal
import time
from datetime import datetime
import re

##################################################################################################################

word_without_vowels = ""
vowels = ("A", "E", "I", "O", "U" )

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ").upper()

for letter in user_word:
    # Complete the body of the loop.
    if letter in vowels:
        continue    
    else:
        word_without_vowels += letter
    
# Print the word assigned to word_without_vowels.
print(word_without_vowels)

print(f"\n{'*' * 114}")

#################################################################################################################

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Check if the letter is a vowel
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        # Print non-vowel letters
        print(letter)

print(f"\n{'*' * 114}")

#################################################################################################################

"""
Your program must:

- ask the user to enter a word;
- use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
- use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
- print the uneaten letters to the screen, each one of them on a separate line

"""

sys.exit() # À commenter si je veux exécuter le code ci-dessous.

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("\nEnter a word: ").upper()
user_word_last = ""

# Complete the body of the for loop.

voyelles = (
    "A", "À", "Â", "E", "É", "È", "Ê", "Ë", 
    "I", "Î", "Ï", "O", "Ô", "U", "Ù", "Û", "Ü", "Y", "Ÿ"
)

letter_eaten = ""
compteur_voyelles = 0

# VÉRIFICATION : Est-ce qu'au moins une des voyelles est dans le mot ?

time.sleep(2)

while not any(v in user_word for v in voyelles):
    print("Votre mot doit contenir au moins une voyelle.")
    
    if input("✋🏾 Voulez-vous en entrer un autre ? ").lower() == "non":
        print("\nVous devez entrer un mot valide.\n")
        time.sleep(2)
        print("🚦 Arrêt du programme.")
        sys.exit()
    time.sleep(2)
    user_word = input("\nEnter a word: ").upper()

# Si le programme continue, c'est que le mot contient bien des voyelles

for letter in user_word:

    if letter in voyelles:
        letter_eaten += letter
        compteur_voyelles +=1
    else:
        user_word_last += letter
    

# Affichage final unique

time.sleep(2)

ma_liste = letter_eaten

ma_liste1 = sorted(ma_liste)

ma_liste2 = set(ma_liste1)

print(f"\nNombre de voyelles collectées : {compteur_voyelles}", f"\nListe de voyelles : {(' ; '.join(ma_liste2))}", end=".\n")

time.sleep(2)
    
print("\nRésultat final :")
print("\n".join(user_word_last))

print(f"\n{'*' * 114}")

sys.exit() # À commenter pour l'exécutions du code ci-après.

##################################################################################################################

# break statement & continue statement

print("""
##################################################################################################################
#                   SIMULATEUR DE BUDGET POUR TRAVAILLER LE BREAK & LE CONTINUE STATEMENT                        #
##################################################################################################################
""")

date_operation = datetime.now().isoformat(timespec='seconds')

salary = Decimal(input("Quel est votre salaire ce mois-ci ? \nRéponse : "))
salaire = int(str(salary))

time.sleep(1)

solde = salary
expense = 0
total_expense = 0

motif_oui = r"^\s*(oui|o|ouais)\s*$"
motif_non = r"^\s*(non|n)\s*$"
motif_invalide = r'[^ouiOUI]'

if salary > 0:
    limit_value = .5 * salaire
    
    epargne = Decimal(input("\nQuel est votre objectif d'épargne mensuel ? \nRéponse : "))
    
    time.sleep(2)
    
    while True:
        expense = Decimal(input("\nCombien avez-vous dépensé ? \nRéponse : "))
        
        total_expense += expense
        solde -= expense

        time.sleep(2)
        
        if total_expense < .2 * salaire:

            answer1 = input("\nVoulez-vous poursuivre Nisi ? \nRéponse : ")
            
            if (match := re.match(motif_non, answer1, re.IGNORECASE)) or (match := re.fullmatch(motif_invalide, answer1, re.IGNORECASE)):
                
                time.sleep(2)
                
                break

            time.sleep(2)
            continue
        
        print(f"\nDate : {date_operation} \nSolde actuel : {solde:.2f} €")
        
        if total_expense >= limit_value:
                print(f"\n🚨 ALERTE : Il ne vous reste plus que {solde} sur votre salaire !")

                time.sleep(2)
                
                print("\n🛑 Arrêt automatique du programme pour protéger votre épargne.")
                
                sys.exit()

        time.sleep(2)

        if solde > 0:

            answer2 = input("\nVoulez-vous poursuivre DIBALA ? \nRéponse : ")
            
            if (match := re.match(motif_non, answer2, re.IGNORECASE)) or (match := re.fullmatch(motif_invalide, answer2, re.IGNORECASE)):

                time.sleep(2)
                
                break
        
            continue
        
        break


        

    time.sleep(2)

    
# Le bout de code ci-dessous est un commentaire multilignes.
    """
    print("""
                #########################################################
                #   🔚 Fin du programme.                                #
                #   🎯 Objectif d'épargne ciblé : {epargne:.2f} €.      #
                #   💵 Solde: {solde:.2f} €.                            #
                #   📆 Date : {date_operation}.                         #
                #########################################################
    """)
    """


    print(f"\n🔚 Fin du programme.")

    time.sleep(2)

    print(f"\n{'#' * 50}")
    
    print(f"\n📆 Date : {date_operation} \n🎯 Objectif d'épargne ciblé : {epargne:.2f} € \n💵 Solde : {solde:.2f} €")
    
    print(f"\n{'#' * 50}")
    
    sys.exit()

time.sleep(2)

print("\nIl vous faut avoir un revenu à budgétiser.")

print(f"\n{'*' * 114}")
    
##################################################################################################################

# Break statement

print("""
##################################################################################################################
#                   SIMULATEUR DE TESTS POUR TRAVAILLER LE BREAK & LE CONTINUE STATEMENT :                       #
##################################################################################################################
""")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


print(f"\n{'*' * 114}")

##################################################################################################################

# Continue statement

print("""
##################################################################################################################
#                   SIMULATEUR DE TESTS POUR TRAVAILLER LE BREAK & LE CONTINUE STATEMENT :                       #
##################################################################################################################
""")

largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    counter += 1
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


print(f"\n{'*' * 114}")

##################################################################################################################

while True:
    if input("Enter a word : ") != "chupacabra":
        time.sleep(2)
        continue
    time.sleep(1)
    print("You've successfully left the loop.")
    break

print(f"\n{'-' * 114}")

##################################################################################################################
