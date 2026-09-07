'''
🟢 Niveau 1 — Révision des bases
Exercice 2 — Positif, négatif ou zéro

Demande un nombre et affiche :

"Positif"
"Négatif"
"Zéro"
'''
number = float(input('\nQuel nombre : '))

if number == 0:
  print("Zéro")
elif number > 0:
  print("Positif")
else:
  print("Négatif")
