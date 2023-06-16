# work_schedule

Here's an explanation of what the code does:

The code defines a function called create_work_schedule(start_date) that takes a start_date as input. This function is responsible for creating the work schedule for the next seven days based on employee availability.

Inside the create_work_schedule() function:

It reads the employee availability from the employees.txt file and stores it in the employee_availability dictionary. Each employee's name is mapped to a list of days they are available to work.
It then proceeds to create the work schedule for the next seven days.
For each day, it checks the availability of employees and randomly assigns one of them to work on that day.
If there are no available employees for a particular day, it selects a random employee from the available list of employees and assigns them to work, displaying a warning message.
The code also defines a main() function that serves as the entry point of the program.

It displays a welcome message to the user.
It prompts the user to enter the start date of the week in the format "YYYY-MM-DD".
It validates the user input, ensuring that the date is in the correct format and corresponds to a Monday.
If the input is valid, it calls the create_work_schedule() function with the provided start date.
If the input is invalid, it displays an error message and prompts the user to enter another date.
Finally, the code checks if the module is being run as the main script (using if __name__ == '__main__':) and calls the main() function to start the program.

When executed, the program reads the employee availability from the file, prompts the user for the start date, and generates a work schedule for the next seven days based on the availability data. It assigns random employees to work on each day and displays the schedule. If there are no available employees for a specific day, it assigns a random employee and displays a warning message.
