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
            "employeeNumber": f"{self.employeeNumber}",
            "name": f"{self.name}",
            "hourlyRate": f"{self.hourlyRate}"
            }
        employeeList.append(employee)

last_employee_in_employeeList = employeeList[-1]["employeeNumber"]
add_one_to_employee_number = int(last_employee_in_employeeList+1 )
print("***", add_one_to_employee_number)


entering_name = input("Please enter employee name: ")
entering_hourly_rate = input("Please enter employee hourly rate: ")
newEmployeedAdded = newEmployee(add_one_to_employee_number, entering_name, entering_hourly_rate)
print("This is the new employee number: " , newEmployeedAdded.employeeNumber)
print("This is the new employee's name: ", newEmployeedAdded.name)
print("This is the new employee hourly rate: ", newEmployeedAdded.hourlyRate)
print(">>>", newEmployeedAdded.addingEmployeeDetails())


print(employeeList)
