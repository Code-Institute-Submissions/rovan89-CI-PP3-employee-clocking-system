import gspread
import sys
import time
import re
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('employee_clocking_system')

in_out_sheet = SHEET.worksheet('in_out_sheet')
user_feedback = SHEET.worksheet('user_feedback')

data = in_out_sheet.get_all_values()

employeeList = [{
    "employeeNumber": 111,
    "name": "John Doe",
    "hourlyRate": "10.00"
    },
    {
    "employeeNumber": 112,
    "name": "Jane Doe",
    "hourlyRate": "11.00"
    },
    {
    "employeeNumber": 113,
    "name": "Jax Teller",
    "hourlyRate": "17.50"
    },
    {
    "employeeNumber": 114,
    "name": "D'Angelo Barksdale",
    "hourlyRate": "11.00"
    },
    {
    "employeeNumber": 115,
    "name": "Tony Stark",
    "hourlyRate": "13.00"
    },
    {
    "employeeNumber": 116,
    "name": "Matilda Wormwood",
    "hourlyRate": "18.00"
    },
    {
    "employeeNumber": 117,
    "name": "Danny DeVito",
    "hourlyRate": "9.00"
    },
    {
    "employeeNumber": 118,
    "name": "Arnold Schwarzenegger",
    "hourlyRate": "11.50"
    },
    {
    "employeeNumber": 119,
    "name": "Kelly Preston",
    "hourlyRate": "15.00"
    }
]

# User Options Menu


def options_menu():
    """
    Gives user an options menu
    """
    print("\n       *************************")
    print("                WELCOME      ")
    print("       *************************")
    print("Please choose one of the following options:\n")
    print("1. Clock in")
    print("2. Clock out")
    print("3. Add new employee to system")
    print("4. Give Feedback")
    print("5. Exit program\n")
    options = options_input()
    if int(options) == 1:
        print("\n*************************************")
        print("           CLOCKING IN      ")
        print("*************************************\n")
        transfer_of_data()
    elif int(options) == 2:
        print("\n*************************************")
        print("            CLOCKING OUT     ")
        print("*************************************\n")
        clock_out()
    elif int(options) == 3:
        print("\n*************************************")
        print("         ADD NEW EMPLOYEE    ")
        print("*************************************\n")
        add_new_employee()
    elif int(options) == 4:
        print("\n*************************************")
        print("         Give Feedback    ")
        print("*************************************\n")
        userFeedback()
    elif int(options) == 5:
        print("\n************************************")
        print("         EXITING PROGRAM    ")
        print("************************************\n")
        print("Closing program...\n")
        exit_program()
    else:
        print("***Please enter a valid number***")
        options_menu()

def options_input():
    """
    This function takes the users' input from the options menu and validates that input.
    """
    while True:
        options = input("Please enter the number of your chosen option: \n")

        if checks_for_empty_input(options) and validate_options_number_count(options) and checks_for_string_input(options) and validate_check_for_special_char(options):
            print("\nInput is valid! \n")
            return options


def employee_input():
    """
    Takes users' employee number input
    """
    while True:

        employee_number = input("Please enter your employee number: \n")
        employee_num_list = list_of_employees_numbers()

        if validate_employee_number_count(employee_number) and int(employee_number) in employee_num_list:
            print("Employee number is valid!")
            return int(employee_number)
        else:
            print("This is not an employee number\n")
# This section validates user input


def validate_employee_number_count(values):
    """
    Rasises ValueError if value is not an int.
    Checks if there is exactly 3 values.
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"3 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"\nInvalid entry: {e}, please try again\n ")
        return False

    return True

def validate_options_number_count(values):
    """
    Rasises ValueError if value is not an int.
    Checks if there is exactly 1 value.
    """
    try:
        if len(values) != 1:
            raise ValueError(
                f"1 value is required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"\nInvalid entry: {e}, please try again\n ")
        return False

    return True

def checks_for_string_input(values):
    """
    Rasises ValueError if input is a alphabetic input.
    """
    try:
        if values.isalpha():
            raise ValueError(
                f"An alphabetic input is not valid"
            )
    except ValueError as e:
        print(f"\nInvalid entry: {e}, please try again\n ")
        return False

    return True

def checks_for_empty_input(values):
    """
    Rasises ValueError if input in empty.
    """
    try:
        if values == "":
            raise ValueError(
                f"An empty input is not valid"
            )
        elif values == "":
            raise ValueError(
                f"A special character input is not valid"
            )
    except ValueError as e:
        print(f"\nInvalid entry: {e}, please try again\n ")
        return False

    return True

def checks_if_input_is_a_digit(values):
    """
    Rasises ValueError if input is a number.
    """
    try:
        if values.strip().isdigit():
            raise ValueError(
                f"Numbers are not a valid input"
            )
    except ValueError as e:
        print(f"\nInvalid entry: {e}, please try again\n ")
        return False

    return True


def validate_check_for_special_char(values):
    """
    This function raises a value error if a special character has been entered
    """
    special_char = ["[" ,"]" ,"'" ,"@","_","!","$","%","^","&","*","(",")","<",">","?","/","|","}","{","~",":","",";","#","+","=","-", " ",'"',"£", "€",".", ","]
    try:
        if values in special_char:
            raise ValueError(
            f"Special characters are not a valid input"
        )
    except ValueError as e:
        print(f"\nInvalid entry: {e}, please try again\n ")
        return False
        
    return True


def userFeedback():
    """
    This function takes user feedback
    """
    while True:

        feedback = input("Please leave us your feedback: ")

        if checks_for_empty_input(feedback) and checks_if_input_is_a_digit(feedback) and validate_check_for_special_char(feedback):
            print("\nInput is valid! \n")
            update_user_feedback_sheet(feedback)
            options_menu()

# Find matching emplyee name to user entered employee number


def itterates_employee_name():
    """
    Itterates throught employees names.
    """
    all_employees_names = [name["name"] for name in employeeList]
    return all_employees_names


def list_of_employees_numbers():
    """
    Itterates throught employees numbers.
    """
    all_employees_numbers = [num["employeeNumber"] for num in employeeList]
    return all_employees_numbers


def itterate_through_employee_details(employee_number):
    """
    Iterates through both lists: list_of_employees_numbers and
    itterates_employee_name.
    This alows the program to find to corresponding row in
    Google Sheets.
    """
    for l, n in zip(list_of_employees_numbers(), itterates_employee_name()):
        if employee_number is l:
            employee_details = [l, n]
            return employee_details
        else:
            continue

# Update Google Sheets


def update_in_out_sheet(timestamp_in):
    """
    Updates the employee in_out_sheet with given values in google sheets.
    """
    print("\nUpdating in_out_sheet clock-in time...")
    clocking_sheet = SHEET.worksheet("in_out_sheet")
    clocking_sheet.append_row(timestamp_in)
    print("\nClock in time updated successfully \n ")


def update_user_feedback_sheet(user_fb):
    """
    This function updates the user_feedback_sheet in google sheets
    """
    print("Updating feedback worksheet...\n")
    feedback_worksheet = SHEET.worksheet("user_feedback")
    feedback_worksheet.append_row([user_fb])
    print("Feedback worksheet updated successfully. \n")


def transfer_of_data():
    """
    Takes data in and formats to list.
    Updates csv file
    """
    employee_number = employee_input()
    employee_details = itterate_through_employee_details(employee_number)
    clockin_time = clock_in_time()
    print("\nYou clocked in at: ", clockin_time)
    csv_result = employee_details + [clockin_time]
    update_in_out_sheet(csv_result)
    options_menu()

# Create a New Employee


class newEmployee:
    """
    This class allows the user to enter the necessary values to
    create a new instance of an employee
    and add it to the employeeList list.
    """
    def __init__(self, employeeNumber, name):
        self.employeeNumber = employeeNumber
        self.name = name

    def addingEmployeeDetails(self):
        employee = {
            "employeeNumber": int(f"{self.employeeNumber}"),
            "name": f"{self.name}",
            }
        employeeList.append(employee)

last_employee_in_employeeList = employeeList[-1]["employeeNumber"]
add_one_to_employee_number = int(last_employee_in_employeeList+1)


def new_employee_input():
    """
    This function takes requests the name of the new employee from the user.
    It also checks if the input is valid.
    """
    while True:
        entering_name = input("Please enter employee name: \n")

        if checks_for_empty_input(entering_name) and validate_check_for_special_char(entering_name) and checks_if_input_is_a_digit(entering_name):
            print("\nInput is valid! \n")
            return entering_name


def add_new_employee():
    """
    This function adds a new employee.
    Once add the function opens the options menu again.
    """
    entering_name = new_employee_input()
    validate_check_for_special_char(entering_name)
    newEmployeedAdded = newEmployee(add_one_to_employee_number, entering_name)
    newEmployeedAdded.addingEmployeeDetails()
    print("\nNew employee added successfully: ", employeeList[-1])
    main()

# Clock in system


def clock_in_time():
    """
    This function returns the current time.
    """
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")

    return current_time



# Clock Out


def clock_out():
    """
    This function marks the current time and
    and updates on google sheets.
    """
   
    row_count = find_last_employee_entry(employee_input())
    clock_out_time = clock_in_time()
    print("\nYou clocked out at: ", clock_out_time)
    in_out_sheet.update(row_count, clock_out_time)
    options_menu()

def find_last_employee_entry(employee_number):
    """
    This function finds the row in Google Sheets of
    number of the employee number that
    was entered by the user
    """
    row_count = 1
    values_list = in_out_sheet.col_values(1)
    values_list = values_list[1:]
    for val in values_list:
        row_count += 1
        cell_val = int(in_out_sheet.acell(f"A{row_count}").value)
        if int(cell_val) == employee_number:
            cell_location = f"D{row_count}"
            return cell_location



# Exit program


def exit_program():
    """
    This function ends the running of the program.
    """
    sys.exit()

# Run program


def main():
    """
    The main function fires the options_menu function.
    This is saved here for readability.
    """
    options_menu()

main()
