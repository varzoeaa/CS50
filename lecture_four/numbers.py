while True:
    try: 
        x = int(input("Please enter a number: "))
    except ValueError:
        print("You did not enter a number.")
    else:
        break

print(f"The number you entered is {x}.") 

'''
The variable x is defined inside the while loop. 
Regardless of how many times the loop iterates, x will eventually be assigned 
a valid integer before the loop can break. This means that by the time the print 
statement is reached, x is guaranteed to be defined

Thats why there is no NameError when the print statement is executed.
'''
def main():
    x = get_int()
    print(f"The number you entered is {x}.")

def get_int():
    while True:
        try: 
            return int(input("Please enter a number: "))
        except ValueError:
            print("You did not enter a number.")
    # return is a stornger break statement

main()

