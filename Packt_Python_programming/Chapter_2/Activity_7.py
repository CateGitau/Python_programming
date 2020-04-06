"""
 store and access our data more effectively using these two data types – lists and dictionaries
"""

employees  =employees = [
    {"name": "John Mckee", "age":38, "department":"Sales"},
    {"name": "Lisa Crawford", "age":29, "department":"Marketing"},
    {"name": "Sujan Patel", "age":33, "department":"HR"}
]

for employee in employees:
    print("Name:", employee['name'])
    print("Age:", employee['age'])
    print("Department:", employee['department'])
    print('-' * 20)

for employee in employees:
    if employee['name'] == 'Sujan Patel':
        print("Name:", employee['name'])
        print("Age:", employee['age'])
        print("Department:", employee['department'])
        print('-' * 20)