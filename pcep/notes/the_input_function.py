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
