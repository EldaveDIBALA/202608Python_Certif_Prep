########################################################################################## 

for i in range(2, 8):
    print("The value of i is currently", i)

print(f"\n{'=' * 90}\n")

##########################################################################################  

for i in range(10):
    print("The value of i is currently", i)

print(f"\n{'=' * 90}\n")

########################################################################################## 

for i in range(2, 100, 10): # Ici 10 est l'incrément.
    print("The value of i is currently", i)

print(f"\n{'=' * 90}\n")

##########################################################################################  

# Un petit exo sur la table de multiplication par le nombre au choix de l'utilisateur

number = int(input("Quel nombre à multiplier ? \nRéponse : "))
resultat = 0
print()

for multiplicateur in range(11):
    resultat = number * multiplicateur
    print("▪️", number, "muliplié par",  multiplicateur, "est égale à", resultat)

print(f"\n{'=' * 90}\n")

########################################################################################## 
 
import time

i = 0

for i in range(6):
    print(i, "Mississippi")
    time.sleep(3)

print("Ready or not, here I come!")

print(f"\n{"=" * 90}\n")
exit()
