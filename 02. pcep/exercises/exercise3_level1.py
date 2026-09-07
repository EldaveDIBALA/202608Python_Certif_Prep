'''
🟢 Niveau 1 — Révision des bases
Exercice 3 — Le plus grand

Demande deux nombres à l'utilisateur et affiche le plus grand.

Si les deux sont égaux, affiche un message approprié.
'''

number1 = float(input("\nQuel est le premier nombre ? Nombre 1 = "))
number2 = float(input("Quel est le second ? Nombre2 = "))

if number1 > number2:
  print(f"{number1} est plus grand que {number2}.")
else:
  print(f"{number2} est supérieur à {number1}.")
