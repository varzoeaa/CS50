with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({f"{name} is in {house}"})

for student in sorted(students):
    print(student)


# this is better bcs we are storing the data in a 
# dictionary, not blending it with the print statement
students = []

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")