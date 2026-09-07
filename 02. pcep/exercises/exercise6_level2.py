'''
🟡 Niveau 2 — Boucles
Exercice 6 — Compter à l'envers

Demande un nombre N et affiche :

N
N-1
N-2
...
1

Puis affiche :

Décollage !
'''

N = int(input("N = "))
print()

while N > 0:

  print(N)
  N -= 1

print("\nDécollage !")
