users  = [
    ("Abhishek", "Developer"),
    ("Rahul", "Designer"),
    ("Priya", "Tester"),
]

for user in users:
    name = user[0]
    role = user[1]
    
    print(name, role)

for name, role in users:
    print(name, role)