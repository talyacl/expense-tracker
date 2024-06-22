class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def get_total_expense(self):
        return sum(self.expenses.values())

    def get_expenses_by_category(self):
        return self.expenses

    def print_expenses(self):
        print("Expense Tracker:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. View Total Expense")
        print("3. View Expenses by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter the category of the expense: ")
            amount = float(input("Enter the amount spent: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")

        elif choice == '2':
            total_expense = tracker.get_total_expense()
            print(f"Total Expense: ${total_expense}")

        elif choice == '3':
            expenses_by_category = tracker.get_expenses_by_category()
            print("Expenses by Category:")
            for category, amount in expenses_by_category.items():
                print(f"{category}: ${amount}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
