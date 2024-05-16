def main():
    hello("worrld")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!")

# if we call main() from the command line, then everytime we use these functions
# in other files then it will output world first then the name we pass in
if "__name__" == "__main__":
    main()