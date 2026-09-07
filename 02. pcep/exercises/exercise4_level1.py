'''
🟢 Niveau 1 — Révision des bases
Exercice 4 — Table de multiplication

Demande un nombre et affiche sa table de multiplication de 1 à 10.
'''

number = int(input("Entrez le nombre à multiplier. \nNombre = "))
print()

for i in range(1, 11):
  print(f"{number} X {i} = ", number * i)

