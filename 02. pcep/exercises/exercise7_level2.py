'''
Exercice 7 — Somme

Demande un nombre N et calcule :

1 + 2 + 3 + ... + N

Affiche le résultat.
'''

N = int(input("N = "))
somme = 0

for i in range(1, N + 1):
  somme += i
  
print(f"Résultat de 1 + ... + {N} : {somme}")
