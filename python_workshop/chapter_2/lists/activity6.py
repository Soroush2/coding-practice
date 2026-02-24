employee=[
    ["John Mckee",'38', 'Sales'],
    ['Lisa Crawfor','29','Marketing'],
    ['Sujan Patle','33','HR']
]
print(employee)
for row in employee:
    print(f"Name: {row[0]}\nAge: {row[1]}\nDepartment: {row[2]}")
print(f"Name: {employee[1][0]}\nAge: {employee[1][1]}\nDepartment: {employee[1][2]}")