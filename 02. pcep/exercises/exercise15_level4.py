'''
🔵 Niveau 4 — Listes + logique
Exercice 15 — Trouver le maximum

À partir d'une liste comme :

[12, 5, 27, 3, 19, 8]

trouve le plus grand nombre avec une boucle.

Essaie de ne pas utiliser directement une fonction qui donne le maximum.
'''

liste = []
list_length = int(input("list length: "))
  
for i in range(list_length):
  nombre = int(input(f"Nombre {i + 1} : "))
  liste.append(nombre)

print(f"\nListe : {liste}")

if liste:
  
  nombre_max = liste[1]
  
  for nombre in liste:
    if nombre >= nombre_max:
      nombre_max = nombre
      
  print(f"Le nombre max est : {nombre_max}.")

else:
  print("Il faut entrer des nombres à comparer.")
