student = {
    "first_name": "Samanta",
    "age" : 19,
    "level" : "L200",
    "id" : 100,
    "courses" : ['math', 'english', 'computer'],
    "scores" : [80, 20, 33]
}

# print(student["courses"][0])

for key in student:
    print(f"{key}: {student[key]}")