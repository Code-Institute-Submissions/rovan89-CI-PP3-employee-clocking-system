import gspread
from google.oauth2.service_account import Credentials

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

#print(data)

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

print(employeeList)

def options_menu():
    """ 
    Gives user an options menu
    """
    print("Please choose one of the following options:\n 1. Clock in \n 2. Clock out\n 3. Add new employee to system")
    options = input("Please enter the number that corresponds with the option you would like to choose: ")
    if int(options) == 1:
        clock_in()
    elif int(options) == 2:
        #clock_out()
        pass
    elif int(options) == 3:
        add_new_employee()
    else:
        print("***You can only choose one of the given options, please enter a valid number***")
        options_menu()

class newEmployee:
    """
    This class allows the user to enter the necessary values to create a new instance of an employee
    and add it to the employeeList list. 
    """
    def __init__(self, employeeNumber, name, hourlyRate):
        self.employeeNumber = employeeNumber
        self.name = name
        self.hourlyRate = hourlyRate

    def addingEmployeeDetails(self):
        employee = {
            "employeeNumber": int(f"{self.employeeNumber}"),
            "name": f"{self.name}",
            "hourlyRate": f"{self.hourlyRate}"
            }
        employeeList.append(employee)

last_employee_in_employeeList = employeeList[-1]["employeeNumber"]
add_one_to_employee_number = int(last_employee_in_employeeList+1)
print("***", int(add_one_to_employee_number))

def add_new_employee():
    entering_name = input("Please enter employee name: ")
    entering_hourly_rate = input("Please enter employee hourly rate: ")
    newEmployeedAdded = newEmployee(add_one_to_employee_number, entering_name, entering_hourly_rate)
    print("This is the new employee number: " , newEmployeedAdded.employeeNumber)
    print("This is the new employee's name: ", newEmployeedAdded.name)
    print("This is the new employee hourly rate: ", newEmployeedAdded.hourlyRate)
    newEmployeedAdded.addingEmployeeDetails()

options_menu()
print(employeeList)