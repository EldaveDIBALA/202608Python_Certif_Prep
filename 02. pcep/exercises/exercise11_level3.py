'''
Exercice 11 — Modifier une liste

Crée :

["chat", "chien", "lapin", "poisson"]

Puis :

remplace "lapin" par "hamster" ;
affiche la liste ;
ajoute "tortue" à la fin ;
affiche à nouveau la liste.
'''

liste = ["chat", "chien", "lapin", "poisson"]

liste[2] = "hamster"
print(liste)
print()

liste.append("tortue")
print(liste)
