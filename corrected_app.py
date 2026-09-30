import json

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: expenses.json is invalid. Starting with an empty list.")
        return []

def add_expense(expenses):
    title = input("Expense name: ").strip()
    if not title:
        print("Expense name cannot be empty.")
        return
    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid numeric amount.")
        return
    expenses.append({"title": title, "amount": amount})
    print("Expense added.")

def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['title']} - ₹{expense['amount']:.2f}")

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return
    try:
        number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return
    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return
    deleted = expenses.pop(number - 1)
    print(f"Deleted: {deleted['title']}")

def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
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
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
