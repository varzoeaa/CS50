students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])


students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student)    # prints the keys

for student in students:
    print(student, students[student], sep=", ")    # prints the keys and values



students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")   # prints the values