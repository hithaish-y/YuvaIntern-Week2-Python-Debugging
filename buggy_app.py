import json

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_expense(expenses):
    title = input("Expense name: ").strip()
    amount = float(input("Amount: "))
    expenses.append({"title": title, "amount": amount})

def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        for index, expense in enumerate(expenses):
            print(f"{index + 1}. {expense['title']} - ₹{expense['amount']:.2f}")

def delete_expense(expenses):
    number = int(input("Enter expense number to delete: "))
    del expenses[number]
    print("Expense deleted.")

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
