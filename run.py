import gspread
import pprint
import sys
from pprint import pprint
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
    print("4. Exit program\n")
    options = input("Please enter the number of your chosen option: ")
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
        print("\n************************************")
        print("         EXITING PROGRAM    ")
        print("************************************\n")
        print("Closing program...\n")
        exit_program()
    else:
        print("***Please enter a valid number***")
        options_menu()


def employee_input():
    """
    Takes user input (Employee number)
    """
    while True:

        employee_number = input("Please enter you employee number: ")
        

        if validate_employee_number_count(employee_number):
            print("Employee number is valid!")
            break

    return int(employee_number)


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

# Clock in system


def clock_in_time():
    """
    This function returns the current time.
    """
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")

    return current_time


def find_last_employee_entry(employee_number):
    """
    This function finds the row in Google Sheets of
    number of the employee number that
    was entered by the user
    """
    count = 1
    new_data_set = data[1:]
    for i in new_data_set:
        count += 1
        if employee_number is int(i[0]):

            return count

# Clock Out


def clock_out():
    """
    This function marks the current time and
    and updates the currect loction on google sheets.
    """
    col_count = find_last_employee_entry(employee_input())
    clock_out_time = clock_in_time()
    print("\nYou clocked out at: ", clock_out_time)
    in_out_sheet.update(f"D{col_count}", clock_out_time)
    options_menu()


# Update Google Sheets


def update_in_out_sheet(timestamp_in):
    """
    Updates Google Sheets with given values.
    """
    print("\nUpdating in_out_sheet clock-in time...")
    clocking_sheet = SHEET.worksheet("in_out_sheet")
    clocking_sheet.append_row(timestamp_in)
    print("\nClock in time updated successfully \n ")


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


def add_new_employee():
    """
    This function adds a new employee.
    Once add the function opens the options menu again.
    """
    entering_name = input("Please enter employee name: ")
    newEmployeedAdded = newEmployee(add_one_to_employee_number, entering_name)
    newEmployeedAdded.addingEmployeeDetails()
    print("\nNew employee added successfully: ", employeeList[-1])
    main()


def exit_program():
    """
    This function ends the running of the program.
    """
    sys.exit()


def main():
    """
    The main function fires the options_menu function.
    This is saved here for readability.
    """
    options_menu()

main()
