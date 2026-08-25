import sys
import time

############################################################################################################################



print(f"\n{"=" * 68}")

############################################################################################################################

"""

Exercise 4

Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace
each 0 with x, and print the modified string to the screen. Use the skeleton below:

"""

for digit in "0165031806510":
    
    if digit == "0":
        modified_string = digit.replace("0", "x") # Line of code.
        #print(digit) # Line of code.
        continue

    #continue # Line of code.
    print(modified_string)

sys.exit()
    
print(f"\n{"=" * 68}")

############################################################################################################################

"""

Exercice 3

Create a program with a for loop and a break statement. The program should iterate over characters in an email
address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton
below:

"""

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break # Line of code.
    print(ch, end="")# Line of code.
    
print(f"\n{"=" * 68}")

############################################################################################################################

"""

Exercise 2

Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

"""

x = 1

while x < 11:
    
    # Line of code.
    if x % 2 != 0:
        
        # Line of code.
        print(x)
        
    # Line of code.
    x += 1
    
# print("Limite 11 atteinte.")

print(f"\n{"=" * 68}")

############################################################################################################################

"""

Exercise 1

Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

"""

for i in range(0, 11):
    # Line of code.

    if i % 2 != 0:
        # Line of code.
        print(i)

print(f"\n{"=" * 68}")

############################################################################################################################
