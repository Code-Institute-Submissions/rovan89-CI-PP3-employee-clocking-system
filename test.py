from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# Link to Google Sheets
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

#List of employees and their details

employeeList = [ {
    "employeeNumber": 111,
    "name": "John Doe",
    "hourlyRate": "10.00"
    },
    {
    "employeeNumber": 112,
    "name": "Jane Doe",
    "hourlyRate": "11.00"
    }
]

#Options Menu

def options_menu():
    """ 
    Gives user an options menu
    """
    print("Please choose one of the following options:\n 1. Clock in \n 2. Clock out\n 3. Add new employee to system")
    options = input("Please enter the number that corresponds with the option you would like to choose: ")
    print(options)
    if int(options) == 1:
        clock_in()
    elif int(options) == 2:
        clock_out()
    elif int(options) == 3:
        adding_new_employee()
    else:
        print("***You can only choose one of the given options, please enter a valid number***")
        options_menu()

#Employee CLock-in Validation and timestamp
def clock_in():
    print("Running Clock in function")
    employee_input()

def clock_out():
    print("Running Clockout")

def adding_new_employee():
    print("Running adding_new_employee()")

def validate_employee_number_count(values):
    """
    Rasises ValueError if value is not an int.
    Checks if there is exactly 3 values.
    """
    print(values)
    try: 
        if len(values) != 3:
            raise ValueError(
                f"3 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again\n ")
        return False

    return True

def employee_input():
    """
    This function takes in the employee number
    """
    while True:

        employee_number = input("Please enter you employee number: ")
        validate_employee_number_count(employee_number)

        if validate_employee_number_count(employee_number):
            print("Employee number is valid!")
            break

    return int(employee_number)

returned_input = type(employee_input())
print("!!!",returned_input)
test_list = []
test_list.append("Hi")
print(test_list)



# Clock in system
def clock_in_time():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")
    print(current_time)
    current_time = current_time.split(':')
    print(current_time)
    current_time = [int(time) for time in current_time]
    print(current_time)

    return current_time

timestamp_in = clock_in_time()
entered_number_by_employee = employee_input()
print(">>>", entered_number_by_employee)
print(clock_in)

def update_in_out_sheet(timestamp_in):
    print("Updating in_out_sheet clock-in time...")
    clocking_sheet = SHEET.worksheet("in_out_sheet")
    clocking_sheet.append_row(entered_number_by_employee, timestamp_in)
    print("Clock in time updated successfully")
update_in_out_sheet(clock_in_time)

options_menu()
    