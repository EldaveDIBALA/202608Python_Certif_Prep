import sys
import time
import calendar

#############################################################################################################

"""

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat.
The pyramid is stacked according to one simple principle:
    * each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks the builders have,
and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers - if the builders
don't have a sufficient number of blocks and cannot complete the next layer, they
finish their work immediately.

Test your code using the data we've provided.

"""

blocks = int(input("Combien de briques vous avez? \nRéponse : "))

#
# Write your code here.
# 1. Initialiser la hauteur de la pyramide à 0
height = 0

# 2. Initialiser le nombre de blocs nécessaires pour le premier étage (1 bloc)
first_layer = 1

if blocks != 0:
    
    # 3. Créer une boucle 'while' qui tourne TANT QUE le nombre de blocs restants est suffisant pour construire le prochain étage
    while blocks >= first_layer:
        
    # 4. À chaque étape dans la boucle :
    #    - Soustraire le nombre de blocs nécessaires pour l'étage actuel du total de blocs restants
        blocks -= first_layer
        
    #    - Incrémenter la hauteur de la pyramide de 1
        height += 1
        
    #    - Augmenter de 1 le nombre de blocs requis pour l'étage suivant
        first_layer += 1
    #
    time.sleep(2)
    print("\nThe height of the pyramid:", height)
else:
    time.sleep(2)
    print("\n😤 Pas de briques, pas de pyramide !")

print(f"\n{'#' * 80}")

#############################################################################################################

annee = int(input("Entrez l'année de votre choix : "))
mois = int(input("Quel mois vous préferez ? \nRéponse : "))

print("\n", calendar.month(annee, mois))
print(f"\n{'#' * 80}")

#############################################################################################################

"""
Scenario

In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.

Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.


Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

Test your code using the data we've provided.
"""


c0 = int(input("Give me any non-negative and non-zero integer number: "))

steps = 0

while c0 != 1:
    
    if c0 % 2 != 0:
        c0 = 1 + (c0 * 3)
    else:
        c0 //= 2
    
    steps += 1
    print(c0)
    
print(f"steps = {steps}")

print(f"\n{'#' * 80}")

#############################################################################################################

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
    
print(f"\n{'#' * 80}")

#############################################################################################################

i = 1
while i < 5:
    print("\n", i)
    i += 1
else:
    print("\nAlors nous avons atteint :", i)
    
print(f"\n{'#' * 80}")

#############################################################################################################
