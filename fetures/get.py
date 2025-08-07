import json
from curd.view_expenses import view_expense

data = view_expense()

def get_total_spent():
    total = sum(item.get("amount", 0) for item in data)
    return total

