import json
import datetime

def add_expense(amount=0, category="Default", date=None, note=""):
    if category == "":
        category = "Default"
    if date is None:
        date = datetime.datetime.now()

    expenses_file = "expense/expenses.json"
    expenses = []

    # Try to read existing expenses
    try:
        with open(expenses_file, "r") as f:
            expenses = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # File does not exist or is empty/corrupt, start with empty list
        expenses = []

    # Determine new id
    if expenses:
        new_id = expenses[-1]["id"] + 1
    else:
        new_id = 1

    expense = {
        "id": new_id,
        "amount": amount,
        "category": category.capitalize(),
        "date": date.strftime("%d-%m-%Y"),
        "note": note
    }

    expenses.append(expense)

    # Write back the updated list
    with open(expenses_file, "w") as f:
        json.dump(expenses, f, indent=4)
