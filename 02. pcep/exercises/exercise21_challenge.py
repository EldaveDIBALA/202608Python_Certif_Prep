'''
🏆 Challenge final — first_unique

Écrire une fonction first_unique(character) qui retourne le premier caractère apparaissant une seule fois 
dans une chaîne, ou None s'il n'y en a aucun.

Par exemple, tu peux tester mentalement :

"swiss"   → "w"
"aabbcc"  → None
"python"  → "p"
"programming" → ...
'''

def first_unique(character):

    occurrences = {}
    
    for i in character:
        
        if i in occurrences:
          occurrences[i] += 1
        else:
          occurrences[i] = 1
    
    for i in character:     
        if occurrences[i] == 1:
          return i
    
    return None

chain = input("\nChaîne de caractères : ")
result = first_unique(chain)
print(result)
