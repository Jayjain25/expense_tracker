from curd.add_expense import add_expense
from curd.view_expenses import print_expense
from fetures.filter import filter_print_expense
from fetures.get import get_total_spent
from curd.update_expense import *
from curd.delete_expense import *

def main():
    while True:
        try:
            input_opt = input(
                "\n\nChoose an option:\n1. Add Expense\n2. View Expenses\n3. Filter\n4. Total Amount Spent\n5. Edit Expense\n6. Delete Expense\n7. Exit\n\n"
            )
            if not input_opt.isdigit():
                print("Please enter a valid number (1-7).")
                continue
            input_opt = int(input_opt)

            if input_opt == 1:
                try:
                    amount = int(input("Enter the amount :- "))
                except ValueError:
                    print("Amount must be a number.")
                    continue

                category = input("Name of Category :- ").strip()
                note = input("Enter a Note\n").strip()

                add_expense(amount=amount, category=category, note=note)
                print("Expense added successfully.")

            elif input_opt == 2:
                print_expense()

            elif input_opt == 3:
                category = input("Enter category:- \n").strip().capitalize()
                if not category:
                    print("Category cannot be empty.")
                    continue
                filter_print_expense(category)

            elif input_opt == 4:
                total_spent = get_total_spent()
                print(f"Total Amount Spent: {total_spent}")

            elif input_opt == 5:
                print_expense()
                id = int(input("Enter the ID of the expense to edit: "))
                if id <= 0:
                    print("ID must be a positive integer.")
                    continue
                else:
                    amount = int(input("Enter New Amount (or keep it blank)"))
                    category = input("Enter New Category (or keep it blank)").strip()
                    date_input = input("Enter New Date (dd-mm-yyyy) (or keep it blank): ").strip()
                    note = input("Enter a New Note (or leave it blank)").strip()

                    edit_expense(expense_id= id, amount=amount, category=category, date = date_input, note = note)

            elif input_opt == 6:
                print_expense()
                id = int(input("Enter Id that you want to delete : "))
                delete_expense(id)

            elif input_opt == 7:
                print("\nExiting the program. Goodbye!")
                break

            else:
                print("Please choose a valid option (1-4).")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()