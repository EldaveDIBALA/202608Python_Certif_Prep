'''
Exercice 8 — Compter les voyelles

Demande une chaîne de caractères et compte combien elle contient de :

a, e, i, o, u

Tu peux considérer uniquement les minuscules pour commencer.
'''

chaine_de_caractere = input("Une chaîne de caractère : ").lower()
lettres = "aeiou"
compteur = 0

for i in chaine_de_caractere:
  
  if i in lettres:
    compteur += 1
    
print(compteur)
