import gspread
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

#Employee Validation

def list_of_employees_numbers():
    """
    Itterates throught employees numbers.
    """
    all_employees_numbers = [num["employeeNumber"] for num in employeeList if "employeeNumber" in num]
    return all_employees_numbers


def employee_input():
    """
    Takes user input (Employee number)
    """
    employee_number = input("Please enter you employee number: ")
    return int(employee_number)
        
class Employee:

    def __init__(self, employee_number, employee_name):
        self.employee_number = employee_number
        self.employee_name = employee_name 

    def find_employee_details(self):
        """
        Takes return value from employee_input()
        Then checks it against employeeNumber in employeeList
        """
        all_employees_numbers = list_of_employees_numbers()
        all_employees_names = itterates_employee_name()
        entered_number_by_employee = employee_input()

        for (self.employee_number, n) in zip(all_employees_numbers, all_employees_names):
            print("This is entered_number_by_employee: ", entered_number_by_employee)

            if entered_number_by_employee is employee_number:
                print(f" {entered_number_by_employee} is = {employee_number} \n")
                print("-->", n)
                return employee_number, n
            else:
                print("is not = \n")
details = Employee(1, "hi")
print(details)
#Find matching emplyee name to user entered employee number

def itterates_employee_name():
    """
    Itterates throught employees names.
    """
    entered_number_by_employee = employee_input()
    all_employees_names = [name["name"] for name in employeeList if "name" in name]
    print(all_employees_names)
    return all_employees_names

# Clock in system
def clock_in_time():
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M")

    return current_time


#Update Google Sheets

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("in_out_sheet")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def transfer_of_data():
    """
    Takes data in and formats to list.
    Updates csv file
    """
    employee_input = Employee(employee_number, employee_name)
    clockin_time = clock_in_time()
    csv_result = [employee_input, clockin_time]
    update_sales_worksheet(csv_result)

def main():
    transfer_of_data()
    
main()