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

try:
  number = int(input("Nombre : "))
  occurrences = 0

  for element in my_list:
    
    if number == element:
      occurrences += 1
  
  print(f"Le nombre apparaît {occurrences} fois.")

except ValueError:
  print('Format invalide !')
