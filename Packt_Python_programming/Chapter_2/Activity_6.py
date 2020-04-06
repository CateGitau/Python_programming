employees = [['John Mckee', 38, 'Sales'], ['Lisa Crawford', 29, 'Marketing'], ['Sujan Patel', 33, 'HR']]
print(employees)


for employee in employees:
    print(employee)

for employee in employees:
    print("Name:", employee[0])
    print("Age", employee[1])
    print("Department: ", employee[2])
    print('-' * 20)

employee = employees[1]
print(employee)
print("Name:", employee[0])
print("Age:", employee[1])
print("Department:", employee[2])
print('-' * 20)