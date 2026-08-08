print("Pour l'addition :", 2 + 2.3)
print()
print("Pour la soustraction :", 1960 - 2026)
print()
print("Pour la multiplication :", 2 * 8.1)
print()
print("Pour la division :", 10 / 3)
print()
print("Pour la division des integers :", 10 // 3)
print()
print("Pour le pourcentage :", 20 % 1000)
print()
print("Pour l'exponenciation :", 2 ** 2.05)

# Arithmetic operators: * exponentiation *
## Pour Python : a ** b => c'est a puissance b
## Si a & b sont des integers, le résultat le sera aussi.
## Si a ou b est un décimal, le résulat sera un décimal aussi.

# Arithmetic operators: * multiplication *
## Pour Python : c * d => c'est c multiplié par d
## Les mêmes règles s'appliquent sur le type de valeurs influençant le résultat

# Arithmetic operators: * division *
## Pour Python : e / f => c'est e divisé par f
## Ici, le résultat sera toujours un décimal, peu importe la nature des valeurs de l'opération.


# Arithmetic operators: * integer division * ou encore * floor division *
## Le résultat sera toujours arrondi. Pas de décimaux.
## Elle s'applique aux règles des enties et aux décimaux
## Par exemple :

print()
print(6 // 4) # tendra vers 1 parce que c'est l'entier positif le plus proche
print(6. // 4) # tendra vers 1.0 parce que c'est l'entier positif le plus proche
print(6 // 4.) # tendra vers 1.0 parce que c'est l'entier positif le plus proche

## Par contre :

print()
print(-6 // 4) # tendra vers -2 parce que c'est l'entier négatif le plus proche
print(-6 // 4.) # tendra vers -2.0 parce que c'est l'entier négatif le plus proche
print(6. // -4) # tendra vers -2.0 parce que c'est l'entier négatif le plus proche

# Operators: remainder (modulo)
## Il évalue le reste après la division entre nombres entiers.
print()
print(14 % 4) # Donne 2 => 14/4 = 3 ; 3X4 = 12 ; 14-12 = 2.
print(12 % 4.5) # Donne 3.0 en suivant la même règle.
