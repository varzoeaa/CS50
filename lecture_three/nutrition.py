def main():
    # fruit dictionary
    fruits_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    fruit_input = input("Enter a fruit: ").lower()

    # output calories
    if fruit_input in fruits_calories:
        print(f"The number of calories in one portion of {fruit_input} is {fruits_calories[fruit_input]} calories.")
    else:
        print("The fruit entered is not on the list. Please input a valid fruit name.")

if __name__ == "__main__":
    main()
