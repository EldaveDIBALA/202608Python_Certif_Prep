import sys
import time

print(f"\n{'='*80}\n{'ATM System':^80}\n{'='*80}\n") # print a formatted header for the ATM system

account = {
    "account_number": "123456789",
    "pin": "1234",
    "balance": 1000.0,
    "type": "business"
}

invalid_pin = 0

while invalid_pin >= 0:
  pin = input("Enter your PIN: ") # prompt user to input their PIN
  time.sleep(2)
  
  if pin == account["pin"]: # check if the entered PIN matches the account's PIN
      invalid_pin = 0
      print("\nAccess granted 😃!") # print access granted message
      
      while True:
        print("\n1. Check Balance") # print option to check balance
        print("2. Account Details") # print option to check account details
        print("3. Deposit Money") # print option to deposit money
        print("4. Withdraw Money") # print option to withdraw money
        print("5. Exit") # print option to exit the system
        
        choice = input("\nEnter your choice (1-5): ") # prompt user to input their choice

        if choice == "1":
          print(f"Current Balance: €{account['balance']:.2f}") # print the current balance formatted to 2 decimal places
          
          time.sleep(3)
          pursue = input("Do you want to pursue?")
          
          if  pursue == "Oui":
            continue
          else:
            break
          
        elif choice == "2":
          print(f"Account Number: {account['account_number']}") # print the account number
          print(f"Account Type: {account['type']}") # print the account type
          
        elif choice == "3":
          try:
            amount_deposit = float(input("How much do you want to deposit? \nAmount deposit of: "))
            
            if amount_deposit > 0:
              account["balance"] += amount_deposit
              print("Money deposited successfully!")
              print(f"Current Balance: €{account['balance']:.2f}") # print the current balance formatted to 2 decimal places
            else:
              print("\nYou have to deposit money for this option.")
          
          except ValueError:
            print("\nError: invalid format.")
          
        elif choice == "4":
          try:
            withdraw_money = float(input("How much do you want to withdraw? \nWithdraw an amount of: "))
            
            if withdraw_money <= 0:
              print("Invalid amount!")
            elif withdraw_money > account["balance"]:
              print("Insufficient balance!")
            else:
              account["balance"] -= withdraw_money
              print(f"New Balance: €{account['balance']:.2f}") # print the current balance formatted to 2 decimal places
              time.sleep(2)
              print("\nCollect your cash and your card!\n")
          
          except ValueError:
            time.sleep(2)
            print("\nError: invalid format.")
            
        elif choice == "5":
          time.sleep(4)
          print("Thank you! \nCollect your card.\n")
          print(f"{"="*80}\n")
          sys.exit()
        
        else:
          print("\nInvalid choice!")

  else:
      print("😑 Wrong pin!")
      invalid_pin += 1
      
      if invalid_pin == 3:
        print("Limit reached!")
        time.sleep(2)
        print("\nYour card will be hold! 📞 Contact your bank for more informations.")
        break

print(f"\n{'='*80}\n")

time.sleep(3)
sys.exit()

# ===========================================================================================
# 🎯 TO-DO / OBJECTIFS D'APPRENTISSAGE POUR FAIRE ÉVOLUER L'ATM
# ===========================================================================================
# [ ] OBJ 1 : Découper le code en fonctions (ex: pin_check(), withdraw_management())
# [ ] OBJ 2 : Boucler sur les erreurs de saisie (float) jusqu'à avoir une valeur valide
# [ ] OBJ 3 : Transformer le dictionnaire account en une classe CompteBancaire (POO)
# [ ] OBJ 4 : Sécuriser le PIN et le solde en attributs privés (Encapsulation)
# [ ] OBJ 5 : Sauvegarder le solde dans un fichier texte/JSON pour conserver les données
# [ ] OBJ 6 : Migrer vers une base SQLite pour gérer plusieurs comptes clients
# ===========================================================================================
