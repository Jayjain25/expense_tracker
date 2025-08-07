import json
from curd.view_expenses import view_expense

def edit_expense(expense_id, amount=None, category=None, date=None, note=None):
    try:
        data = view_expense()  # Always get the latest data
        updated = False

        for expense in data:
            # Ensure both are int for comparison
            if int(expense.get("id", 0)) == int(expense_id):
                if amount:
                    expense["amount"] = amount
                if category:
                    expense["category"] = category.capitalize()
                if date:
                    # Accept both string and datetime
                    if hasattr(date, "strftime"):
                        expense["date"] = date.strftime("%d-%m-%Y")
                    else:
                        expense["date"] = str(date)
                if note:
                    expense["note"] = note
                updated = True
                break  # Stop after finding the expense

        if updated:
            with open('expense/expenses.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Expense updated successfully.")
        else:
            print("Expense ID not found.")

    except Exception as e:
        print(f"Exception Occurred: {e}")

# Example usage:
# edit_expense(1, amount=500, note="Updated note")