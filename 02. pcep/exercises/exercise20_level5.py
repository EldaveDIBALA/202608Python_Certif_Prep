'''
🔴 Niveau 5 — Petit challenge
Exercice 20 — Analyse d'une liste

Écris un programme qui travaille avec :

[12, 5, 8, 21, 3, 14, 8, 5, 19]

Ton programme doit afficher :

le nombre d'éléments ;
la somme ;
le plus grand nombre ;
le plus petit nombre ;
le nombre de nombres pairs ;
le nombre de nombres impairs.

Essaie de faire le maximum avec une seule boucle.
'''

my_list = [12, 5, 8, 21, 3, 14, 8, 5, 19]
  
count_even = 0
count_odd = 0
total = 0
element_count = 0

if not my_list:
    print("Liste vide.")

maximum = my_list[0]
minimum = my_list[0]

for number in my_list:
  
    element_count += 1
    total += number

    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    
    if number > maximum:
        maximum = number
    
    if number < minimum:
        minimum = number
    
print(f"Le nombre d'éléments : {element_count}.")
print(f"La somme : {total}.")
print(f"Le plus grand nombre est {maximum}.")
print(f"Le plus petit nombre : {minimum}.")
print(f"Le nombre de nombres pairs : {count_even}.")
print(f"Le nombre de nombres impairs : {count_odd}.")
