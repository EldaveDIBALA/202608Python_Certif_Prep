'''
Exercice 14 — Compter les nombres pairs

À partir d'une liste de nombres, compte combien de nombres sont pairs.

Exemple :

[3, 8, 12, 5, 7, 10]

Résultat attendu :

3
'''

liste = []
compteur = 0

for i in range(int(input("Combien de nombres pour la liste ? "))):
  nombre = int(input(f"Nombre {i + 1} : "))
  liste.append(nombre)
  
  if nombre % 2 == 0:
    compteur += 1
  
print(f"\nListe de nombres : {liste}")

print(f"Résultat attendu : {compteur}\n")
