import datetime

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Enter a date (month-day-year): ")
    try:
        if date_input.split('/')[0].isdigit():
            date = datetime.datetime.strptime(date_input, "%m/%d/%Y")
        else:
            date = datetime.datetime.strptime(date_input, "%B %d, %Y")
        break
    except ValueError:
        print("Invalid date, please try again.")

print(date.strftime("%Y-%m-%d"))