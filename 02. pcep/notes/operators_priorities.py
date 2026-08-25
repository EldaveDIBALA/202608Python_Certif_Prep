# La hierarchie des priorités ordonnance l'action de certains opérateurs avant d'autres.
# Par exemple, la multiplication vient avant l'addition.

# Avec Python, le calcul se fait de la gauche vers la droite.
# Par exemple :
print(9 % 6 % 2)
print()

# Operators and their bindings: exponentiation
print(2 ** 2 ** 3)
print()

# Operators and their priorities: multiplication and modulo
print(2 * 3 % 5) # Les deux operations ont la même priorité, donc le calcul se fait de gauche à droite.
print()

# Operators and parentheses: parentheses have the highest priority
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print()
