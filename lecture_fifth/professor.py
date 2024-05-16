from random import randrange, randint


def main():
    number = get_level()
    x, y = generate_integer(number)
    generate_math_problems(x, y)


def get_level():
    while True:
        x = int(input("Enter the level (1, 2, or 3): "))
        if x in [1, 2, 3]:
            break
    return x


def generate_integer(level):

    if level == 1:
        y = randint(1, 9)
        x = randint(1, 9)
    elif level == 2:
        y = randint(10, 99)
        x = randint(10, 99)
    elif level == 3:
        y = randint(100, 999)
        x = randint(100, 999)
    
    return x, y


def generate_math_problems(x, y):
    
    answer = x + y 
    attempts = 0

    while attempts < 3:
        try:
            user_answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if user_answer == answer:
            print("Correct!")
            return
        else:
            print("EEE")
            attempts += 1
        
        
    print(f"Sorry, the answer was {answer}")


if __name__ == "__main__":
    main()