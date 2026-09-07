'''
🟢 Niveau 1 — Révision des bases
Exercice 1 — Pair ou impair

Demande un nombre à l'utilisateur et affiche :

"Pair" s'il est divisible par 2
"Impair" sinon.
'''

number = int(input('Indiquez un nombre. \nRéponse : '))

if number % 2 == 0:
  print("Le nombre est pair.")
else:
  print("Le nombre est impair")
