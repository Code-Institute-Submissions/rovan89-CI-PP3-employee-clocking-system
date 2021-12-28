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


def employee_input():
    employee_number = input("Please enter you employee number: ")
    return int(employee_number)
print(type(employee_input()))


list_of_numbers = []
def list_of_employees_numbers(employee_number):
    """
    Itterates throught employees numbers.
    """
    for num in employeeList:
        list_of_numbers.append(num["employeeNumber"])
    return list_of_numbers



class Clocking:
    """
    This class will take three values for clocking in and out
    1. Employee Number
    2. Employee Name
    3. clocking time
    Then it will update the clocking sheet
    """

    def __init__(self, employee_name, employee_number, clocking_time):
        self.employee_name = employee_name
        self.employee_number = employee_number
        self.clocking_time = clocking_time

    def update_sheet(self):
        print(f"Name: {self.employee_name} Number: {self.employee_number} Time: {self.clocking_time}", )
        print(self.employee_name, self.employee_number, self.clocking_time)
        return self.employee_name, self.employee_number, self.clocking_time
        
        
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
    data = employee_input()
    csv_result = [data]
    update_sales_worksheet(csv_result)

def main():
    entered_number_by_employee = employee_input()
    employee_id = int(entered_number_by_employee)
    print(">>>", employee_id)
    print("User entered: ", entered_number_by_employee)
    #new_data_entry_by_user = Clocking.(employee_id, "Blank", "Blank2")
    #print("new_data_entry_by_user: ", new_data_entry_by_user())
    transfer_of_data()
main()

