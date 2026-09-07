'''
Exercice 16 — Trouver le minimum

Même principe, mais pour trouver le plus petit nombre.
'''

created_list = []

try:
  list_length = int(input("list length: "))

  if list_length > 0:
    
    for i in range(list_length):
      
      number = int(input(f"Number {i + 1}: "))
      created_list.append(number)

    print(f"\nYour created_list: {created_list}")
  
  else:
    print(f"The list must be greater than 0.")

except ValueError:
  print("Invalid input.")
    
if created_list:

  min_number = created_list[0]

  for number in created_list[1:]:
    
    if number < min_number:
      min_number = number
      
  print(f"The minimum entered number is: {min_number}.")

else:
  print("Need numbers to compare.")
