print("""Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80
""")

bubblegum = 200
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

print(f"Income: ${income}")

cal_staff_expenses = int(input("Staff Expenses:"))
staff_expenses = income - cal_staff_expenses
print(staff_expenses)

cal_other_expenses = int(input("Other Expenses:"))
other_expenses = income - cal_other_expenses
print(other_expenses)

