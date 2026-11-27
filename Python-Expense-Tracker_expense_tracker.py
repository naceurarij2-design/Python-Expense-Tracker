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
    if not expenses:
        print("No expenses recorded.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")


def show_total():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)

    print(f"Total : {total:.2f}")
    print(f"Average expense: {average:.2f}")


def delete_expense():
    if not expenses:
        print("No expenses recorded.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")

    choice = input("Expense number to delete: ")

    if not choice.isdigit():
        print("Invalid expense number.")
        return

    index = int(choice) - 1

    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['description']}")

        if expenses:
            average = sum(expense["amount"] for expense in expenses) / len(expenses)
            print(f"Average expense: {average:.2f}")
        else:
            print("No expenses recorded.")
    else:
        print("Invalid expense number.")


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