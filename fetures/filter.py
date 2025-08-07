import json
from curd.view_expenses import view_expense

data = view_expense()

def truncate(text, length):
    text = str(text)
    return text if len(text) <= length else text[:length-3] + "..."

def filter_print_expense(category):
    data = view_expense()
    if data:
        print("{:<5} {:<10} {:<15} {:<12} {}".format("ID", "Amount", "Category", "Date", "Note"))
        print("-" * 60)
        for d in data:
            if category in d.get("category", ""):
                print("{:<5} {:<10} {:<15} {:<12} {}".format(
                    d.get("id", ""),
                    d.get("amount", ""),
                    truncate(d.get("category", ""), 15),
                    d.get("date", ""),
                    truncate(d.get("note", ""), 25)
                ))
    else:
        print("No expenses found.")