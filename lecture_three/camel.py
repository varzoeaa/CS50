def main():
    camel_case_input = input("Enter the variable name in camel case: ")
    snake_case_output = camel_to_snake(camel_case_input)
    print("Snake case variable name:", snake_case_output)


def camel_to_snake(name):
    snake_case = []  # storing
    for i, char in enumerate(name):
        if char.isupper():  
            if i == 0:   # first character
                snake_case.append(char.lower())
            else:
                snake_case.append('_' + char.lower())
        else:
            snake_case.append(char)
    return ''.join(snake_case) 

main()
