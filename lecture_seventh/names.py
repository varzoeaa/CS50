
names = []

for _ in range(3):
    name = input("Enter a name: ")
    names.append(name)

for name in sorted(names):
    print(f"Hello, {name}!")


name = input("Enter a name: ")

# open the file in a way i can write to it, also if it doesn't exist, create it
# the "w" also recreates the file if it already exists
file = open("names.txt", "a")   # open the file in append mode
file.write(name + "\n")  
# write the name to the file
file.close()  # close the file

with open("names.txt", "r") as file:
    file.write(name + "\n")  


with open("names.txt", "r") as file:
    lines = file.readlines()       # read all the lines in the file

for line in lines:
    print("Hello, " + line.rstrip())     # remove the newline character from the end of the line


# bring it all togethet
with open ("names.txt", "r") as file:
    for line in file:             # read the file line by line
        print("Hello, " + line.rstrip())
