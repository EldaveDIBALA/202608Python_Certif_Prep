print(__name__)
print()

print("/Users/eldavedibala/Documents/Engineer/SDET/202608Python_Certif_Prep/pcep/notes")
print()

print(__file__)
print()

var = 2026
print(var - 1990)
print()

var = var + 1
print(var - 1990)
print()

# Le théorème de Pythagore appliqué au triangle rectangle ABC :

cote_ab = 5
cote_bc = 12
hypothenus = (cote_ab ** 2 + cote_bc ** 2) ** .5
print("Les valeurs des côtés AB et BC étant égale respectivement à", cote_ab, "et", cote_bc, ", alors l'hypothénus est égale à :", hypothenus)
print()


# Shortcut operators

x = 18
x = x * 2 # x = 36

y = 18
y *= 2 # y = 36

ab = 1990
ab = ab + 36 # ab = 2026

bc = 1990
bc += 36 # bc = 2026

print("En utilisant les raccourcis, x = y et ab = bc")
print()
print("En voici la preuve :", "\nx = ", x, ";\ny = ", y, ";\nab =", ab, ";\net bc =", bc, end="\n")
print()

# LAB

x = float(input("Quelle valeur veux-tu assigner à x ?\n"))
print("\nx =", x)
print()

y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
print("y =", y)
print()
