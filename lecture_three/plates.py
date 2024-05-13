def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    # starts w aat least 2 letters
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # no special characters
    if not plate.isalnum():
        return False

    # integers must be at the end
    has_number_started = False
    for i in range(len(plate)):
        if plate[i].isdigit():
            # integer middle or at the start
            if plate[i] == '0' and i == 2:  # first integer cant be zero
                return False
            if not has_number_started:
                has_number_started = True  
        elif has_number_started:  
            return False
    
    return True

main()
