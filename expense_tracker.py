expenses = []

def add_expense():
    description = input("Description : ")
    amount = float(input("Montant : "))
    
    expenses.append({
        "description": description,
        "amount": amount
    })
    
    print("Depense ajoutee !")


def show_expenses():
    # Travail de l'etudiant B
    pass


def show_total():
    # Travail de l'etudiant B
    pass





def main():
  while True:
   print("\n===== EXPENSE TRACKER =====")
   print("1. Add an expense")
   print("2. View expenses")
   print("3. Show total")
   print("4. Exit")
   print("5. Delete an expense")
   print("6. Show average")
   choice = input("Choose an option: ")
   if choice == "1":
    add_expense()
   elif choice == "2":
    show_expenses()
   elif choice == "3":
    show_total()
   elif choice == "4":
    print("Goodbye!")
    break
   elif choice == "5":
    delete_expense()
   elif choice == "6":
    show_average()
   else:
    print("Invalid option.")
if __name__ == "__main__":
  main()