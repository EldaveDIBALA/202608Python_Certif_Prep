'''
Exercice 9 — Trouver un caractère

Demande une chaîne et un caractère.

Indique si ce caractère apparaît dans la chaîne.

Exemple :

Chaîne : ordinateur
Caractère : t

Le caractère existe.
'''

chaine_de_caractere = input("Une chaine de caractères : ").lower()
un_caractere = input("Un caractère : ").lower()

if len(un_caractere) == 1:
  
  if un_caractere in chaine_de_caractere:
    print("\nLe caractère existe.")
  else:
    print("\nLe caractère n'existe pas.")
    
else:
  print("Un caractère ...")
