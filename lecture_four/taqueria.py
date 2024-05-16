def main():
    # Menu items and prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    total_cost = 0.0

    try:
        while True:
            item = input("Enter item: ")
            # Normalize the input to match the menu keys
            normalized_item = item.strip().title()
            if normalized_item in menu:
                total_cost += menu[normalized_item]
                print(f"Total: ${total_cost:.2f}")
            else:
                print("Item not on the menu. Please try again.")
    except EOFError:
        print("\nOrder complete.")
        print(f"Final Total: ${total_cost:.2f}")

main()
