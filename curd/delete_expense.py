import json
from curd.view_expenses import view_expense

def delete_expense(expense_id):
    try:
        data = view_expense()  
        deleted = False

        for expense in data:
            # Ensure both are int for comparison
            if int(expense.get("id", 0)) == int(expense_id):
                data.remove(expense)
                deleted = True
                break  # Stop after finding the expense

        if deleted:
            with open('expense/expenses.json', 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Expense ID : {id} deleted successfully.")
        else:
            print("Expense ID not found.")

    except Exception as e:
        print(f"Exception Occurred: {e}")