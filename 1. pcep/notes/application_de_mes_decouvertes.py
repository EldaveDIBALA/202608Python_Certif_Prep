import time
import re
import sys

invalid_input = 0

def add(n, m):
    return n + m

while True or invalid_input < 3:
    try:
        n = int(input("\nEntrer un chiffre n : "))
            
        if n > 5:
            time.sleep(2)
            print(1)
            if n < 11:
                time.sleep(2)
                print(2)
                if n != 10:
                    time.sleep(2)
                    print(3)
                else:
                    if n % 2 == 0:
                        time.sleep(2)
                        print(4)
                    else:
                        time.sleep(2)
                        print(5)
        else:
            time.sleep(2)
            print("\nn est inférieur ou égal à 5")
        
        while True or invalid_input < 3:
            try:
                m = int(input("\nEntrez un chiffre m : "))
                time.sleep(2)
                print(add(n, m))
                break
            except ValueError:
                time.sleep(1)
                if invalid_input < 2:
                    print("\nValeur de m invalide. Entrez un chiffre valide.")
                    invalid_input += 1
                else:
                    break
        sys.exit("\nNombre de tentatives dépassées. Arrêt du programme.")
            
    except ValueError:
        time.sleep(1)
        if invalid_input < 2:
            print("\nValeur de n invalide. Entrez un chiffre valide.")
            invalid_input += 1
        else:
            break
sys.exit("\nNombre de tentatives dépassées. Arrêt du programme.")
