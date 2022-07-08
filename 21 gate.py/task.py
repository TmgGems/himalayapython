emails=[
    "1@gmail.com",
    "2@yahoo.com",
    "3@gmail.com",
    "4@outlook.com",
    "5@gmail.com",
    "gmail.com67"
]
output=list(filter(lambda n:n.endswith("@gmail.com"),emails))
print(output)
