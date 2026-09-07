'''
Exercice 17 — Compter les occurrences

À partir de :

[2, 5, 2, 8, 5, 2, 9]

demande à l'utilisateur un nombre et indique combien de fois il apparaît.

Exemple :

Nombre : 2
Le nombre apparaît 3 fois.
'''

my_list = [2, 5, 2, 8, 5, 2, 9] 

number = int(input("Enter a number: "))
compteur = 0

for i in my_list:
  if number == i:
    compteur += 1
  else:
    print(f"{number} is not in {my_list}.")
