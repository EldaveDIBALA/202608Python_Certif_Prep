'''
Exercice 18 — Copier les éléments intéressants

À partir de :

[3, 8, 12, 5, 7, 20, 1]

crée une nouvelle liste contenant uniquement les nombres supérieurs à 10.

Résultat attendu :

[12, 20]
'''

numbers = [3, 8, 12, 5, 7, 20, 1]
numbers_greater_than_10 = []

for element in numbers:
  
  if element > 10:
    numbers_greater_than_10.append(element)

print(numbers_greater_than_10)
