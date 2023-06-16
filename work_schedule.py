import random
from datetime import datetime, timedelta
import csv

def validate_file_format(filename):
    """
    Validates the format of the input file.

    Args:
        filename (str): The name of the input file.

    Returns:
        bool: True if the file format is valid, False otherwise.
    """
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) < 2:
                    return False
                for day in row[1:]:
                    if day not in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
                        return False
    except (FileNotFoundError, csv.Error):
        return False
    return True


def validate_user_input(date_str):
    """
    Validates the user input date.

    Args:
        date_str (str): The user input date string.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        start_date = datetime.strptime(date_str, '%Y-%m-%d')
        if start_date.weekday() != 0:
            return False
    except ValueError:
        return False
    return True


def create_work_schedule(start_date):
    """
    Creates a work schedule for the next seven days based on employee availability.

    Args:
        start_date (datetime.datetime): The start date of the week.

    Returns:
        None
    """
    # Read employee availability from file
    employee_availability = {}
    with open('employees.txt', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) > 1:
                employee = row[0]
                availability = row[1:]
                employee_availability[employee] = availability
    
    # Create work schedule for the next seven days
    print("\nWork Schedule:")
    for i in range(7):
        current_date = start_date + timedelta(days=i)
        current_day = current_date.strftime('%Y-%m-%d (%a)')
        
        # Get available employees for the current day
        available_employees = [
            employee for employee, availability in employee_availability.items() if current_day[12:15] in availability
        ]
        
        if available_employees:
            # Assign a random employee for the current day
            employee = random.choice(available_employees)
            print(f"{current_day}: {employee}")
        else:
            random_employee = random.choice(list(employee_availability.keys()))
            print(f"Warning: no available employees for {current_day[12:15]}, assigned {random_employee}.")
    
    print("\nGoodbye!")


def main():
    """
    The main function of the work schedule app.

    Prompts the user for the start date of the week and creates a work schedule.
    """
    print("Welcome to the work schedule app!\n")

    # Input validation for file format
    if not validate_file_format('employees.txt'):
        print("Invalid file format. Please make sure employees.txt is a valid CSV file with correct weekday abbreviations.")
        return

    while True:
        start_date_str = input("Enter the start date of the week (YYYY-MM-DD): ")
        
        # Input validation for user input
        if validate_user_input(start_date_str):
            break
        else:
            print("Invalid date format or start date is not a Monday. Please enter a valid date.")

    year, month, day = map(int, start_date_str.split('-'))
    start_date = datetime(year, month, day)
    
    create_work_schedule(start_date)

if __name__ == '__main__':
    main()
