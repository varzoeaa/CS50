def main():
    name = input("Enter your name: ")
    print(hello(name))

def hello(to="World"):
    return f"Hello, {to}!"

# we cant test if the hello function doesnt return a value
# but rather prints it -> its a side effect