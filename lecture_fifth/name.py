import sys

try:
    print("Hello my name is ", sys.argv([1]))  # one beacse the first argument is the name of the file
except IndexError:
    print("You must provide a name as an argument")



if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello my name is ", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


print("Hello my name is ", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("Too few arguments") 

for arg in sys.argv[1:]:       # startint from the second argument
    print("Hello my name is ", arg)
