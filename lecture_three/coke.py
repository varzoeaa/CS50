def main():
    total = 50
    while total > 0:
        coin_input = input("Put coins into the vending machine (25, 10, 5): ")
        try:
            coin_input = int(coin_input)
            new_total = inserted_coins(total, coin_input)
            if new_total is not None:  
                total = new_total
                print(f"Amount left: {total}")
            else:
                print("Please try again with a valid coin.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def inserted_coins(total, coin_input):
    if coin_input in [25, 10, 5]:
        new_total = total - coin_input
        return new_total if new_total >= 0 else None
    else:
        print("Invalid coin amount. Please insert 25, 10, or 5.")
        return None

main()
