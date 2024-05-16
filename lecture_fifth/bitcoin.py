import requests
import sys
import json

def main():
    number = get_num_bitcoins()
    price = get_bitcoin_price(number)

    print(f"{number} bitcoins are worth {price} euros.")



def get_num_bitcoins():

    if len(sys.argv) < 2:
        sys.exit()
    elif len(sys.argv) > 2:
        sys.exit()
    elif len(sys.argv) == 2:
        try:
            number = float(sys.argv[1])
        except ValueError:
            sys.exit()
    
    return number

def get_bitcoin_price(number):

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()

    for bpi in data["bpi"]:
        if bpi == "EUR":
            price = data["bpi"][bpi]["rate_float"]
            return price * number
    
if __name__ == "__main__":
    main()
