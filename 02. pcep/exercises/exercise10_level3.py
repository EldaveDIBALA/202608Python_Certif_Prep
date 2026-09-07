'''
🟠 Niveau 3 — Premiers exercices avec les listes
Exercice 10 — Créer une liste

Crée une liste contenant 5 nombres.

Puis affiche :

la liste entière ;
son premier élément ;
son dernier élément ;
son deuxième élément.

Attention : réfléchis aux index.
'''

liste = []
i = 0

while i <= 4:
  i += 1
  num = int(input("Nombre = "))
  liste.append(num)

print(liste)
print()

print(liste[0])
print()

print(liste[4])
print()

print(liste[1])
