##################################################################################################################

# break statement & continue statement

print("""
##################################################################################################################
#                   SIMULATEUR DE BUDGET POUR TRAVAILLER LE BREAK & LE CONTINUE STATEMENT                        #
##################################################################################################################
""")

import sys
from decimal import Decimal
import time
from datetime import datetime
import re

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

print(f"\n{'-' * 114}")

##################################################################################################################

# 


print("""
##################################################################################################################
#                   SIMULATEUR DE BUDGET POUR TRAVAILLER LE BREAK & LE CONTINUE STATEMENT                        #
##################################################################################################################
""")

print(f"\n{'-' * 114}")

##################################################################################################################
