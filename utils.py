import datetime


def get_number_or_quit(self):
    while True:
        user_input = input("Please enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Quitting...")
            break
        try:
            number = int(user_input)
            self.numbers.append(number)
            print(f"You entered the number: {number}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if 1 in self.numbers:
        self.numbers = [1]
        print("List contained 1, all other numbers removed.")
    print(f"Final list of numbers: {self.numbers}")
    return self.numbers


def get_user_dates(self):
    date_format = "%m/%d/%Y"
    while True:
        try:
            start_date = input("Enter the starting date (MM/DD/YYYY): ")
            start_date_obj = datetime.strptime(start_date, date_format)
            end_date = input("Enter the ending date (MM/DD/YYYY): ")
            end_date_obj = datetime.strptime(end_date, date_format)
            if end_date_obj < start_date_obj:
                print("Ending date must be after the starting date. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter the date in MM/DD/YYYY format.")
    return start_date, end_date
