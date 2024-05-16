from random import randrange

x = int(input("Enter the level: "))
number = randrange(1, x)
guess = int(input("Guess the number: "))

while guess != number:
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    guess = int(input("Guess the number: "))

print("You guessed the number!")