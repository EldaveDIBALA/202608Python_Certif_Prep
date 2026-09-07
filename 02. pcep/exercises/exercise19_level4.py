'''
Exercice 19 — Inverser une liste

À partir de :

[1, 2, 3, 4, 5]

construis une nouvelle liste contenant :

[5, 4, 3, 2, 1]

Essaie de le faire avec ce que tu connais déjà.
'''

my_list = [1, 2, 3, 4, 5] 
reversed_list = []

# for i in my_list[::-1]:
#   reversed_list.append(i)

for i in range(len(my_list) -1, -1, -1):
  reversed_list.append(my_list[i])
  
print(reversed_list)
