weather = float(input("Bonjour à vous." + "\nQuelle température il fait aujourd'hui ?" + "\nIl fait : "))
print()

if weather in range(18, 22):
    print("Très bien, je vous remercie." + "\nIl fait assez bon pour une promenade 🙂.")
elif weather < 18:
    print("Impossible de sortir avec ce froid de canard." + "\nMerci à vous pour le temps accordé.")
else:
    print("Il fait trop chaud dehors, alors." + "\nIl y a donc un risque de canicule." + "\nMerci à vous.")
print()

#############################################################################################################

demande_visa = "En attente de réponse."
visa = input("Avez-vous obtenu votre visa ?" + "\nRéponse : ")
demarche = "Statut démarche : En cours."

if visa == "Oui":
    print("Félications !" + "\nVotre réservation de logement est confirmée.")
elif visa == demande_visa:
    print("Revenez quand vous aurez récupéré votre passeport auprès du Consulat.")
print(demarche) # S'affichera toujours, parce que hors de la boucle de conditions.

#############################################################################################################
