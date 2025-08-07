import json

def view_expense():
    try:
        with open('expense/expenses.json', 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print("Expense file not found.")
        return []
    except json.JSONDecodeError:
        print("Expense file is empty or corrupted.")
        return []

def truncate(text, length):
    text = str(text)
    return text if len(text) <= length else text[:length-3] + "..."

def print_expense():
    data = view_expense()
    if data:
        print("{:<5} {:<10} {:<15} {:<12} {}".format("ID", "Amount", "Category", "Date", "Note"))
        print("-" * 60)
        for d in data:
            print("{:<5} {:<10} {:<15} {:<12} {}".format(
                d.get("id", ""),
                d.get("amount", ""),
                truncate(d.get("category", ""), 15),
                d.get("date", ""),
                truncate(d.get("note", ""), 25)
            ))
    else:
        print("No expenses found.")

# Example usage:
# print_expense()